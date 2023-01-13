import json
import winreg as reg
import os       
from flask import Flask, request

mock_file = open('mock.json', encoding='utf-8')
data = json.load(mock_file)
mock_file.close()

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'SMALL API TEST SCHEMA'

@app.route('/test/<document>', methods=['GET'])
def getDocument(document):
    for item in data:
        if document == item['documento']:
            return json.dumps(item), 200, {'content-type':'application/json'}
    return {}


if __name__ == '__main__':
    app.run(port=3001, debug=True)