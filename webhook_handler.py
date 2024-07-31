from flask import Flask, request, jsonify
import telegram
app = Flask(__name__)

TELEGRAM_BOT_TOKEN = ''



bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    
    TELEGRAM_CHAT_ID = data.get('id')
    if TELEGRAM_CHAT_ID:
        message = f"Hello how Are You?: {TELEGRAM_CHAT_ID}"
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        return jsonify({"status": "success", "message": "Message sent to Telegram"}), 200
    else:
        return jsonify({"status": "error", "message": "ID not found in the data"}), 400

if __name__ == '__main__':
    app.run(port=5000)
