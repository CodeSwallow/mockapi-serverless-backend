import json
import os
import boto3


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ["MOCK_API_TABLE"])


def post_project_handler(event, context):
    print(event)
    response = table.put_item(
        Item={
            'id': event['id'],
            'name': event['title'],
            'description': event['description'],
            'models': event['models']
        }
    )
    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
