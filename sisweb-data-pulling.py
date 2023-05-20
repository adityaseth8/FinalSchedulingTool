import requests
import json
import pandas as pd
import csv

# Set the URL of the API endpoint
url = 'https://registrar-apps.ucdavis.edu/courses/search/index.cfm'

# Set the request parameters
params = {
    'action': 'results',
    'termCode': '202330'  # Spring 2023 term code
}

# Send a GET request to the API endpoint
# response = requests.get(url, params=params)
response = requests.request("GET", url, params=params)
response.raise_for_status()
print(response.headers)

# Check if the request was successful
if (
    response.status_code != 204 and
    response.headers[""].strip().startswith("application/json")
):
    try:
        data = response.json()

        print(data) 
    except ValueError:
        print("Error with getting data")
        # decide how to handle a server that's misbehaving to this extent

    

#     # Parse the JSON response
    # data = json.loads(response.text)
    # data = pd.json_normalize(response.json()['data'])
    # print(data)


#     # Convert the data to a DataFrame
#     df = pd.DataFrame(data)

    # Save the DataFrame as a CSV file
#     csv_filename = 'course_data.csv'
#     df.to_csv(csv_filename, index=False)

#     # Print the CSV content
#     with open(csv_filename, 'r') as file:
#         csv_content = file.read()
#         print(csv_content)
# else:
#     print('Error:', response.status_code)
