# todo_backlog_back
todo listの内容をBacklogに記録するWebアプリのバックエンド処理

## 前提条件
- Backの処理はAWS Lambda
- APIはAmazon API Gateway 
-  利用ライブラリー requests

## Lambda関数
以下のディレクトリにrequests(ライブラリ)を個別に取得しZip圧縮でLambdaにアップロードする
- add_backlog_issue
- get_backlog_data
- update_backlog_issue

## requestsの個別インストール方法
各ディレクトリで以下を実行
```
pip install requests -t .
```

## Lambdaに設定する環境変数
各Lambdaに設定する環境変数は以下

- HOST
ex) https://xxxxx.backlog.jp
- PROJECT_KEY
BacklogのProject key
ex) TODOLIST
- API_KEY
Backlog API KEY
ex) apiKey=#####YOUR_API_KEY#####

## API Gateway
Lambdaに紐付けるために以下を別途用意
- add_backlog_issue
Method: POST
- get_backlog_data
Method: GET
- update_backlog_issue
Method: POST

### 注意
フロント側でAjaxでやりとりするためCORSを有効にする必要がある



