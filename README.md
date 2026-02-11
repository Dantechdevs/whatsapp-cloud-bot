# WhatsApp Cloud API Bot

A Python Flask bot connected to **WhatsApp Cloud API** to send and receive WhatsApp messages automatically.  
This project is built for **Dantech Developers** and uses Meta's official WhatsApp API.

---

## Features

- Auto-reply to incoming WhatsApp messages
- Webhook verification with Meta
- Simple Flask backend
- Easy to deploy on local machine or cloud
- NGROK support for testing webhooks
- Environment variable management with `.env`

---

## Requirements

- Python 3.9+
- Flask
- Requests
- python-dotenv
- Ngrok (for local testing)
- Meta Developer account with WhatsApp product

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/Dantechdevs/whatsapp-cloud-bot.git
cd whatsapp-cloud-bot
Create virtual environment

bash
Copy code
python -m venv venv
Activate environment

Windows CMD:

cmd
Copy code
venv\Scripts\activate
Git Bash / Linux:

bash
Copy code
source venv/Scripts/activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
Set environment variables

Create a .env file based on .env.example:

ini
Copy code
VERIFY_TOKEN=your_verify_token
ACCESS_TOKEN=your_meta_access_token
PHONE_NUMBER_ID=your_phone_number_id
Usage
Run Flask app

bash
Copy code
python app.py
Run ngrok (for testing on local machine)

bash
Copy code
./ngrok.exe http 5000
Set webhook URL on Meta Dashboard

arduino
Copy code
https://YOUR_NGROK_URL/webhook
Subscribe to events: messages

Test on WhatsApp

Send message to the connected WhatsApp number

Bot will auto-reply

Project Structure
bash
Copy code
whatsapp-cloud-bot/
│── app.py                # Main Flask bot
│── .env                  # Environment variables (not tracked)
│── .env.example          # Sample environment variables
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation
│── .gitignore            # Ignore venv, logs, and ngrok
Git Commit Guidelines
Initial commit → Initial Flask setup

Install dependencies → Added Flask, Requests, dotenv

Webhook setup → Add webhook verification & auto-reply

Ignore ngrok.exe → Remove binary from repository

License
MIT License © 2026 Dantech Developers

yaml
Copy code
