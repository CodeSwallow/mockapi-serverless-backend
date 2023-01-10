import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ["MOCK_API_TABLE"])


def get_project_detail_handler(event, context):
    response = table.get_item(
        Key={
            'id': event["pathParameters"]["id"]
        }
    )

    if 'Item' in response:
        return {
            "statusCode": 200,
            "body": json.dumps(response['Item'])
        }

    return {
        "statusCode": 404,
        "body": json.dumps({
            "message": "Project not found"
        }),
    }
