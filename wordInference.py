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

def obtenga_redis(listName):
    valuer = (r.lrange(listName,0,-1))
    return valuer

def codifique_utf8(listaBuscada):
    listaDatos = []
    for word in listaBuscada:
        val = word.decode("utf-8")
        listaDatos.append(val)
    return listaDatos    
    
print(fetch_verbos())

"""
verbos =[]   
def open_file():
    with open('gran_rebelion.txt', 'r') as inF:
            
        for line in inF:
            for word in line.split():
                if word.endswith(tuple):
                    verbos.append(word)
                
                
    print(verbos)            

"""


"""
with open("gran_rebelion.txt","r") as f:
    for line in f:
        for word in line.split():
            if word in preposiciones:
                pruebita.append(word)
            elif word in listaUTF:
                pruebita2.append(word)

def fill_redis_data():
    #SUSTANTIVOS
    for sustantivo in listaUTF:
        r.lpush("sustantivosMin",sustantivo)
    print(r.lrange("sustantivosMin",0,-1))    
    
    #ADJETIVOS
    
    #PRONOMBRES
    
    #PREPOSICIONES
    
    #TERMINACIONES VERBALES REGULARES NO PERSONALES
fill_redis_data()    """