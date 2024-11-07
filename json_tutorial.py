'''
Python API and Pandas Dataframe Tutorial

**Purpose:** To create a quick reference for myself (and others!) to use APIs and incorporate them into Panda Dataframes which we are more familiar with working with in Python.

**From:**
[Dataquest API Tutorial](https://www.dataquest.io/blog/python-api-tutorial/)
[Pandas Dataframe Tutorial Instructions](https://www.geeksforgeeks.org/pandas-convert-json-to-dataframe/)

Code is displayed as written from those pages, except where it generated errors -- for example the GeeksforGeeks link has '\&quot;' instead of """. I have added notes from the page where apropriate, and tried whenever possible to simplify them. 
'''

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import requests #http requests
import json #json handling
import io #for pandas dataframe handling of JSON in string format

'''
Making a Request
'''

#Intentionally query a data source that doesn't exist
response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
print(response.status_code)

'''
API Codes:<br>
- 200: Everything went okay, and the result has been returned (if any).<br>
- 301: The server is redirecting you to a different endpoint.<br>
- 400: The server thinks you made a bad request.<br>
- 401: The server thinks you're not authenticated.<br>
- 403: The resource you're trying to access is forbidden: you don't have the right permissions to see it.<br>
- 404: The resource you tried to access wasn't found on the server.<br>
- 503: The server is not ready to handle the request.
'''

#Query an API that exists
response = requests.get("http://api.open-notify.org/astros")
print(response.status_code)

'''
JSON Responses
'''

#Print the resultant JSON
print(response.json())

# create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

'''

Filter By

Failing to use a filter can return a dataset that is larger than intended

'''

response = requests.get("https://api-server.dataquest.io/economic_data/countries")
print(response.json())

'''

Use of "?filter_by=region=" allows that data to be filtered by that region.

? indicates the beginning of the query string
filter_by indicates the type of filter being applied
region is a specific field in the API we want to use to filter
= us used to assign the filter criteria and then again to set the value we want
%20 is used to indicate a space in a URL, this can be skipped in most programs due to parsing

'''

response = requests.get("https://api-server.dataquest.io/economic_data/countries?filter_by=region=Sub-Saharan%20Africa")
ssa_data = response.json()
print(ssa_data)

'''

Pandas Dataframe from JSON

'''

#Create a dummy set of JSON data
data = {
    "Name": {
        "0": "Harsha",
        "1": "Vardhan",
        "2": "Krishna",
        "3": "Hanuman",
        "4": "Shiva"
    },
    "Roll_no": {
        "0": 1,
        "1": 2,
        "2": 3,
        "3": 4,
        "4": 5
    },
    "subject": {
        "0": "C",
        "1": "JAVA",
        "2": "C++",
        "3": "SWIFT",
        "4": "PYTHON"
    }
}

with open('subject.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

#Reading the JSON File 
dataFrame = pd.read_json("subject.json")
#Printing the data Frame
print(dataFrame)

'''

Now, lets try it with the large JSON dataset from Sub Saharan Africa. We use the df.head() method to limit the dataset to just the top 5 entries, reducing the size of the resultant printout.

'''

#Reading the JSON File 
df = pd.read_json(io.StringIO(ssa_data))
#Printing the data Frame
print(df.head())

'''

Now you can put your data into a CSV file, or do whatever you would like to analyze it using the normal methods -- sns, plotly, etc.

'''

print("End")
