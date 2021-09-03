import os
import glob
import urllib.request
from PIL import Image
from compress import *
from flask import Flask, Response, request, jsonify, render_template
app = Flask(__name__)
import json


ALLOWED_EXTENSIONS = set(['jpg'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/')
def home():
    ret = 'hello'
    return ret
sc = []
@app.route('/upload-image', methods=['GET', 'POST'])
def upload_file_api():
    foldername = 'uploaded_images'
    path = os.path.join(os.path.abspath('static'), foldername)
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        files = glob.glob(path + '/*')
        for f in files:
            os.remove(f)
    contents = request.json
    #print(contents)
    for content in contents:
        id = content['id']
        #print(id)
        # check if the post request has the file part
        file = content['image']
        file_name = file.split('/')[-1]
        sp = os.path.join(path, file_name)
        urllib.request.urlretrieve(
            file,
            sp)
        img = img_compress(sp)
        ret = {'url':file,'id':id,'image': img}
        sc.append(ret)
    jsonString = json.dumps(sc,indent=4)
    #print(jsonString)
    return jsonString

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=False)
