import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

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

### Formas No Personales
formasNoPersonales = ['ar','er','ir','or','ur','ndo','ado','ido','to','so','cho','aba']
infinitivos = ['ar','er','ir','or','ur']
gerundios = ['ndo']
participio = ['ado','ido','to','so','cho']

###Pronombres
pronombres = ['yo','tu','tú','vos','usted','el','ella','ello','nosotras','nosotros','vosotras'
            'vosotros','ustedes','ellos','ellas','me','te','se','lo','la','le'
            'se','nos','os','los','las','les','mío','tuyo','suyo','suya','tuya','mía','tuyos',
              'tuyas','mías','suyos']
##Preposiciones
preposiciones = ['a','ante','bajo','cabe','con','contra','de','desde','en','entre','hacia'
                'hasta','para','por','segun','sin','sobre','tras'
                'durante','mediante','excepto','salvo','incluso','más','menos','acerca de'
                'al lado de','antes de','alrededor de','a pesar de','cerca de','con arreglo a',
                'debajo de','delante de','dentro de','después de','detrás de','encima de',
                'en cuanto a','enfrente de','fuera de','frente a','gracias a','junto a',
                'lejos de','por culpa','y']

"""Chequea si tiene alguna terminación de verbo, si lo tiene entonces
se extrae la raiz y se la agregan todas las terminaciones, luego se le meten
en la base de datos.
Si no lo tiene se chequea si es sustantivo o adjetivo"""


for word in test:
    if word.endswith(tuple(formasNoPersonales)):
        palabrasAba.append(word)
    elif word.lower() in pronombres:
        pronombresList.append(word)
    else:
        palabrasNoAba.append(word)


print("Verbos")
print(palabrasAba)
print("Pronombres")
print(pronombresList)
print("Palabras no procesadas")
print(palabrasNoAba)

adjetivosLista = []                            
with open('sustantivos.txt' ,'r') as f:
    adjetivos = [line.strip() for line in f]
    adjetivosLista.append(adjetivos)
    
data = [line.strip() for line in open('sustantivos.txt', 'r')]
texts = [[word.lower() for word in text.split()] for text in data]

    
    
print("LISTA")    
print(adjetivosLista)

print("Redis")
r.set('foo', 'bar')
value = r.get('foo')
print(value)


print("Minuscula")
print(texts)


print("LISTA REDIS")
value = r.lrange('test2',0,-1)

listaUTF = []

for word in value:
    test = word.decode("utf-8")
    listaUTF.append(test)
        
print(listaUTF)
print(r.llen('test2'))

pruebita = []
pruebita2 = []

with open('gran_rebelion.txt','r') as f:
    for line in f:
        for word in line.split():
            if word in preposiciones:
                pruebita.append(word)
            elif word in listaUTF:
                pruebita2.append(word)
                

print("Preposiciones")
print(len(pruebita))
print(pruebita)
print("UTF")
print(len(pruebita2))
print(pruebita2)