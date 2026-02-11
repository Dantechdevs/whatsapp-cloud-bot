from flask import Flask, request
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")


@app.route("/", methods=["GET"])
def home():
    return "WhatsApp Bot Running Successfully 🚀"


@app.route("/webhook", methods=["GET"])
def verify_webhook():
    """
    This endpoint is used by Meta to verify your webhook.
    """
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("Webhook verified successfully!")
        return challenge, 200

    return "Verification failed", 403


@app.route("/webhook", methods=["POST"])
def receive_message():
    """
    This endpoint receives incoming WhatsApp messages.
    """
    data = request.get_json()
    print("Incoming Data:", data)

    try:
        message = data["entry"][0]["changes"][0]["value"]["messages"][0]
        sender = message["from"]
        text = message["text"]["body"]

        print(f"Message from {sender}: {text}")

        # Reply automatically
        send_message(sender, f"Hello 👋 You said: {text}")

    except Exception as e:
        print("Error:", e)

    return "EVENT_RECEIVED", 200


def send_message(to, message_text):
    """
    Send message back to WhatsApp user.
    """
    url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "text": {"body": message_text}
    }

    response = requests.post(url, headers=headers, json=payload)

    print("Send Message Response:", response.status_code, response.text)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
