import requests
import json
#import os

#FACEBOOK_GRAPH_URL = os.environ.get('FACEBOOK_GRAPH_URL')
#CONTENT_TYPE = os.environ.get('CONTENT_TYPE')
FACEBOOK_GRAPH_URL = "https://graph.facebook.com/v2.6/me/"
CONTENT_TYPE = "application/json"

class Bot(object):
    def __init__(self, access_token, api_url = FACEBOOK_GRAPH_URL):
        self.access_token = access_token
        self.api_url = api_url

    #Enviamos el mensaje
    def send_text_message(self, psid, message, messaging_type = "RESPONSE"):
        headers = {
            'Content-Type': CONTENT_TYPE
        }

        data = {
            'messaging_type': messaging_type,
            'recipient': {
                'id': psid
            },
            'message': {
                'text': message,                
            }
        }

        params = {
            'access_token': self.access_token
        }

        self.api_url = self.api_url + 'messages'
        #Enviamos una solicitud de publicación
        response = requests.post(self.api_url,
                                 headers = headers,
                                 params = params,
                                 data = json.dumps(data))
        print(response.content)   