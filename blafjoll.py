#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import requests
import json
from bs4 import BeautifulSoup

# Load environment variables
OLD_TEXT_FILE = 'old.txt'
NOTIFIER = os.environ.get('NOTIFIER')
SKIDASVAEDI = os.environ.get('SKIDASVAEDI')
API_KEY = os.environ.get('API_KEY')

# Define the notification parameters
notification_title = 'Eru Bláfjöll Opin'

def get_old_text():
    try:
        with open(OLD_TEXT_FILE, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return ""

def save_new_text(new_text):
    with open(OLD_TEXT_FILE, 'w') as file:
        file.write(new_text)

def check_content_and_notify():
    # Fetch the current content from the website
    response = requests.get(SKIDASVAEDI)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        current_text = soup.select_one("#blafjoll-open-text h1").text.strip()

        # Compare the fetched content with the OLD_TEXT
        old_text = get_old_text()
        if current_text != old_text:
            # If different, send a notification
            data = {
                "ApiKey": API_KEY,
                "PushTitle": notification_title,
                "PushText": current_text,
            }
            headers = {'Content-Type': 'application/json'}
            r = requests.post(NOTIFIER, data=json.dumps(data), headers=headers)

            if r.status_code == 200:
                print('Notification sent!')
                save_new_text(current_text)
            else:
                print('Error while sending notification!')
        else:
            print('No change detected.')
    else:
        print(f'Failed to fetch content from {SKIDASVAEDI}. Status code: {response.status_code}')

if __name__ == "__main__":
    check_content_and_notify()

