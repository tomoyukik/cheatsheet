# 環境設定

社内でDeepRacerのトレーニング環境を提供する際の環境構築例。
SageMakerを活用したトレーニングを行える環境の構築を行う。

## アクセスキー管理

AWS CLIを使用してモデル作成・提出を行うにはアクセスキーが必要となるので、アクセスキー利用のポリシーを作成する。

<!-- TODO -->
*※ アクセスキーは90日ごとのローテーションが推奨されているので、対策は要検討*

### アクセスキーポリシー

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowViewAccountInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetAccountPasswordPolicy",
                "iam:GetAccountSummary"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowManageOwnAccessKeys",
            "Effect": "Allow",
            "Action": [
                "iam:CreateAccessKey",
                "iam:DeleteAccessKey",
                "iam:ListAccessKeys",
                "iam:UpdateAccessKey"
            ],
            "Resource": "arn:aws:iam::*:user/${aws:username}"
        }
    ]
}
```

### 参考

- [IAM ユーザーのアクセスキーの管理](https://docs.aws.amazon.com/ja_jp/IAM/latest/UserGuide/id_credentials_access-keys.html)
- [Best practices for managing AWS access keys](https://docs.aws.amazon.com/accounts/latest/reference/credentials-access-keys-best-practices.html)
- [自分のアクセスキーの作成・更新](https://docs.aws.amazon.com/ja_jp/IAM/latest/UserGuide/reference_policies_examples_aws_my-sec-creds-self-manage-pass-accesskeys-ssh.html)

## S3管理

SageMakerを利用してモデルのトレーニングを行う場合、報酬関数など、シークレットにしたいファイルがS3にアップロードされる。
そのためユーザごとにアクセスを制限された環境が必要になる。

管理を簡単にするため、一つのバケット内にユーザごとのフォルダを作成し、フォルダごとにユーザのアクセス権限を設定する。
フォルダ名に各ユーザのフレンドリ名を用い、ポリシー作成時にポリシー変数を使用してポリシーを作成する。

*※ バケット名はグローバルに一意 (世界中で唯一) である必要があるため、会社名と日時情報を含めることを推奨する。*
*※ 本ポリシーでは、ユーザはバケット直下へのアクセス権限を持つことができないため、自分に割り当てられたフォルダに直接アクセスする必要がある。*

バケット名は、`s3://会社名-aws-deepracer-test-作成日時`だとする(例: `s3://mycompany-aws-deepracer-test-20221131201905`)。

### S3ポリシー

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
          "Action": ["s3:ListBucket"],
          "Effect": "Allow",
          "Resource": ["arn:aws:s3:::会社名-aws-deepracer-test-作成日時"]
        },
        {
          "Action": [
            "s3:GetObject",
            "s3:PutObject",
            "s3:DeleteObject"
          ],
          "Effect": "Allow",
          "Resource": ["arn:aws:s3:::会社名-aws-deepracer-test-作成日時/${aws:username}/*"]
        },
        {
            "Action": [
                "s3:CreateBucket",
                "s3:DeleteBucket"
            ],
            "Effect": "Deny",
            "Resource": "*"
        }
    ]
}
```

### 参考

- <https://dev.classmethod.jp/articles/iam-user-for-each-s3bucket/>


## SageMakerの管理ポリシー

SageMakerのNotebookインスタンスもS3同様、各インスタンスへのアクセス権をユーザごとに制限したい。
各インスタンスにタグを割り当て、タグの値により条件を設定することで、ユーザごとのアクセス権を設定する。

*※ タグを削除した場合に、アクセス権限を失うため、タグの削除・更新が出来ないよう制限するなど、何らかの対応の検討は必要となる*

### SageMakerポリシー

以下ポリシーでは、SageMaker NotebookInstanceに`user`タグに各ユーザのフレンドリ名を設定し、タグ名による条件付けをすることで各インスタンスへの接続を制限している。

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sagemaker:ListNotebookInstances",
                "sagemaker:BatchGetMetrics",
                "sagemaker:BatchPutMetrics",
                "sagemaker:*Training*",
                "sagemaker:List*"
            ],
            "Resource": "*",
        },
        {
            "Effect": "Allow",
            "Action": [
                "sagemaker:CreatePresignedNotebookInstanceUrl",
                "sagemaker:UpdateNotebookInstance",
                "sagemaker:StopNotebookInstance",
                "sagemaker:DescribeNotebookInstance",
                "sagemaker:StartNotebookInstance"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "sagemaker:ResourceTag/user": "${aws:username}"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcs"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:ListRoles",
                "iam:PassRole"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "kms:List*"
            ],
            "Resource": "*"
        }
    ]
}
```

### 参考

- <https://dev.classmethod.jp/articles/sagemaker-restrict-access/>
    - tagを使って制御する
- sagemakerのpolicy
    - <https://docs.aws.amazon.com/ja_jp/sagemaker/latest/dg/api-permissions-reference.html>
