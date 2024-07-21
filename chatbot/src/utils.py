import json

import requests

def call_llama (model, prompt, stream=False):
    url = "http://localhost:11434/api/generate"
    data = {
        "model":model,
        "prompt":prompt,
        "stream":stream
    }
    json_data = json.dumps(data)
    response = requests.post(url, data=json_data,headers={'Content-Type':'application/json'})
    if requests.status_codes == 200:
        return response.json()
    else:
        return f'Error: {response.status_code}'
    