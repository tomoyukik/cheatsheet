# import pytest
from expression import app

def test_abc():
    client = app.test_client()
    result = client.get('abc')
    print(result.data)
    assert result.data == b'123'

def test_not_abc():
    client = app.test_client()
    result = client.get('abc')
    print(result.data)
    assert not result.data == b'111'

def test_add():
    client = app.test_client()
    result = client.get('add?n=2&m=3')
    print(result.data)
    assert result.data == b'5'

def test_sabtract_not():
    client = app.test_client()
    result = client.get('sabtract?n=25&m=15')
    print(result.data)
    assert result.data == b'10'

def test_dic():
    client = app.test_client()
    result = client.get('dic')
    print(result.data)
    # assert result.data == {'one': 1, 'two': 2}