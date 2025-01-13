import requests
import json
from bs4 import BeautifulSoup
data=[]
for i in range(1,51):
    url= "http://wannahack.iitbhucybersec.in:65338/hostel/D?page=" + str(i)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'user-table'})
    rows = table.find('tbody').find_all('tr')

    for row in rows:
        cells = row.find_all('td')
        name = cells[1].text.strip()
        email = cells[2].text.strip()
        room = int(cells[3].text.strip())
        data.append({
            "hostel": "Hostel D",
            "name": name,
            "email": email,
            "room": room
        })
with open('hostel_d.json', 'w') as f:
    json.dump(data, f, indent=4)