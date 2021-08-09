import cv2
import requests
# request フォームから送信した情報を扱うためのモジュール
# redirect  ページの移動
# url_for アドレス遷移
from flask import Flask, request, redirect, url_for


UPLOAD_FOLDER = "./uploads"
app = Flask(__name__)

def airport():
    url = "https://www.ana.co.jp/topics/coronavirus-travel-information/images/airport-info/t01_hnd_210805.jpg"
    file_name = "t01_hnd_210805.webp"

    response = requests.get(url)
    image = response.content

    with open(file_name, "wb") as f:
       f.write(image)

    img = cv2.imread(file_name)
    cv2.imwrite("t01_hnd_210805.jpeg", img)

@app.route("/", methods=["GET","POST"])
def uploads_file():
    airport()

if __name__ == '__main__':
    app.debug = True
    app.run()