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

def generateAyxEndpoint(gallery_url, operation, method):
    req_url = gallery_url + '{operation}/{method}/'.format(operation=operation,
                                                         method=method)
    return req_url

def generateAyxRequest(endpoint, client_key, client_secret):
    queryoauth = OAuth1(client_key, client_secret, signature_type='query')
    return requests.get(endpoint, auth=queryoauth)

def getSubscriptionWorkflows(client_key, client_secret,
                             gallery_url='http://localhost:80/gallery/api/v1/'):
    endpoint = generateAyxEndpoint(gallery_url, 'workflows', 'subscription')
    return generateAyxRequest(endpoint, client_key, client_secret).json()

def getWorkflowQuestions(client_key, client_secret, app_id,
                         gallery_url='http://localhost:80/gallery/api/v1/'):
    endpoint = generateAyxEndpoint(gallery_url, 'workflows', app_id) + 'questions/'
    return generateAyxRequest(endpoint, client_key, client_secret).json()

def getWorkflowJobs(client_key, client_secret, app_id,
                         gallery_url='http://localhost:80/gallery/api/v1/'):
    endpoint = generateAyxEndpoint(gallery_url, 'workflows', app_id) + 'jobs/'
    return generateAyxRequest(endpoint, client_key, client_secret).json()


def checkJobState(client_key, client_secret, job_id,
                         gallery_url='http://localhost:80/gallery/api/v1/'):
    endpoint = generateAyxEndpoint(gallery_url, 'jobs', job_id)
    return generateAyxRequest(endpoint, client_key, client_secret).json()


def getJobOutput(client_key, client_secret, job_id, output_id,
                gallery_url='http://localhost:80/gallery/api/v1/'):
    endpoint = generateAyxEndpoint(gallery_url, 'jobs', job_id)
    endpoint = endpoint + 'output/{output_id}/'.format(output_id=output_id)
    queryoauth = OAuth1(client_key, client_secret, signature_type='query')
    payload = {'format': 'Csv'}
    DATA = StringIO(requests.get(endpoint, auth=queryoauth, params=payload).text)
    return pd.read_csv(DATA)

def fetchJobOutput(client_key, client_secret, job_id, gallery_url='http://localhost:80/gallery/api/v1/'):
    job_info = checkJobState(client_key, client_secret, job_id, gallery_url)
    result_list = []
    output_id_list = [output['id'] for output in job_info['outputs'][:-1]]
    for output_id in output_id_list:
        output_df = getJobOutput(client_key, client_secret, job_id, output_id, gallery_url)
        result_list.append(output_df)
    df = pd.concat(result_list)
    return df[:-1]


def executeWorkflow(client_key, client_secret, app_id, question_payload,
                    gallery_url='http://localhost:80/gallery/api/v1/'):
    endpoint = generateAyxEndpoint(gallery_url, 'workflows', app_id) + 'jobs/'
    queryoauth = OAuth1(client_key, client_secret, signature_type='query')
    return requests.post(endpoint, auth=queryoauth, json=question_payload)


def executeAndFetchResults(client_key, client_secret, app_id,
                           question_payload, gallery_url='http://localhost:80/gallery/api/v1/'):
    response = executeWorkflow(client_key, client_secret, app_id, question_payload, gallery_url)
    job_id = response.json()['id']
    job_state = 'Queued'
    while(job_state == 'Queued'):
        job = checkJobState(client_key, client_secret, job_id)
        j_state = job['status']
        print(j_state)
        if (j_state == 'Completed'):
            job_state = j_state
        time.sleep(1)
    return fetchJobOutput(client_key, client_secret, job_id, gallery_url)
