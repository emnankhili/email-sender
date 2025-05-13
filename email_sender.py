from flask import Flask, request, jsonify
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.get_json()
    receiver = data.get("to")
    subject = data.get("subject")
    message = data.get("message")

    try:
        email = EmailMessage()
        email["From"] = "Gainz@gmail.com"
        email["To"] = receiver
        email["Subject"] = subject
        email.set_content(message)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login("Gainz@gmail.com", "your_app_password")
            smtp.send_message(email)

        return jsonify({"status": "success"}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
