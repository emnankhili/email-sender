from flask import Flask, request, jsonify
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.get_json()
    receiver = data.get("to")
    subject = data.get("subject")
    message = data.get("message")

    try:
        email = EmailMessage()
        email["From"] = "emnankhili12@gmail.com"
        email["To"] = receiver
        email["Subject"] = subject
        email.set_content(message)

        # Use environment variable for Gmail password (App Password or OAuth2)
        gmail_password = os.getenv("BacMath12")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login("emnankhili12@gmail.com", gmail_password)
            smtp.send_message(email)

        return jsonify({"status": "success"}), 200

    except Exception as e:
        app.logger.error(f"Error: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
