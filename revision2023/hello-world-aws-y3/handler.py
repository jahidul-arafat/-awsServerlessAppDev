import json
import os
import time
import boto3

# Note: Define boto3 outside the handler.hello() function scope
# Purpose
'''
(1) To get all Lambda Function deployed under my aws account
(2) Print a OS environment varible named "FIRST_NAME" passes as variable in <serverless.yml>
(3) Print the payload passed in the Event which triggered the AWS Lambda Function
(4) Print the Context - information about the execution environment of Lambda Function
(5) Print an OS Environment variable


IAM Dependencies:
(1) For boto.list_functions() >> Allow lambda:* for all-resoures


'''
bClient = boto3.client("lambda")  # this require IAM:


def hello(event, context):
    print("Received Event: ", event)
    allLambdaFuncList = bClient.list_functions()  # lambda function would try to list all the function under its scope as defiend in <serverless.yaml>

    #print("Person Executing this Script is {} from {}".format(event["name"], event["site"]))

    body = {
        #"message": "Hello {}!, Welcome to JA's Code Lab".format(os.environ["FIRST_NAME"]),
        "statusCode": 200,
        "eventPayload": event,
        "All Lambda Functions": allLambdaFuncList,
    }

    # return the boay as reponse, at the same time make sure the body info is logged in AWS CloudWatch
    # print("Body: ", body)

    # print the lambda context
    print("Lambda function ARN:", context.invoked_function_arn)
    print("CloudWatch log stream name:", context.log_stream_name)
    print("CloudWatch log group name:", context.log_group_name)
    print("Lambda Request ID:", context.aws_request_id)
    print("Lambda function memory limits in MB:", context.memory_limit_in_mb)

    # We have added a 1 second delay so you can see the time remaining in get_remaining_time_in_millis.
    time.sleep(1)
    print("Lambda time remaining in MS:", context.get_remaining_time_in_millis())

    # prepare the http response
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }

    # return the response
    return response


