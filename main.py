#!./env/bin/python

import requests
import os
import sys
from flask import Flask, request, Response
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

LISTENING_PORT = os.environ.get('LISTENING_PORT', 8000)
TLGM_BOT_TOKEN = os.environ.get('TLGM_BOT_TOKEN')
# if TLGM_BOT_TOKEN:
#     except Exception as error:
#         print(error)
#     exit(1)


def send_telegram(message):
    bot_token = TLGM_BOT_TOKEN
    url = "http://tlgm.lvlup.dev-stream.ru/bot"
    dst_id = "-259175544"
    method = url + bot_token + '/sendMessage'
    res = requests.post(method, data={
        "chat_id": dst_id,
        "text": message
    })
    return res


@app.route('/1/smsmessaging/outbound/SmartU/requests', methods=['GET', 'POST'])
def index():
    req = request
    if req.is_json:
        message = str(req.get_json().get('address')[0] + ' Message ' + req.get_json().get('outboundSMSTextMessage').get('message'))
        print(message)
        return Response(send_telegram(message))
    else:
        return 'invalid request'


if __name__ == "__main__":
    app.run(port=LISTENING_PORT)
