def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": "<h1>Hello from nubinix technologies</h1><p>This was deployed via GitHub Actions.</p>"
    }
