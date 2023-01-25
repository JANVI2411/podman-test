from flask import Flask
# from celery import Celery
from gevent.pywsgi import WSGIServer
import webbrowser

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

# celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
# celery.conf.update(app.config)

@app.route("/")
def hello():
    # task = my_background_task.apply_async(args=[10, 20])
    task = ""
    return "hello"

# @celery.task
# def my_background_task(arg1, arg2):
#     result=arg1+arg2
#     return result


ip = '0.0.0.0'
port = 5001
app.debug = True
http_server = WSGIServer((ip, port), app)#, keyfile='key.pem', certfile='cert.pem')
webbrowser.open_new(f'http://localhost:{port}')
http_server.serve_forever()

# from gevent.pywsgi import WSGIServer
# import webbrowser
# import os
# import cv2
# from flask import Flask,redirect,Response,render_template

# app = Flask(__name__, static_url_path='')

# def live_feed():
#     rtsp = "rtsp://admin:cpplus123@183.82.250.57:554/cam/realmonitor?channel=1&subtype=0"
#     vcap = cv2.VideoCapture(rtsp)
#     # h=vcap.get()
#     # w=vcap.get()
#     skip_rate = 2
#     c=0
#     while True:
#         try:
#             ret,frame = vcap.read()
#             if c%2==0:
#                 c=1
#                 continue
#             c=0
#             encoded = cv2.imencode('.png', frame)[1]
#             yield (b'--frame\r\n'
#                     b'Content-Type: image/png\r\n\r\n' + bytearray(encoded) + b'\r\n')
#         except Exception as e:
#             print("Live error:",e)

# @app.route("/live")
# def live_video_feed():
#     return Response(live_feed(),
#                     mimetype="multipart/x-mixed-replace; boundary=frame")

# @app.route('/')
# def home():
#     return render_template('stream.html') 


# ip = '0.0.0.0'
# port = 5001
# app.debug = True
# http_server = WSGIServer((ip, port), app)#, keyfile='key.pem', certfile='cert.pem')
# webbrowser.open_new(f'http://localhost:{port}')
# http_server.serve_forever()
