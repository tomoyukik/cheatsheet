# Django cheat

## カレントディレクトリでプロジェクト作成

### 先にディレクトリ作成する場合

```
mkdir sample_project
cd sample_project
django-admin startproject sample_project .
```

### ディレクトリを同時に作成する場合

```
django-admin startproject sample_project
```

## アプリ作成

```
python3 manage.py startapp transportation_system
```

## サーバ起動

```
python3 manage.py runserver
```

## django App 作成手順

```
django-admin startproject myapp
cd myapp
python3 manage.py startapp polls
```

### viewを設定

```polls/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

### urlを設定

作成が必要

```polls/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

デフォルトで存在する

```myapp/urls.py
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

### appのsettings

```
vim myapp/settings.py
# database (sqlite/postgres/mysql/etc...)
# timezone
# etc...設定
```

```myapp/settings.py
INSTALLED_APPS = [
    'polls.apps.PollsConfig', # 追記
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

```


### migration

```
python3 manage.py migrate
```

```
python3 manage.py makemigrations polls
python3 manage.py sqlmigrate polls 0001 # sqlが見られるだけ
python3 manage.py migrate # 実際のmigration
```

### admin画面にモデルを認識させる

```polls/admin.py
from .models import Question

admin.site.register(Question)

```

### viewでtemplateを使用する

```
mkdir polls/templates/polls
```

```polls/template/index.html
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li>
            <a href="/polls/{{ question.id }}/">{{ question.question_test }}</a>
        </li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

```polls/views.py
from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
            'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

`{% if True %}`や`{{ object.id }}`のようにしてコードを埋め込める
viewで見えるか見えないかが違う。
`{% endif %}`や`{% endfor %}`が必要

あるいは以下も可

```
from django.shortcuts import render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
            'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
```

### staticなファイルについて

```
mkdir -p polls/static/polls
```

### まとめ

- viewの追加
  1. polls/view.pyにメソッドを追加
  2. polls/urls.pyにurlを追加
  3. 未設定ならmyapp/urls.pyにも設定を追加

## admin spaceの管理

```
python manage.py createsuperuser
```

`localhost/admin` でアクセス

## djangoのモデル定義例

```polls/models.py
from django.db import models

class Question(models.Model):
    # フィールドの定義
    #   field_name = mdoels.DataType(conditions)
    question_test = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') # Field の最初の位置引数には、オプションとして人間可読なフィールド名も指定できます。
```

## appのパッケージ化

https://docs.djangoproject.com/ja/3.1/intro/reusable-apps/

```
root_dir/
    app/
    README.rst
    LICENSE
    setup.cfg
    setup.py
    MANIFEST.in
```

```
python setup.py sdist
```

dist/django-app-0.1.tar.gz ができる

### install

```
python -m pip install --user path/to/django-app-0.1.tar.gz
```

## test

### modelのtest

```polls/tests.py
import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
```

### viewのtest

ほとんどmodelのtestと同じ

### ブラウザのtest

LiveServerTestCaseはseleniumと連携しやすい

https://docs.djangoproject.com/ja/3.1/topics/testing/tools/#django.test.LiveServerTestCase

### テストされてない部分を見つける

コードカバレッジをチェックする
https://docs.djangoproject.com/ja/3.1/topics/testing/advanced/#topics-testing-code-coverage


### 汎用template

```polls/urls.py
from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

### migration

空のmigration

```
python manage.py makemigrations --empty
```

### bootstrap使い方

https://github.com/zostera/django-bootstrap4

```
pip install django-bootstrap4
```

```
INSTALLED_APPS = {
    "bootstrap4",
}
```

```
{% load bootstrap4 %}

{# Display a form #}

<form action="/url/to/submit/" method="post" class="form">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% buttons %}
        <button type="submit" class="btn btn-primary">Submit</button>
    {% endbuttons %}
</form>
```
