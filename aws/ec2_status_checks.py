import boto3
import schedule
from telegram import t_notify

ec2_client = boto3.client('ec2', region_name='eu-central-1')
#ec2_resourse = boto3.resource('ec2', region_name='eu-central-1')

#instances = ec2_client.describe_instances()

#for rsrv in instances['Reservations']:
    #print(rsrv['Instances'])
#    for inst in rsrv['Instances']:
#        print('Server: {}    State: {}'.format(inst['Tags'][0]['Value'], 
#                                               inst['State']['Name']))

def check_instance_status():
    instance_status = ec2_client.describe_instance_status(
        IncludeAllInstances=True
    )
    t_mes = ''
    for status in instance_status['InstanceStatuses']:
        t_mes = t_mes + ('Instance "{}" is {} with state "{}" \n').\
                         format(status['InstanceId'],
                         status['InstanceState']['Name'],
                         status['InstanceStatus']['Status'])
    print(t_mes)
    if t_mes == '':
        t_notify('Error - Empty result')
    else:
        t_notify(t_mes)


schedule.every(20).seconds.do(check_instance_status)

while True:
    schedule.run_pending()