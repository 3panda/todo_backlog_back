#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import os
import json
import urllib


def lambda_handler(event, context):
    try:
        HOST = os.environ['HOST']
        API_KEY = os.environ['API_KEY']

        # 課題の追加
        # ${HOST}/api/v2/issues?${API_KEY}

        # フロントから渡る値を設定
        data = {
            'projectId': event['requestParameters']['project_id'],  # 課題を登録するプロジェクトのID
            'summary': event['requestParameters']['summary'],  # 課題の件名
            'assigneeId': event['requestParameters']['assignee_id'],  # 課題の担当者ID
            'issueTypeId': event['requestParameters']['issue_type_id'],  # 課題の種別のID
            'priorityId': event['requestParameters']['priority_id'],  # 課題の優先度のID
            'description': event['requestParameters']['description']  # 課題の詳細
        }
        r = requests.post(HOST + '/api/v2/issues?' + API_KEY, data=data)

        r_json = r.json()
        # print(r.json())
        # print("-----")
        # print(r_json['keyId'])
        issues_id = r_json['id']

        # issues_id = 11111

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