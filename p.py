from __future__ import print_function  # Python 2/3 compatibility
import json
import boto3

# AWS_ACCESS = ""
# AWS_SECRET = ""
AWS_REGION = "eu-west-3"
TABLE_NAME = "users"

client = boto3.client(
    'dynamodb',
    # aws_secret_access_key=AWS_SECRET,
    # aws_access_key_id=AWS_ACCESS,
    region_name=AWS_REGION)

response = client.scan(
    TableName='Music',
    Select='ALL_ATTRIBUTES',
    ReturnConsumedCapacity='TOTAL'
)
# print(json.dumps(response))
with open(TABLE_NAME+'.json', 'w') as f:
    print(json.dumps(response), file=f)
