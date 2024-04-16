import requests

# ===== Input : Image =====

# 1. txt 파일 저장할 때
resp = requests.get('http://127.0.0.1:5005/predict?source=https://cdn.pixabay.com/photo/2023/09/12/13/46/ai-generated-8248880_1280.png&save_txt=T',
                    verify=False)
print(resp.content)


# 2. txt 파일을 저장하지 않고 이미지에 레이블만 지정
# resp = requests.get('http://0.0.0.0:5005/predict?source=https://raw.githubusercontent.com/ultralytics/ultralytics/main/ultralytics/assets/zidane.jpg',
#                    verify=False)
# print(resp.content)

# 모니터링 URL / # input 소스 주소
# 'http://127.0.0.1:5005/predict?source=https://raw.githubusercontent.com/ultralytics/ultralytics/main/ultralytics/assets/zidane.jpg'