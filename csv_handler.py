import csv
import json
import requests

csv_output = "test_out.csv"
csv_input = 'test.csv'
url = 'http://127.0.0.1:3001/test'

def readFileAndOperate(filename, apiUrl):
    results = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            document = row['name'].split('.')[0]
            url = "{0}/{1}".format(apiUrl, document)
            response = requests.get(url)
            data=json.loads(response.text)
            if data:
                results.append(data)
        saveFile(results)
        

def saveFile(data):
    with open(csv_output, 'w', newline='') as csvfile:
        fieldnames = ['documento', 'status', 'creatAt']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow({'documento': item['documento'], 'status': item['metadata']['razaoSocial'],'creatAt':item['criadoEm']})

readFileAndOperate(csv_input, url)
