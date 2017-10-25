import os
from flask import Flask,request,redirect,url_for,render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/ubuntu/workspace/txtApi'
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_files(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/uploadFile', methods =['GET','POST'])
def uploadFile():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_files(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploadFile',
                                    filename=filename))
    return render_template('upload.html')







app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))