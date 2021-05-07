import os
from flask import Flask, request, abort

from linebot import (
  LineBotApi, WebhookHandler
)
from linebot.exceptions import (
  InvalidSignatureError
)
from linebot.models import (
  MessageEvent, TextMessage, TextSendMessage, ImageMessage
)
from io import BytesIO
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

app = Flask(__name__)

YOUR_CHANNEL_ACCESS_TOKEN = os.getenv('YOUR_CHANNEL_ACCESS_TOKEN')
YOUR_CHANNEL_SECRET = os.getenv('YOUR_CHANNEL_SECRET')
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

YOUR_FACE_API_KEY = os.environ['YOUR_FACE_API_KEY']
YOUR_FACE_API_ENDPOINT = os.environ['YOUR_FACE_API_ENDPOINT']
face_client = FaceClient(
	YOUR_FACE_API_ENDPOINT,
	CognitiveServicesCredentials(YOUR_FACE_API_KEY)
)

PERSON_GROUP_ID = os.getenv('PERSON_GROUP_ID')
PERSON_ID_AUDREY = os.getenv('PERSON_ID_AUDREY')

@app.route("/callback", methods=['POST'])
def callback():
	# get X-Line-Signature header value
	signature = request.headers['X-Line-Signature']

	# get request body as text
	body = request.get_data(as_text=True)
	app.logger.info("Request body: " + body)

	# handle webhook body
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		print("Invalid signature. Please check your channel access token/channel secret.")
		abort(400)
	return 'OK'

# textへの返信
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	line_bot_api.reply_message(
		event.reply_token,
		TextSendMessage(text=event.message.text))

# 画像への返信
@handler.add(MessageEvent, message=ImageMessage)
def handle_image(event):
  if detected_faces != []:
		# 検出された顔の最初のIDを取得
		text = detected_faces[0].face_id
	else:
		# 検出されない場合のメッセージ
		text = "no faces detected"
	# LINEチャネルを通じてメッセージを返答
	line_bot_api.reply_message(
		event.reply_token,       
		TextSendMessage(text=text)
	)

if __name__ == "__main__":
	app.run()
