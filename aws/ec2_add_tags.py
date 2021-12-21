import boto3

ec2_client = boto3.client('ec2', region_name='eu-central-1')
ec2_resourse = boto3.resource('ec2', region_name='eu-central-1')

instances = ec2_client.describe_instances()


instances_ids = []

for rsrv in instances['Reservations']:
    instances_ids.append(rsrv['Instances'][0]['InstanceId'])

#print(instances_ids)

response = ec2_resourse.create_tags(
    Resources=instances_ids,
    Tags=[
        {
            'Key': 'Environment',
            'Value': 'Prod'
        },
    ]
)

