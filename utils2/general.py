# Flask API에서 요청을 받아들여서 옵션을 업데이트하는 함수를 정의
import os
from pathlib import Path
import json

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]
RANK = int(os.getenv('RANK', -1))
    
def update_options(request):
    # GET parameters
    if request.method == 'GET':
        all_args = request.args # TODO:
        source = request.args.get('source')
        save_txt = request.args.get('save_txt')

    # POST parameters
    if request.method == 'POST':
        json_data = request.get_json()
        json_data = json.dumps(json_data)
        dict_data = json.loads(json_data)
        source = dict_data['source']
        save_txt = dict_data.get('save_txt', None)        
    
    return source, bool(save_txt)
