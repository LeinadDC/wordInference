import redis

r = redis.Redis(host="127.0.0.1", port=6379, db=0)

oracion = """El resto della concluían sayo de velarte, calzas de
velludo para las fiestas, con sus pantuflos de lo mesmo, y los días de
entresemana se honraba con su vellorí de lo más fino. Tenía en su casa una
ama que pasaba de los cuarenta, y una sobrina que no llegaba a los veinte,
y un mozo de campo y plaza, que así ensillaba el rocín como tomaba la
podadera. Frisaba la edad de nuestro hidalgo con los cincuenta años; era de
complexión recia, seco de carnes, enjuto de rostro, gran madrugador y amigo
de la caza. Luego de esto, el hombre se fue a
cazar estaba ido en el mar, cuando de pronto se encontró nadando en el agua"""


test = oracion.split(" ")
palabrasAba = []
palabrasNoAba = []
pronombresList = []



"""
for word in test:
    if word.endswith(tuple(formasNoPersonales)):
        palabrasAba.append(word)
    elif word.lower() in pronombres:
        pronombresList.append(word)
    else:
        palabrasNoAba.append(word)
"""

print("Verbos")
print(palabrasAba)
print("Pronombres")
print(pronombresList)
print("Palabras no procesadas")
print(palabrasNoAba)


listaUTF = []
listaUTF2 = []
    

valuer = (r.lrange("adjetivosMin2",0,-1))

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