import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://registrar-apps.ucdavis.edu/rooms/sum.cfm?room_type=General"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find('table')
rows = table.find_all('tr')

data = []
for row in rows:
    tds = row.find_all('td')
    if len(tds) >= 2:
        data.append([tds[0].text.strip(), tds[1].text.strip()])

rooms = pd.DataFrame(data[1:], columns=data[0])
rooms['Capacity'] = pd.to_numeric(rooms['Capacity'])  
rooms = rooms.sort_values('Capacity', ascending=False)
print(rooms)