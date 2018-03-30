from requests_oauthlib import OAuth1Session
from requests_oauthlib import OAuth1
import requests
import pandas as pd
import csv
import sys
if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO
import time

class PyRyxApi:

    def __init__(self, client_key, client_secret, gallery_url):
        self.client_key = client_key
        self.client_secret = client_secret
        self.gallery_url = gallery_url


    def generateAyxEndpoint(self, operation, method):
        req_url = self.gallery_url + '{operation}/{method}/'.format(operation=operation,
                                                             method=method)
        return req_url

    def generateAyxRequest(self, endpoint):
        queryoauth = OAuth1(self.client_key, self.client_secret, signature_type='query')
        return requests.get(endpoint, auth=queryoauth)

    def getSubscriptionWorkflows(self):
        endpoint = self.generateAyxEndpoint('workflows', 'subscription')
        return self.generateAyxRequest(endpoint).json()

    def getWorkflowQuestions(self, app_id):
        endpoint = self.generateAyxEndpoint('workflows', app_id) + 'questions/'
        return self.generateAyxRequest(endpoint).json()

    def getWorkflowJobs(self, app_id):
        endpoint = self.generateAyxEndpoint('workflows', app_id) + 'jobs/'
        return self.generateAyxRequest(endpoint).json()


    def checkJobState(self, job_id):
        endpoint = self.generateAyxEndpoint('jobs', job_id)
        return self.generateAyxRequest(endpoint).json()


    def getJobOutput(self, job_id, output_id):
        endpoint = self.generateAyxEndpoint('jobs', job_id)
        endpoint = endpoint + 'output/{output_id}/'.format(output_id=output_id)
        queryoauth = OAuth1(self.client_key, self.client_secret, signature_type='query')
        payload = {'format': 'Csv'}
        DATA = StringIO(requests.get(endpoint, auth=queryoauth, params=payload).text)
        return pd.read_csv(DATA)

    def fetchJobOutput(self, job_id):
        job_info = self.checkJobState(job_id)
        result_list = []
        output_id_list = [output['id'] for output in job_info['outputs']]
        for output_id in output_id_list:
            output_df = self.getJobOutput(job_id, output_id)
            result_list.append(output_df)
        if (len(result_list) > 1):
            df = pd.concat(result_list)
        else:
            df = result_list[:1]
        return df[:-1]


    def executeWorkflow(self, app_id, question_payload):
        endpoint = self.generateAyxEndpoint('workflows', app_id) + 'jobs/'
        queryoauth = OAuth1(self.client_key, self.client_secret, signature_type='query')
        return requests.post(endpoint, auth=queryoauth, json=question_payload)


    def executeAndFetchResults(self, app_id,
                               question_payload):
        response = self.executeWorkflow(app_id, question_payload)
        job_id = response.json()['id']
        job_state = 'Queued'
        while(job_state == 'Queued'):
            job = self.checkJobState(job_id)
            j_state = job['status']
            print(j_state)
            if (j_state == 'Completed'):
                job_state = j_state
            time.sleep(1)
        return self.fetchJobOutput(job_id)
