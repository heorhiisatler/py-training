import requests
from telegram import t_notify

try:
    responce = requests.get('http://ec2-52-58-55-252.eu-central-1.compute.amazonaws.com:9080/')
    #if False:
    if responce.status_code == 200:
        print('Application is running successfully!')
    else:
        msg = f'Application down with code "{responce.status_code}", fixe it!'
        print(msg)
        #send telegram message
        t_notify(msg)
except Exception as ex:
    msg = f'Connection error happened "{ex}", fixe it!'
    print(msg)
    t_notify(msg)