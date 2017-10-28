import os,json
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

###Este método necesita un poco más de trabajo para mostrar txt en servidor.
@app.route('/index')
def hello():
    txtList = []
    json_data = {}
    for file in os.listdir("/home/ubuntu/workspace/wordInference"):
        if file.endswith(".txt"):
            txtList.append(file)
            json_data = json.dumps([dict(name=file) for pn in txtList])
            
    return render_template('index.html',data=[{'name':'gran_rebelion.txt'},{'name':'platillos_voladores.txt'}])


@app.route('/wordCount', methods = ['GET','POST'])     
def wordCount():
    select = request.form.get('comp_select')
    pesos = open_txt(select)

    labels = ["Sustantivos", "Adjetivos", "Verbos", "Pronombres", "Preposiciones", "No procesadas"]
    legend = "Cantidad de palabras"
    values = []
    for valor in pesos:
        values.append(valor)
    return render_template('chart.html', values=values,labels=labels,legend=legend)

###Este método podría redireccionar al index.
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
            return redirect(url_for('uploadFile'))
            
    return render_template('upload.html')
    
 

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
    
def open_txt(libro):
    sustantivosEncontrados = []
    adjetivosEncontrados = []
    verbosEncontrados = []
    pronombresEncontrados = []
    preposicionesEnccontradas = []
    palabraDesconocida = []
    
    try:
        with open(libro,'r') as txt:
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
    pesos = []
    pesos.append(len(sustantivosEncontrados))
    pesos.append(len(adjetivosEncontrados))
    pesos.append(len(verbosEncontrados))
    pesos.append(len(pronombresEncontrados))
    pesos.append(len(preposicionesEnccontradas))
    pesos.append(len(palabraDesconocida))
    
    return pesos

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