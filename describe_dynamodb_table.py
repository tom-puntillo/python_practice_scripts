import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.describe_table(
    TableName='Directors',
)

print(response)