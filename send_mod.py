# API 요청 시 필요한 정보를 생성 및 변환

import datetime, time
import base64

def channel_id():
    return str(5) # 여러분의 번호

def server_id():
    return str(1) # 고정

def req_id():
    return str(0) # 고정

def req_time():
    d = datetime.datetime.now()
    date = d.strftime('%Y-%m-%d')
    time = d.strftime('%X.f')
    t = date + 'T' + time + 'Z'
    return t

# req_image() 함수는 이미지 파일을 base64 형식으로 인코딩하여 API 요청에 포함될 이미지 데이터를 생성
def req_image(recv_img):
    img = open(recv_img, 'rb')
    base64_str = base64.b64encode(img.read())
    return str(base64_str)[2:-1]
