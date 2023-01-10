import json
import os
import boto3


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ["MOCK_API_TABLE"])


def get_project_list_handler(event, context):
    response = table.scan()
    return {
        "statusCode": 200,
        "body": json.dumps(response['Items'])
    }
