oracion = """El resto della concluían sayo de velarte, calzas de
velludo para las fiestas, con sus pantuflos de lo mesmo, y los días de
entresemana se honraba con su vellorí de lo más fino. Tenía en su casa una
ama que pasaba de los cuarenta, y una sobrina que no llegaba a los veinte,
y un mozo de campo y plaza, que así ensillaba el rocín como tomaba la
podadera. Frisaba la edad de nuestro hidalgo con los cincuenta años; era de
complexión recia, seco de carnes, enjuto de rostro, gran madrugador y amigo
de la caza. Cazar estaba ido en el mar, cuando de pronto me encontré nadando"""


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
pronombres = ['yo','tu','vos','usted','el','ella','ello','nosotras','nosotros','vosotras'
            'vosotros','ustedes','ellos','ellas','me','te','se','lo','la','le'
            'se','nos','os','los','las','les']


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
print("Otros")
print(palabrasNoAba)

