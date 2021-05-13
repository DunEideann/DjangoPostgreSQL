from django.shortcuts import render
from autenthi.views import lessons
from django.contrib import messages

# Create your views here.
#region information
info = {
    'ger_nouns': {
        '1': [
            ['País', 'Das Land'], ['Región', 'Die Region'],
            ['Provincia', 'Die Provinz'], ['Ciudad', 'Die Stadt'],
            ['Pueblo', 'Das Dorf'], ['Calle', 'Die Strasse'],
            ['Plaza', 'Der Platz'], ['Avenida', 'Die Allee'],
            ['Monumento', 'Das Denkmal'], ['Fuente', 'Die Quelle'],
            ['Aeropuerto', 'Der Flughafen'], ['Estación', 'Der Bahnhof'],
            ['Puerto', 'Der Hafen'], ['Metro', 'Die U-Bahn'],
            ['Parque', 'Der Park'], ['Aparcamiento', 'Der Parkplatz'],
            ['Hospital', 'Das Krankenhaus'], ['Panaderia', 'Die Bäckerei'],
            ['Cine', 'Das Kino'], ['Teatro', 'Das Theater'],
            ['Restaurante', 'Das Restaurant'], ['Tienda', 'Das Geschäft']
        ],
        '2': [
            ['Casa', 'Das Haus'], ['Puerta', 'Die Tür'],
            ['Ventana', 'Das Fenster'], ['Pared', 'Die Wand'],
            ['Suelo', 'Der Boden'], ['Techo', 'Die Zimmerdecke'],
            ['Tejado', 'Das Dach'], ['Chimenea', 'Der Schornstein'],
            ['Balcón', 'Der Balkon'], ['Pasillo', 'Der Flur']
            
        ],
        '3': [
            ['Salón', 'Das Wohnzimmer'], ['Comedor', 'Das Esszimmer'],
            ['Dormitorio', 'Das Schlafzimmer'], ['Baño', 'Das Badezimmer'],
            ['Despacho', 'Das Arbeitszimmer'], ['Escalera', 'Die Treppe'],
            ['Garaje', 'Die Garage'], ['Cocina', 'Die Küche'],
            ['Jardín', 'Der Garten'], ['Patio', 'Der Hinterhof']
        ],
        '4': [
            ['Padre', 'Der Vater'], ['Madre', 'Die Mutter'],
            ['Hermano', 'Der Bruder'], ['Hermana', 'Die Schwester'],
            ['Hijo', 'Der Sohn'], ['Hija', 'Die Tochter'],
            ['Hijos', 'Die Kinder'], ['Padres', 'Die Eltern'],
            ['Hermanos', ''], ['Familia', 'Die Familie'],
            ['Primo/a', 'Der Cousin'], ['Nieto', 'Der Enkel'],
            ['Nieta', 'Die Enkelin'], ['Abuelo', 'Der Großvater'],
            ['Abuela', 'Die Großmutter'], ['Familiares', 'Die Vertrauten']
        ],
        '5': [
            ['Perro', 'Der Hund'], ['Gato', 'Die Katze'],
            ['Caballo', 'Das Pferd'], ['Cerdo', 'Das Schwein'],
            ['Raton', 'Die Maus'], ['Abeja', 'Die Biene'],
            ['Pescado', 'Dr Disch'], ['Pajaro', 'Der Vogel'],
            ['Animal', 'Das Tier'], ['Mascota', 'Das Haustier']
        ],
        '6': [
            ['Vehiculo', 'Das Fahrzeug'], ['Cosa', 'Zeug'],
            ['Encendedor', 'Feuerzeug'], ['Juguete', 'Das Spielzeug'],
            ['Tejido', 'Das Strickzeug'], ['Herramienta', 'Das Wekzeug'],
            ['Tambores', 'Das Schlagzeug'], ['Utensilios de escritura', 'Das Schreibzeug'],
            ['Traje de Baño', 'Das Badezeug'], ['La cosa verde', 'Das Grünzeug']
        ],
        '7': [
            ['Pan', 'Das Brot'], ['Pizza', 'Die Pizza'],
            ['Azucar', 'Der Zucker'], ['Sal', 'Das Salz'],
            ['Carne', 'Das Fleisch'], ['Hamburguesa', 'Der hamburger'],
            ['Tomate', 'Die Tomate'], ['Patata', 'Die Kartoffel'],
            ['Lechuga', 'Der Salat'], ['Fideos', 'Die Nudeln'],
            ['Arroz', 'Der Reis'], ['Agua', 'Das Wasser'],
            ['Jugo', 'Der Saft'], ['Jugo de Manzana', 'Der Apfelsaft'],
            ['Cerveza', 'Das Bier'], ['Vino', 'Der Wein'],
            ['Té', 'Der Tee'], ['Café', 'Der Kaffee']
        ],
        '8': [
            ['Vehículo', 'Das Fahrzeug'], ['Avión', 'Das Flugzeug'],
            ['Auto', 'Das Auto'], ['Camión', 'Der Lastwagen'],
            ['Camioneta', 'Der Truck'], ['Bus', 'Der Bus'],
            ['Trén', 'Der Zug'], ['Barco', 'Das Schiff'],
            ['Bicicleta', 'Das Fahrrad'], ['Motocicleta', 'Das Motorrad'],
            ['Scooter', 'Der Roller'], ['Moto', 'Das Moto'],
            ['Metro', 'Der U-Bahn'], ['Taxi', 'Das Taxi']
        ]
    },
    'ger_verbs': {
        '1': [
            ['Teclar', 'Schlüssel'], ['Saludar', 'Grüßen'],
            ['Programar', 'Programm'], ['Trabajar', 'Arbeiten']
        ],
        '2': [
            ['Comer', 'Essen'], ['Cocinar', 'Kochen'],
            ['Limpiar', 'Aufräumen'], ['Cortar', 'Schneiden'],
            ['Poner', 'Einstellen'], ['Agarrar', 'Greifen'],
            ['Soltar', 'Veröffentlichung'], ['Traer', 'Bringen'],
            ['Calentar', 'Wärmen'], ['Cocer', 'Aufkochen']
        ],
        '3': [
            ['Subir', 'Steig'], ['Bajar', 'Raus'],
            ['Viajar', 'Reisen'], ['Esperar', 'Warten'],
            ['Caminar/Ir', 'Gehen'], ['Correr', 'Laufen'],
            ['Conducir', 'Führen'], ['Moverse', 'Bewegung']
        ],
        '4': [
            ['Comprar', 'Kaufen'], ['Vender', 'Verkaufen'],
        ]
    },
    'eng_pro': {
        '1': [
            ['Perchero', 'coat rack']
        ]
    }
}


def study(request, language, number, hide=True):
    to_study = info[language][str(number)]
    if hide == '0':
        hide = False
    elif hide == '1':
        hide = True
        
    #Add an space to info so we can fill it later
    for i in range(len(to_study)):
        if len(to_study[i])<3:
            to_study[i].append(None)
        else:
            to_study[i][2] = None

    return render(request, 'languages.html', {'lessons': lessons, 'information': to_study, 'hidden': hide, 'lang':language, 'num': number})

def compare_words(word, word_to_compare):
    word_to_analize = list(word)
    word_to_compare_to = list(word_to_compare)
    hits = 0
    proximity_index = 0.7
    hits_factor = proximity_index*len(word_to_analize)

    #Fill the smaller word with spaces
    if len(word_to_analize)>len(word_to_compare_to):
        for i in range(len(word_to_analize)-len(word_to_compare_to)):
            word_to_compare_to.append('')
                
    elif len(word_to_compare_to)>len(word_to_analize):
        for i in range(len(word_to_compare_to)-len(word_to_analize)):
            word_to_analize.append('')

    #Compares letter to letter
    for i in range(len(word_to_compare_to)):
        if word_to_compare_to[i] == word_to_analize[i]:
            hits = hits+1

    hits_factor = proximity_index*len(word_to_analize)

    if hits > hits_factor:
        guess = True
    else:
        guess = False

    return guess


def evaluate(request, language, number):
    answers = info[language][str(number)]
    guesses = []
    
    if request.method == 'POST':
        for i in range(len(answers)):
            word = request.POST.get('word'+str(answers[i][0]), answers[i][1])
            translated = answers[i][1]

            if len(answers[i])<3:
                answers[i].append(compare_words(word, translated))
            else:
                answers[i][2] = compare_words(word, translated)

    else:
        messages.error(request, "Unexpected error ocurred while selecting lesson")
    hide = True
    
    return render(request, 'languages.html', {'lessons': lessons, 'information': answers, 'hidden': hide, 'lang':language, 'num': number})