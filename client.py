import requests

# 1. ===== Input : Image =====

'''
# txt 파일 저장할 때
resp = requests.get('http://0.0.0.0:5000/predict?source=https://raw.githubusercontent.com/ultralytics/ultralytics/main/ultralytics/assets/zidane.jpg&save_txt=T',
                    verify=False)
print(resp.content)

# txt 파일을 저장하지 않고 이미지에 레이블만 지정
resp = requests.get('http://0.0.0.0:5005/predict?source=https://raw.githubusercontent.com/ultralytics/ultralytics/main/ultralytics/assets/zidane.jpg',
                    verify=False)
print(resp.content)

# 브라우저에서 다음 URL을 복사하여 붙여넣을 수도 있습니다
# 'http://0.0.0.0:5005/predict?source=https://raw.githubusercontent.com/ultralytics/ultralytics/main/ultralytics/assets/zidane.jpg' # input 소스 주소
'''

# 2. ==== Input : video ====

# 브라우저에 동영상 주소를 request.get
resp = requests.get('http://127.0.0.1:5005/predict?source=https://www.youtube.com/watch?v=MNn9qKG2UFI',
                    verify=False)

# 이미지 사례와 같이 브라우저에서 다음 URL을 복사하여 붙여넣을 수도 있습니다
#'http://127.0.0.1:5005/predict?source=https://www.youtube.com/watch?v=MNn9qKG2UFI'


# ==== 로컬 파일 보내기 ==== #

# 지정된 이미지 or 동영상 파일을 서버에 POST하여 예측 결과를 받아온다.

url = 'http://127.0.0.1:5005/predict'
file_path = 'data/images/bus.jpg'

params = {
    'save_txt': 'T'
}

with open(file_path, "rb") as f:
    response = requests.post(url, files={"myfile": f}, data=params, verify=False)

print(response.content)