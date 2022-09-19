import boto3
from time import gmtime, strftime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserDetails')

def lambda_handler(event, context):

    EmailID1 = event['EmailID']
    FName1 = event['FName']
    LName1 = event['LName']
    now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    response = table.put_item(
        Item={
            'EmailID' : EmailID1,
            'LatestGreetingTime' : now,
			'FName' : FName1,
			'LName' : LName1
            })
    return {'statusCode': 200}