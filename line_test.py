import requests
from flask import Flask, request, abort
from linebot import LineBotApi
from linebot.models import TextSendMessage


app = Flask(__name__)

ACCESS_TOKEN = "cZbI01NiyLImwW + 8DoeOyoSixx5cnNMLf4H8Apyt1aNC2dzT5tPnSyiNcrtQrxJBQG1qWDpHFDXNnTJUdA6KVBq56Ij6bp3JGwlBxaFitSAAY2oZgRCvJ9"
SECRET = "8e578bcd83d870c8400b10976b6cb327"

line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(SECRET)

#herokuへのデプロイが成功したかどうかを確認するためのコード
@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/callback", methods=["POST"])
def callback():
　signature = request.headers["X-Line-Signature"] 　body = request.get_data(as_text=True)
　app.logger.info("Request body: " + body)

　try:
　　handler.handle(body, signature)
　except InvalidSignatureError:
　　abort(400)

　return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
　line_bot_api.reply_message(
　　event.reply_token,
　　TextSendMessage(text=event.message.text))

if __name__ == "__main__":
　app.run()
