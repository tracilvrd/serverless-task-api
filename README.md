# Serverless Task Management API
A fully serverless REST API built using AWS services to manage tasks.
The system supports creating, retrieving, updating and deleting tasks using a scalable, event-driven architecture.

# Architecture
AWS Lambda (compute)
Amazon API Gateway (API layer)
Amazon DynamoDB (database)

# Flow:
Client → API Gateway → Lambda → DynamoDB → Response

# Features
Create tasks (POST /tasks)
Retrieve tasks (GET /tasks)
Delete tasks (DELETE /tasks?taskId=...)


# Tech Stack
Python (Lambda runtime)
AWS Lambda
Amazon API Gateway
Amazon DynamoDB

# API Endpoints
POST /tasks
Creates a new task
Request:
{
  "title": "Sample task"
}
Response:
{
  "taskId": "uuid",
  "title": "Sample task",
  "createdAt": "timestamp"
}

GET /tasks
Returns all tasks
Response:
[
  {
    "taskId": "uuid",
    "title": "Sample task"
  }
]

DELETE /tasks
Deletes a task
Query:
/tasks?taskId=uuid
Response:
{
  "message": "Task deleted"
}

# Setup Guide
1. Create DynamoDB table Tasks
2. Deploy Lambda function
3. Configure API Gateway routes
4. Deploy API to prod stage

# What This Project Demonstrates
1. Serverless architecture design
2. REST API development using API Gateway
3. Lambda function integration
4. NoSQL data modeling with DynamoDB
5. End-to-end request handling

# Future Improvements
 - Add PUT endpoint (update task)
 - Add authentication (JWT / Cognito)
 - Implement pagination for large datasets
 - CI/CD pipeline for automated deployment


# Author
Ese Daniel
