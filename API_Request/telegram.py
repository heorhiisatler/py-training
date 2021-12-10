import json
import requests

def t_notify(message):
    k_path = 'training-code\py-training\API_Request\keys.json'
    with open(k_path, 'r') as keys_file:
        k = json.load(keys_file)
        token = k['telegram_token']
        chat_id = k['telegram_chat_id']
    t_message_url = ('https://api.telegram.org/'
                     'bot{}/sendMessage?chat_id={}'
                     '&text={}').format(token, chat_id, message)
    #print(t_message_url)
    requests.get(t_message_url)

t_notify("Test message")

