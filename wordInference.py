import redis

r = redis.Redis(host="127.0.0.1", port=6379, db=0)


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
        val = word.decode("utf-8")
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
                    if word in listaSustantivos:
                        sustantivosEncontrados.append(word)
                    elif word in listaAdjetivos:
                        adjetivosEncontrados.append(word)
                    elif word in listaPronombres:
                        pronombresEncontrados.append(word)
                    elif word in listaPreposiciones:
                        preposicionesEnccontradas.append(word)
                    elif word.endswith(tuple(listaTerminacionesVerbos)):
                        verbosEncontrados.append(word)
                    else:
                        palabraDesconocida.append(word)
    except:
        print("Error")
    print(preposicionesEnccontradas)    
                            
open_txt()
