import os
import json
import boto3
import requests
import time

bClient = boto3.client("lambda")    # this require IAM: 

def lambda_handler(event, context):
    #allLambdaFuncList = bClient.list_functions() # lambda function would try to list all the function under its scope as defiend in <serverless.yaml>
    
    # print the lambda context
    print("Lambda function ARN:", context.invoked_function_arn)
    print("CloudWatch log stream name:", context.log_stream_name)
    print("CloudWatch log group name:",  context.log_group_name)
    print("Lambda Request ID:", context.aws_request_id)
    print("Lambda function memory limits in MB:", context.memory_limit_in_mb)
    
    # We have added a 1 second delay so you can see the time remaining in get_remaining_time_in_millis.
    time.sleep(1) 
    print("Lambda time remaining in MS:", context.get_remaining_time_in_millis())


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello Mr. {}!, Welcome to JA's Code Lab".format(os.environ['FIRST_NAME']),
            "eventPayload": event
            #"All Lambda Functions": json.dumps({"a": allLambdaFuncList})
        }),
    }

