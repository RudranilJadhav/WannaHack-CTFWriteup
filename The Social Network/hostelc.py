import json
new =[]
with open('hostel_cold.json') as f:
    data = json.load(f)
    for record in data:
        name = record['username']
        email = record['mail']
        room = int(record['room'])
        new.append({
            "hostel": "Hostel C",
            "name": name,
            "email": email,
            "room": room
        })
with open('hostel_c.json', 'w') as f:
    json.dump(new, f, indent=4)