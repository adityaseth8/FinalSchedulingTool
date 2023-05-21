import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://registrar-apps.ucdavis.edu/rooms/sum.cfm?room_type=General"

# Send HTML Get Request
response = requests.get(url)

# Parse HTML content 
soup = BeautifulSoup(response.text, "html.parser")

# find the first table element, and all table row elements within that table
table = soup.find('table')
rows = table.find_all('tr')

data = []
for row in rows:
    # find all table data cell elements within that row, extract the first 2 td elements
    tds = row.find_all('td')
    if len(tds) >= 2:
        # append first 2 td elements to list
        data.append([tds[0].text.strip(), tds[1].text.strip()])

# create pandas dataframe to store data from 2nd row onwards using extracted data
# 1st row used for column names
rooms = pd.DataFrame(data[1:], columns=data[0])
# Convert 2nd column to type integer from string
rooms['Capacity'] = pd.to_numeric(rooms['Capacity'])  
# sort dataframe in descending order by room capacity
rooms = rooms.sort_values('Capacity', ascending=False)
print(rooms)

# HTML format

# <div class="_user_table">
#    <table style="WIDTH:85%;">
#       <tbody> 
#          <tr> 
#              <td> 204 Art</td>
#              <td> 174 </td>
#              <td> hhdhd</td>
#              <td> hhdhfdf </td>
#          </tr>