import boto3

sqs = boto3.client('sqs')

queue_name = "practice_queue"

response = sqs.create_queue(
    QueueName=queue_name 
)

print(response)