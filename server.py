import os
from flask import Flask,request,redirect,url_for,render_template
from werkzeug.utils import secure_filename
import redis

r = redis.Redis(host="127.0.0.1", port=6379, db=0)


UPLOAD_FOLDER = '/home/ubuntu/workspace/wordInference'
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
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_files(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('countWords',
                                    filename=filename))
            
    return render_template('upload.html')

@app.route("/simple_chart")
def chart():
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('chart.html', values=values, labels=labels, legend=legend)
 

"""AQUI INICIAN LOS MÉTODOS PROPIOS DE LA BASE DE DATOS"""
def fetch_adjetivos():
    listaBuscada = obtenga_redis("adjetivosMin2")
    listaDatos = codifique_utf8(listaBuscada)
    return listaDatos     

def fetch_sustantivos():
    listaBuscada = obtenga_redis("sustantivosMin")
    listaDatos = codifique_utf8(listaBuscada)
    return listaDatos     

def fetch_preposiciones():
    listaBuscada = obtenga_redis("preposiciones")
    listaDatos = codifique_utf8(listaBuscada) 
    return listaDatos    

def fetch_verbos():
    listaBuscada = obtenga_redis("terminacionesVerbos")
    listaDatos = codifique_utf8(listaBuscada)
    return listaDatos

def fetch_pronombres():
    listaBuscada = obtenga_redis("pronombres")
    listaDatos = codifique_utf8(listaBuscada)
    return listaDatos    

def obtenga_redis(listName):
    valuer = (r.lrange(listName,0,-1))
    return valuer

def codifique_utf8(listaBuscada):
    listaDatos = []
    for word in listaBuscada:
        val = word.decode("utf-8").lower()
        listaDatos.append(val)
    return listaDatos  
    
def open_txt():
    sustantivosEncontrados = []
    adjetivosEncontrados = []
    verbosEncontrados = []
    pronombresEncontrados = []
    preposicionesEnccontradas = []
    palabraDesconocida = []
    
    try:
        with open("gran_rebelion.txt",'r') as txt:
            listaSustantivos = fetch_sustantivos()
            listaAdjetivos = fetch_adjetivos()
            listaPronombres = fetch_pronombres()
            listaPreposiciones = fetch_preposiciones()
            listaTerminacionesVerbos = fetch_verbos()
            
            for line in txt:
                for word in line.split():
                    palabraLimpia = clean_word(word)
                    if palabraLimpia in listaSustantivos:
                        sustantivosEncontrados.append(word)
                    elif palabraLimpia in listaAdjetivos:
                        adjetivosEncontrados.append(word)
                    elif palabraLimpia in listaPronombres:
                        pronombresEncontrados.append(word)
                    elif palabraLimpia in listaPreposiciones:
                        preposicionesEnccontradas.append(word)
                    elif palabraLimpia.endswith(tuple(listaTerminacionesVerbos)):
                        verbosEncontrados.append(word)
                    else:
                        palabraDesconocida.append(word)
    except:
        print("Error")
    print(adjetivosEncontrados)

def clean_word(word):
     palabraMinuscula = word.lower()
     palabraSinPunto = palabraMinuscula.replace('.','')
     palabraLimpia = palabraSinPunto.replace(',','')
     return palabraLimpia    

"""
@app.route('/countWords',methods = ['GET','POST'])
def countWords():
    return "Hola"""
    






app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))