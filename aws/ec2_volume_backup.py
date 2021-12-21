import boto3

ec2_client = boto3.client('ec2', region_name='eu-central-1')
#ec2_resourse = boto3.resource('ec2', region_name='eu-central-1')

volumes = ec2_client.describe_volumes()

for vol in volumes['Volumes']:
    new_snapshot = ec2_client.create_snapshot(VolumeId=vol['VolumeId'])
    #print(new_snapshot)

