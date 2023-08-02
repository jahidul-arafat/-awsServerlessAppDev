import json
import time
import uuid

import boto3

dynamodb = boto3.resource('dynamodb')
table_name = 'calculator-db'
table = dynamodb.Table(table_name)


def hello(event, context):
    # Measure the start time of the Lambda function execution
    start_time = time.time()

    # get query string parameter inputs
    # only for the API call
    x = event['queryStringParameters']['x']
    y = event['queryStringParameters']['y']
    op = event['queryStringParameters']['op']

    # to invoke with the event payload, instead of query string parameters
    # x = event["x"]
    # y = event["y"]
    # op = event["op"]

    # log the inputs
    print(f"x:{x}, y:{y}, op:{op}")

    # prepare the response body
    response_body = {
        'x': x,
        'y': y,
        'op': op,
        'output': calc(x, y, op)
    }

    # Calculate the total execution time and billing duration
    end_time = time.time()
    execution_time = round((end_time - start_time) * 1000,
                           2)  # Convert the execution time to milliseconds as float with two decimal points

    # Calculate the billed duration
    # Convert memory_used to an integer
    memory_used = int(context.memory_limit_in_mb)
    billing_duration = round(((execution_time / 100) * (memory_used / 64)) * 1000,
                             2)  # converting seconds to milliseconds

    # Include the execution time and billing duration in the response body
    response_body['execution_time'] = execution_time
    response_body['billing_duration'] = billing_duration

    # store the data in dynamodb
    print("Storing data in DynamoDB ....")
    store_in_dynamodb(response_body, context)

    # prepare the http response
    http_response = {
        'statusCode': 200,
        'Content-Type': 'application/json',
        'body': json.dumps(response_body)
    }

    print("Returning response .....")
    return http_response


# method to do mathematical calculations on two numbers based on the choice of operation
def calc(a, b, op):
    a = float(a)
    b = float(b)
    op = op.lower().strip()

    if op == 'add':
        return a + b
    elif op == 'sub':
        return a - b
    elif op == 'mul':
        return a * b
    elif op == 'div':
        # handle division by zero
        if b == 0:
            return 0
        return a / b
    else:
        return 0


# method to store the data in dynamodb
def store_in_dynamodb(response_body, context):
    item = {
        'id': str(uuid.uuid4()),  # Generate a unique ID for the item
        'x': str(response_body['x']),
        'y': str(response_body['y']),
        'op': str(response_body['op']),
        'output': str(response_body['output']),  # Convert the numeric output to string before storing in DynamoDB
        'log_stream_name': context.log_stream_name,
        'execution_time': str(response_body['execution_time']),
        'billing_duration': str(response_body['billing_duration'])
    }
    table.put_item(Item=item)
