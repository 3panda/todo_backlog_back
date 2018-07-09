#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import os


def lambda_handler(event, context):
    HOST = os.environ['HOST']
    PROJECT_KEY = os.environ['PROJECT_KEY']
    API_KEY = os.environ['API_KEY']

    # 仮
    ISSUE_TYPE_ID = 147348
    PRIORITY_ID = 1
    PROJECT_ID = 32538
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
        'issueTypeId': ISSUE_TYPE_ID,  # 課題の種別のID
        'priorityId': PRIORITY_ID,  # 課題の優先度のID
        'description': description  # 課題の詳細
    }
    r = requests.post(HOST + '/api/v2/issues?' + API_KEY, data=data)
    print(r.json())

