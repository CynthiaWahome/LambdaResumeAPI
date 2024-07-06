import json
import boto3

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Resumes')

def lambda_handler(event, context):
    # Extract resumeId from pathParameters in the event
    resume_id = event['pathParameters']['id']  # assuming id is passed as a path parameter

    try:
        # Retrieve item from DynamoDB based on resumeId
        response = table.get_item(
            Key={
                'resumeId': resume_id
            }
        )
        
        # Check if the item exists
        item = response.get('Item')
        if not item:
            # If resume not found, return 404 status code
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Resume not found'})
            }

        # If resume found, return 200 status code and the resume data
        return {
            'statusCode': 200,
            'body': json.dumps(item)
        }
    
    except Exception as e:
        # Return 500 status code and error message if any exception occurs
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }
