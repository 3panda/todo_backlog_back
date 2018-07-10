
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
        ISSUE_ID = 1135285

        params = {
            'statusId': 4,
            'comment': '完了しました'
        }

        print(HOST)
        print(PROJECT_KEY)
        print(API_KEY)
        r = requests.patch(HOST + '/api/v2/issues/' + str(ISSUE_ID) + '?' + API_KEY, params=params)
        print(r.json())

        return {
            'statusCode': 200,
            'headers': {
                'access-control-allow-origin': '*',
                'content-type': 'application/json'
            },
            'data': {'issues_id': ISSUE_ID},
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