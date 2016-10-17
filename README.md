# PyRyx

## Python + Alteryx

PyRyx is a Python client helper for working with the Alteryx Gallery API.

It includes functions which allow a user to easily use Alteryx Applications as
data processing APIs, piping in data and retrieving the results.

## Usage

    from PyRyx import pyryx

    client_key = 'your_gallery_client_key_here'
    client_secret = 'your_gallery_client_secret_here'
    #Below url is for a local server installation
    gallery_url = 'http://localhost:80/gallery/api/v1/'

    workflows = pyryx.getSubscriptionWorkflows(client_key, client_secret, gallery_url)
    workflow_id = workflows[0]['id']

    questions_list = pyryx.getWorkflowQuestions(client_key, client_secret, workflow_id, gallery_url)

    question_param = {'questions': [{'name': 'Select Region', 'value': 'East'},
                      {'name': 'Orders on or after', 'value': '2016-07-10'}]}
    #executeAndFetchResults will send data to and execute an Alteryx workflow,
    #with the results being returned as a Pandas DataFrame.  
      
    workflow_output_data = pyryx.executeAndFetchResults(client_key, client_secret, workflow_id,
                             question_param, gallery_url)
