import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.put_item(
    Item={
        'Director': {
            'S': 'steven_speilberg',
        },
        'MovieTitle': {
            'S': 'jaws',
        },
    },
    ReturnConsumedCapacity='TOTAL',
    TableName='Directors',
)

print(response)