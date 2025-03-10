import time
import requests
from bs4 import BeautifulSoup
import os

# Ottieni le variabili d'ambiente da Railway
TELEGRAM_BOT_TOKEN = "7616181870:AAEAVHZbP8vMgOam3ZoiTu5Acnq-DBB4FTw"
TELEGRAM_CHAT_ID = "214186478"
URL = "https://www.amazon.it/dp/B0DK93ZQPC/"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=data)

def check_availability():
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    if "Disponibile" in soup.text:  # Modifica questa parte in base al sito
        send_telegram_message(f"🎉 Il prodotto è disponibile! Controlla qui: {URL}")

while True:
    check_availability()
    time.sleep(5)  # Controlla ogni 5 secondi