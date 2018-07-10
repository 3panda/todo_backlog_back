#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.parse
import requests
import os
import json
import urllib


def lambda_handler(event, context):
    try:

        HOST = os.environ['HOST']
        PROJECT_KEY = os.environ['PROJECT_KEY']
        API_KEY = os.environ['API_KEY']

        print(HOST)
        print(PROJECT_KEY)
        print(API_KEY)

        r = get_users_info(HOST, API_KEY)
        MY_ID = r.json()['id']

        print(MY_ID)

        # プロジェクト情報取得
        # ${HOST}/api/v2/projects/${PROJECT_ID}?${API_KEY}
        r = requests.get(HOST + '/api/v2/projects/' + PROJECT_KEY + '?' + API_KEY)
        PROJECT_ID = r.json()['id']
        print(r.json())

        # 種別一覧の取得
        # ${HOST}/api/v2/projects/${PROJECT_ID}/issueTypes?${API_KEY}
        r = requests.get(HOST + '/api/v2/projects/' + PROJECT_KEY + '/issueTypes?' + API_KEY)
        print(r.json())
        ISSUE_TYPE_ID = r.json()[0]['id']

        # 優先度一覧の取得
        # ${HOST}/api/v2/priorities?${API_KEY}
        r = requests.get(HOST + '/api/v2/priorities?' + API_KEY)
        print(r.json())

        PRIORITY_ID = r.json()[0]['id']

        # 課題一覧
        print("------------")
        # ${HOST}/api/v2/issues/${PROJECT_ID}/issueTypes?${API_KEY}
        params = {
            'assigneeId[]': MY_ID,
            'statusId[]': 1
        }
        r = requests.get(HOST + '/api/v2/issues?' + API_KEY, params=params)

        issues_data = r.json()
        print(issues_data)


        return {
            'statusCode': 200,
            'headers': {
                    'access-control-allow-origin': '*',
                    'content-type': 'application/json'
            },
            'data': issues_data,
            'completed': 1

        }

    except:
        import traceback
        traceback.print_exc()
        return {
            'statusCode': 200,
            'headers': {
                    'access-control-allow-origin': '*',
                    'content-type': 'application/json'
            },
            'completed': 0
        }


def get_users_info(host: str, api_key: str):
    # ユーザ情報の取得
    # GET ${HOST}/api/v2/users/myself?${API_KEY}
    # r = requests.get(host + '/api/v2/users/myself?' + api_key)
    r = requests.get(host + '/api/v2/users/myself?' + api_key)
    return r