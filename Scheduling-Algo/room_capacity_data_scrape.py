import requests
from bs4 import BeautifulSoup
import pandas as pd

# Database url
url = "https://registrar-apps.ucdavis.edu/rooms/sum.cfm?room_type=General"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Assign table and rows 
table = soup.find('table')
rows = table.find_all('tr')

data = []
# Iterate through rows of the table
for row in rows:
    tds = row.find_all('td')
    if len(tds) >= 2:
        # Get classroom list and capacity
        data.append([tds[0].text.strip(), tds[1].text.strip()])

# Create data frame from web scraping
rooms = pd.DataFrame(data[1:], columns=data[0])
rooms['Capacity'] = pd.to_numeric(rooms['Capacity'])  

# Sort data frame by capacity from greatest to least
rooms = rooms.sort_values('Capacity', ascending=False)

# Export data frame to csv
rooms.to_csv('data.csv')