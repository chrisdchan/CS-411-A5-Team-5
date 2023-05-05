import requests
import os
from dotenv import load_dotenv
load_dotenv()

ASSEMBLY_KEY = os.getenv("ASSEMBLY_API_KEY")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")


def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data


def handle(file):
    headers = {'authorization': f"{ASSEMBLY_KEY}"}
    response = requests.post('https://api.assemblyai.com/v2/upload',
                             headers=headers,
                             data=read_file(file))

    url = response.json()['upload_url']

    endpoint = "https://api.assemblyai.com/v2/transcript"
    json = {"audio_url": str(url)}
    headers = {
        "authorization": f"{ASSEMBLY_KEY}",
        "content-type": "application/json"
    }
    response = requests.post(endpoint, json=json, headers=headers)

    return response.json()
