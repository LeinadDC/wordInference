import redis

r = redis.Redis(host="127.0.0.1", port=6379, db=0)


listaUTF = []
listaUTF2 = []
    

def fetch_sustantivos():
    valuer = (r.lrange("adjetivosMin2",0,-1))
    for word in valuer:
        val = word.decode("utf-8")
        listaUTF.append(val)

def fetch_adjetivos():
    valuer = (r.lrange("preposiciones",0,-1))
    for word in valuer:
        val = word.decode("utf-8")
        listaUTF.append(val)

def fetch_preposiciones():
    valuer = (r.lrange("preposiciones",0,-1))
    for word in valuer:
        val = word.decode("utf-8")
        listaUTF.append(val)    
    return listaUTF    

def fetch_verbos():
    valuer = (r.lrange("terminacionesVerbos",0,-1))
    for word in valuer:
        val = word.decode("utf-8")
        listaUTF.append(val)

print(listaUTF) 

verbos =[]   
def open_file():
    with open('gran_rebelion.txt', 'r') as inF:
        for line in inF:
            for word in line.split():
                if word.endswith(tuple(listaUTF)):
                    verbos.append(word)
                
                
    print(verbos)            




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