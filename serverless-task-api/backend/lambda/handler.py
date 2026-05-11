import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):

    method = event.get("httpMethod")

    if method == "POST":
        body = json.loads(event.get('body') or "{}")

        task = {
            "taskId": str(uuid.uuid4()),
            "title": body.get("title", "Untitled Task"),
            "createdAt": datetime.utcnow().isoformat()
        }

        table.put_item(Item=task)

        return {
            "statusCode": 200,
            "body": json.dumps(task)
        }

    elif method == "GET":
        response = table.scan()

        return {
            "statusCode": 200,
            "body": json.dumps(response.get("Items", []))
        }

    elif method == "DELETE":
        params = event.get("queryStringParameters") or {}
        task_id = params.get("taskId")

        if not task_id:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "taskId is required"})
            }

        table.delete_item(Key={"taskId": task_id})

        return {
            "statusCode": 200,
            "body": json.dumps({"message": f"Task {task_id} deleted"})
        }

    return {
        "statusCode": 400,
        "body": json.dumps({"error": "Unsupported method"})
    }