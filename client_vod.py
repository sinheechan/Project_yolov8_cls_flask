import requests

# ==== Input : video ====

# 브라우저에 동영상 주소를 request.get
resp = requests.get('http://127.0.0.1:5005/predict?source=https://www.youtube.com/watch?v=MNn9qKG2UFI',
                    verify=False)

# 모니터링 URL / # input 소스 주소
#'http://127.0.0.1:5005/predict?source=https://www.youtube.com/watch?v=MNn9qKG2UFI'


# ==== 로컬 파일 보내기 ====

# 지정된 이미지 or 동영상 파일을 서버에 POST하여 프레임 단위로 예측 결과를 받아온다.
url = 'http://127.0.0.1:5005/predict'
file_path = 'C:/Users/gmlck/HeechansVS/YOLOv8API/runs/detect/bus.jpg'

params = {
    'save_txt': 'T'
}

with open(file_path, "rb") as f:
    response = requests.post(url, files={"myfile": f}, data=params, verify=False)

print(response.content)