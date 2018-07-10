#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import os
import json
import urllib


def lambda_handler(event, context):
    try:
        HOST = os.environ['HOST']
        PROJECT_KEY = os.environ['PROJECT_KEY']
        API_KEY = os.environ['API_KEY']

        # 仮 フロントから渡る値
        ISSUE_TYPE_ID = 147348
        PRIORITY_ID = 1
        PROJECT_ID = 32538
        My_ID = 84381

        print(HOST)
        print(PROJECT_KEY)
        print(API_KEY)

        # 課題の追加
        # ${HOST}/api/v2/issues?${API_KEY}
        description = """===
        これは課題投稿のテストです。
        Backlog APIを利用してPythonから課題を投稿しています。
        ===

        """
        data = {
            'projectId': PROJECT_ID,  # 課題を登録するプロジェクトのID
            'summary': '課題投稿サンプル',  # 課題の件名
            'assigneeId': My_ID,  # 課題の担当者ID
            'issueTypeId': ISSUE_TYPE_ID,  # 課題の種別のID
            'priorityId': PRIORITY_ID,  # 課題の優先度のID
            'description': description  # 課題の詳細
        }
        r = requests.post(HOST + '/api/v2/issues?' + API_KEY, data=data)
        print(r.json())

        issues_id = 9999
        return {
            'statusCode': 200,
            'headers': {
                'access-control-allow-origin': '*',
                'content-type': 'application/json'
            },
            'data': {'issues_id': issues_id},
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