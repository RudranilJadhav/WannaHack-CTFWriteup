import requests
from bs4 import BeautifulSoup
import json
def scrape_hostel_a():
    data=[]
    for i in range(1,51):
        url = "http://wannahack.iitbhucybersec.in:65338/hostel/A?page=" + str(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'class': 'user-table'})  # Update with actual ID or class
        for row in table.find_all('tr')[1:]:  # Skip the header row
            cells = row.find_all('td')
            data.append({
                "hostel": "Hostel A",
                "name": cells[0].text.strip(),
                "email": cells[1].text.strip(),
                "room": int(cells[2].text.strip())
            })
    return data
data = scrape_hostel_a()
def export_to_json(data, filename='output.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
export_to_json(data, 'hostel_a.json')