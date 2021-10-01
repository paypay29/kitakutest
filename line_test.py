from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage,
)
import os

app = Flask(__name__)

#herokuの環境変数に設定された、LINE DevelopersのアクセストークンとChannelSecretを
#取得するコード
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

user_id = "Ub58032ed8192de02a6209c8021fa535e"

def sum(a):
    ans = a + 5
    
    return(ans)

#herokuへのデプロイが成功したかどうかを確認するためのコード
@app.route("/")
def hello_world():
    return "hello world"


#LINE DevelopersのWebhookにURLを指定してWebhookからURLにイベントが送られるようにする
@app.route("/callback", methods=['POST'])
def callback():
    # リクエストヘッダーから署名検証のための値を取得
    signature = request.headers['X-Line-Signature']

    # リクエストボディを取得
    body = request.get_data(as_text=True)
    #app.logger.info("Request body: " + body)

    # 署名を検証し、問題なければhandleに定義されている関数を呼ぶ
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


#以下でWebhookから送られてきたイベントをどのように処理するかを記述する
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "グラフ":
        """line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="グラフ送信"))"""
        
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url = r"C:\Users\shoki00\asobi\kitaku\line_test\一時記録.jpg",
                preview_image_url = r"C:\Users\shoki00\asobi\kitaku\line_test\一時記録.jpg"))
        
    elif event.message.text == "グラフ表示":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="グラフ表示"))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="そのようなコマンドはありません。"))
    """a = int(event.message.text)
    ans = sum(a)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text= ans))"""
    


# ポート番号の設定
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
