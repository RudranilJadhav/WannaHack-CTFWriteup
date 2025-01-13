from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import json

def scrape_infinite_scroll(url):
    # Initialize WebDriver
    driver = webdriver.Chrome()  # Ensure you have ChromeDriver installed
    driver.get(url)
    driver.maximize_window()

    # Allow time for the page to load
    time.sleep(3)

    # Scroll and load all data
    last_height = driver.execute_script("return document.body.scrollHeight")
    data = []

    while True:
        # Scroll to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)  # Wait for new content to load

        # Extract data from the loaded cards
        cards = driver.find_elements(By.CLASS_NAME, 'user-card')  # Update selector if necessary
        for card in cards:
            name = card.find_element(By.TAG_NAME, 'h3').text.strip()
            email = card.find_elements(By.TAG_NAME, 'p')[0].text.strip()
            room_text = card.find_elements(By.TAG_NAME, 'p')[1].text.strip()
            room = int(room_text.replace("Room", "").strip())

            record = {
                "hostel": "Hostel E",  # Add hostel name
                "name": name,
                "email": email,
                "room": room
            }
            if record not in data:  # Avoid duplicates
                data.append(record)

        # Check if we've reached the end
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break  # No more content to load
        last_height = new_height

    driver.quit()
    return data

# Example usage
url = "http://wannahack.iitbhucybersec.in:65338/hostel/E"  # Replace with the actual URL
data = scrape_infinite_scroll(url)
with open('hostel_e.json', 'w') as f:
    json.dump(data, f, indent=4)