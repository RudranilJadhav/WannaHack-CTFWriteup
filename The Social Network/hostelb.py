import requests
from bs4 import BeautifulSoup
import json
def scrape_hostel_b():
    data=[]
    for i in range(1,51):
        url = "http://wannahack.iitbhucybersec.in:65338/hostel/B?page=" + str(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        cards = soup.find_all('div', {'class': 'card'})
        for card in cards:
            name = card.find('h2', class_='data1').text.strip()
            email = card.find('p', class_='data2').text.strip()
            room = int(card.find('p', class_='room').text.strip())
            data.append({
                "hostel": "Hostel B",  
                "name": name,
                "email": email,
                "room": room
            })
    return data
data = scrape_hostel_b()
def export_to_json(data, filename='output.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
export_to_json(data, 'hostel_b.json')