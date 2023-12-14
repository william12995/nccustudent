from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os
import re
from classify import getURL

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

    

# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     message = text=event.message.text
#     if re.match('測試',message):
#         line_bot_api.reply_message(event.reply_token, TextSendMessage(text = getURL("2").to_string()))
#         
#     else:
#         message = TextSendMessage(text=event.message.text)
#         line_bot_api.reply_message(event.reply_token, message)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    message = text=event.message.text
    if re.match("告訴我秘密",message):
        buttons_template_message = TemplateSendMessage(
        alt_text='按鈕選單',
        template=ButtonsTemplate(
            thumbnail_image_url='https://imgur.com/a/X4AWylx',
            title='政大交流版',
            text='選擇貼文類型 :',
            actions=[
                MessageAction(
                    label='問卷',
                    text= '問卷'
                ),
                MessageAction(
                    label='遺失物',
                    text= '遺失物'
                ),
                MessageAction(
                    label='剩食',
                    text= '剩食'
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    elif re.match('問卷',message):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = getURL("1").to_string(index=False)))
    elif re.match('遺失物',message):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = getURL("2").to_string(index=False)))
    elif re.match('剩食',message):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = getURL("3").to_string(index=False)))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)