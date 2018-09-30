from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

import requests
import io
import base64
import json
import os

def to_text(audio_file, config):
    b64_audio = base64.b64encode(audio_file)
    
    api_key_env = str(os.environ['API_KEY'])
    url = 'https://speech.googleapis.com/v1/speech:recognize?key='+api_key_env

    json_data = {
        "config": config,
        "audio": {"content": b64_audio.decode("utf-8")}
    }

    response = requests.post(url, json=json_data)
    return response.json()

def request_handler(request):
    response = to_text(request.body, json.loads(request.POST["config"]))
    return response

if __name__ == '__main__':
    config = Configurator()

    config.add_route('to_text', '/to_text')

    config.add_view(request_handler, route_name='to_text', renderer='json', request_method='POST')

    app = config.make_wsgi_app()
    server = make_server('', 80, app)
    server.serve_forever()
