# 吉沢亮様の顔認証BOT

## 概要

### QRcode
<img src="https://user-images.githubusercontent.com/38125792/117513103-f9da7e80-afcb-11eb-8304-fd448a078aeb.png" width=20% >

### 目的
- LINE BOTを開発できるようになる
- Flaskで作成した簡易Webアプリをデプロイできるようになる
- Azure Face APIを利用できるようになる
- Azureでデプロイ
- jupyter notebookでインタラクティブにコーディング＆出力確認を体験

### 内容
- LINEからテキストメッセージを取得 => オウム返し
- LINEから画像を取得 => Azure Face API && Flask で処理
- 吉沢亮と顔認証を行い信頼度が0.5以上で真、それ未満で偽をメッセージ送信

### 環境
- MacOS BigSur 11.2.3
- python 3.7
- line-bot-sdk 1.14
- azure-cognitiveservices-vision-face 0.4
