import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Director',
            'AttributeType': 'S',
        },
        {
            'AttributeName': 'MovieTitle',
            'AttributeType': 'S',
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'Director',
            'KeyType': 'HASH',
        },
        {
            'AttributeName': 'MovieTitle',
            'KeyType': 'RANGE',
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5,
    },
    TableName='Directors',
)

print(response)