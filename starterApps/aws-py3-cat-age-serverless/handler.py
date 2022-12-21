import os
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def hello(event, context):
    logger.info("## ENVIRONMENT VARIBALES")
    logger.info(os.environ)

    logger.info("## EVENT RECEIVED")
    logger.info(event)


    # Business Logic
    # multiply the cat age we received from event by 7
    multiFactor =7
    catAge = event['age'] * multiFactor

    logger.info("## CAT AGE AFTER HUMAN TRANSFORMATION")
    logger.info(catAge)
    

    body = {
        "message": "Serverless Cat Age Calculator",
        "input": event,
        "catAge": catAge

    }

    response = {
        # for http API call rerequire the responseStatusCode and headerType
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
