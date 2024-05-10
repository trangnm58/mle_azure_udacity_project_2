import urllib.request
import json
import pandas as pd
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data = [
    {
        "age": 17,
    "campaign": 1,
    "cons.conf.idx": -46.2,
    "cons.price.idx": 92.893,
    "contact": "cellular",
    "day_of_week": "mon",
    "default": "no",
    "duration": 971,
    "education": "university.degree",
    "emp.var.rate": -1.8,
    "euribor3m": 1.299,
    "housing": "yes",
    "job": "blue-collar",
    "loan": "yes",
    "marital": "married",
    "month": "may",
    "nr.employed": 5099.1,
    "pdays": 999,
    "poutcome": "failure",
    "previous": 1
  },
    {
        "age": 87,
    "campaign": 1,
    "cons.conf.idx": -46.2,
    "cons.price.idx": 92.893,
    "contact": "cellular",
    "day_of_week": "mon",
    "default": "no",
    "duration": 471,
    "education": "university.degree",
    "emp.var.rate": -1.8,
    "euribor3m": 1.299,
    "housing": "yes",
    "job": "blue-collar",
    "loan": "yes",
    "marital": "married",
    "month": "may",
    "nr.employed": 5099.1,
    "pdays": 999,
    "poutcome": "failure",
    "previous": 1
  }
]

df = pd.DataFrame(data)

# Convert the DataFrame to the desired format
converted_data = {
    "input_data": {
    "data": df.values.tolist(),
    "columns": list(df.columns),
    "index": df.index.tolist()
}}

body = str.encode(json.dumps(converted_data))

url = 'https://baseline.southcentralus.inference.ml.azure.com/score'
# Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
api_key = 'tlgMuD2c5EBi8bTaKg2CzHvp9SPl9STq'
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")

# The azureml-model-deployment header will force the request to go to a specific deployment.
# Remove this header to have the request observe the endpoint traffic rules
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'baseline-v1' }

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))
