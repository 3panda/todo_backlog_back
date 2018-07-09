#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import os

def lambda_handler(event, context):
    issue_id = 1135285
    params = {
        'statusId': 4,
        'comment': '完了しました'
    }
    r = requests.patch(HOST + '/api/v2/issues/' + str(issue_id) + '?' + API_KEY, params=params)
    print(r.json())
