import cv2
import datetime
import time
import json
import base64
import tkinter as tk
#ーーーー顔認識ーーーーー

face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while True:
#   ファイルの名前
  fileName = "photo_" + datetime.datetime.today().strftime('%Y%m%d_%H%M%S') + ".png"
#   画像の読み込み
  ret, img = cap.read()
#   顔認識
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
  for x, y, w, h in faces:
    # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2).T
    # face = img[y: y + h, x: x + w]
    face_gray = gray[y: y + h, x: x + w]
    def send_image(img):
    # ーー　画像を送信可能な形式に変換してJSONに格納　―ー
      _, encimg = cv2.imencode(".png", img)
      img_str = encimg.tostring()
    #  ーー base64形式にする　ーー
      img_byte = base64.b64encode(img_str).decode("utf-8")
    #  ーー json形式にする ーー
      img_json = json.dumps({'image': img_byte}).encode('utf-8')
      print(img_json)
    #  ーーpng形式での保存ーー
    cv2.putText(img, 'face detect', (20,50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,200), 2, cv2.LINE_AA, cv2.imwrite(fileName, img))
    # time.sleep(3)
    # ーーコメント表示ーー
    root = tk.Tk()
    # サイズ
    root.geometry('500x300')
    # 終了する
    root.after(1000, lambda: root.destroy()) 
    # 表示するもの
    label = tk.Label(root, text="ようこそ　〇〇", font=("",20), bg="#aafaff")  
    label.pack()
    root.mainloop()
    # ーーーーーーーーーーーー
  cv2.imshow('video image', img)
  # if faces :
  #   cv2.imwrite(fileName, img)

  key = cv2.waitKey(10)
  if key == 27:
    break
cap.release()
cv2.destroyAllWindows()