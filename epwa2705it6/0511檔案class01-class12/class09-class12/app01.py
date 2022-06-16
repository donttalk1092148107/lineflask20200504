from flask import *
import os
from werkzeug.utils import secure_filename
import firebase_admin
from firebase_admin import credentials, firestore, storage 
app = Flask(__name__)
#cred=credentials.Certificate('放憑證檔案')
cred=credentials.Certificate('pcschoolline.json')
#firebase_admin.initialize_app(cred, {'storageBucket': 'storage位置'})
firebase_admin.initialize_app(cred, {'storageBucket': 'pcschoolline.appspot.com'})
#app01 = firebase_admin.initialize_app(cred, {'storageBucket': 'storage位置',}, name='storage') 
app01 = firebase_admin.initialize_app(cred, {'storageBucket': 'pcschoolline.appspot.com',}, name='storage') 
app.config['UPLOAD_FOLDER'] = './static/'

@app.route("/")
def index():    
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['photo']
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        bucket = storage.bucket(app=app01)
        blob = bucket.blob(filename)
        blob.upload_from_filename(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        return render_template('upload.html')
        
    else:
        return render_template('upload.html')



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)    
    


