import json
import time
import boto3

# Note: Define boto3 outside the handler.hello() function scope
client = boto3.client("lambda");


def hello(event, context):
    # body = {
    #     "message": "Go Serverless v1.0! Your function executed successfully!",
    #     "input": event
    # }

    # response = {
    #     "statusCode": 200,
    #     "body": json.dumps(body)
    # }

    # invoke the boto3 client and get all the lambda functions

    print("Hello World")  # this will go into function log

    time.sleep(4)

    return {
        "message": "Passed the 3s Timeout Barrier.. into the Another Hello World!",
        "event": event
    }

    # # print the lambda contexts
    # print("Lambda function ARN:", context.invoked_function_arn)
    # print("CloudWatch log stream name:", context.log_stream_name)
    # print("CloudWatch log group name:",  context.log_group_name)
    # print("Lambda Request ID:", context.aws_request_id)
    # print("Lambda function memory limits in MB:", context.memory_limit_in_mb)
    # # We have added a 1 second delay so you can see the time remaining in get_remaining_time_in_millis.
    # time.sleep(1) 
    # print("Lambda time remaining in MS:", context.get_remaining_time_in_millis())

    # return response

    # # Use this code if you don't use the http event with the LAMBDA-PROXY
    # # integration
    # """
    # return {
    #     "message": "Go Serverless v1.0! Your function executed successfully!",
    #     "event": event
    # }
    # """
