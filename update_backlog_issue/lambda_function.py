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

        print(event)
        # フォームに入力されたデータを得る
        #param = urllib.parse.parse_qs(event['requestParameters'])
        #print(param)
        # 仮 フロントから渡る値
        #issues_id = 1157408
        issues_id = event['requestParameters']['issues_id']

        params = {
            'statusId': 4,
            'comment': '完了しました'
        }

        print(HOST)
        print(PROJECT_KEY)
        print(API_KEY)
        r = requests.patch(HOST + '/api/v2/issues/' + str(issues_id) + '?' + API_KEY, params=params)
        # print(r.json())

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