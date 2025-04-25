import time

def pausa_corta():
    time.sleep(0.7)

def pausa_media():
    time.sleep(1)

def pausa():
    time.sleep(1.6)

def pausa_larga():
    time.sleep(2.2)

def pausa_importante():
    time.sleep(3.3)

### Diccionarios: Registro de habitaciones y objetos

visited_rooms = {
    "habitacion_principal": True,
    "vestidor": False,
    "bathroom": False,
    "libreria_personal": True,
    "sala_reliquias": False,
    "sala_trofeos": False,
    "pasillo_principal": False,
    "salon_baile": False,
    "salon_ceremonia": False,
    "comedor": False,
    "puerta_principal": False
}

objetos_recogidos = {
    "vestido": False,
    "maquillaje": False,
    "libro_encantado": True,
    "daga_plateada": False,
    "celular": False,
    "velas": False,
    "llave": True,
    "mantel": False,
}

### Funciones completas 

def vestidor():
    if visited_rooms["vestidor"]: ## Si ya entraste a esta habitación
        print("\nHas vuelto al vestidor. Ya estuviste aquí antes.\n")
        if objetos_recogidos.get("vestido"):
            pausa()
            print("Por cierto, ¡el vestido te queda lindo!")
            pausa()
            if objetos_recogidos.get("libro_encantado") and objetos_recogidos.get("vestido") and not objetos_recogidos.get("maquillaje"):
                pausa_importante()
                print( + "\nPista: Ya tienes un vestido antiguo...")
                pausa()
                print( + "Tal vez necesitas algo más para completar tu disfraz...\n")
                pausa()
            elif objetos_recogidos.get("libro_encantado") and objetos_recogidos.get("vestido") and objetos_recogidos.get("maquillaje"):
                pausa()
                print( + "\nPista: Un vestido antiguo y maquillaje pálido...")
                pausa()
                print( + "¡Luces como toda una vampira!\n")
                pausa()

        opciones_mostradas = {
            "sur": "Dormitorio" if visited_rooms["habitacion_principal"] else "sur (puerta no explorada)",
            "oeste": "Baño" if visited_rooms["bathroom"] else "oeste"
        }

        print("\n¿A dónde deseas ir?")
        pausa()
        print(f"♥ {opciones_mostradas['sur'].capitalize()}")
        pausa_corta()
        print(f"♥ {opciones_mostradas['oeste'].capitalize()}")
    
        respuesta = ""
        while respuesta not in opciones_mostradas.values():
            pausa()
            respuesta = input("\nSelecciona la puerta:  ").strip().lower()

            if respuesta == "sur" or respuesta == "dormitorio":
                posicion_actual = "habitacion_principal"
                habitacion_principal()
            elif respuesta == "oeste" or respuesta == "baño":
                posicion_actual = "bathroom"
                bathroom()
            else:
                print("\n¡Esa no es una puerta! Intenta de nuevo.")
        return posicion_actual

    # Primer ingreso a la habitación
    print("\n¡Has entrado al vestidor de Carmilla!")
    visited_rooms["vestidor"] = True
    pausa()
    print("\nVes cientos de hermosos y antiguos vestidos de gala colgando ordenadamente.")
    pausa()

    if objetos_recogidos.get("libro_encantado"):
        print( + "\nPista: ...Un vestido antiguo podría ser útil como disfraz para pasar desapercibida.")
        pausa_larga()

    while True:
        print("\n¿Quieres tomar uno?")
        pausa()
        respuesta = input("\nDecide (sí/no): ").strip().lower()
        if respuesta == "sí":
            pausa()
            print("\n¡Has tomado un vestido!")
            objetos_recogidos["vestido"] = True
            pausa()
            if objetos_recogidos.get("libro_encantado"):
                print( + "\nPista: Ya tienes un vestido antiguo...")
                pausa()
                print( + "Tal vez necesitas algo más para completar tu disfraz...\n")
                pausa()
            break

        elif respuesta == "no":
            print("\nDecides no tomar ningún vestido.\n")
            pausa()
            print( + "Necesitas una estrategia para sobrevivir, sigue explorando...\n")
            pausa_larga()
            break

        else:
            print("\nRespuesta inválida. Intenta de nuevo.")

    
        ###Diccionario de opciones para personalizarlas según historial de exploración del jugador

    opciones_mostradas = {
        "sur": "Dormitorio" if visited_rooms["habitacion_principal"] else "sur (puerta no explorada)",
        "oeste": "Baño" if visited_rooms["bathroom"] else "oeste"
    }

    print("\n¿A dónde deseas ir?")
    pausa()
    print(f"♥ {opciones_mostradas['sur'].capitalize()}")
    pausa_corta()
    print(f"♥ {opciones_mostradas['oeste'].capitalize()}")
   
    respuesta = ""
    while respuesta not in opciones_mostradas.values():
        pausa()
        respuesta = input("\nSelecciona la puerta:  ").strip().lower()

        if respuesta == "sur" or respuesta == "dormitorio":
            posicion_actual = "habitacion_principal"
            habitacion_principal()
        elif respuesta == "oeste" or respuesta == "baño":
            posicion_actual = "bathroom"
            bathroom()
        else:
            print("\n¡Esa no es una puerta! Intenta de nuevo.")
    return posicion_actual


def libreria_personal():
    posicion_actual = libreria_personal
    if visited_rooms["libreria_personal"]: ## Si ya entraste a esta habitación
        print("\nHas vuelto a la librería de Carmilla. Ya estuviste aquí antes.")
        if objetos_recogidos["libro_encantado"]:
            pausa_larga()
            print("\nDeberías considerar lo que aprendiste del libro...\n")
    else:
        print("\nHas entrado a la librería personal.")
        pausa_larga()
        print("\nEstanterías imponentes se alzan a lo largo de todas las paredes, envolviendo la habitación por completo.")
        pausa_importante()
        print("\nAl centro de la habitación observas un libro peculiar con páginas que emiten luz.")
        pausa_importante()
        print("\n'El ritual de la Luna Roja'")
        pausa()
        print("lee el título de la página en tinta bermellón.")
        pausa_importante()
        print("\nRápidamente escanéas las páginas del libro, y descubres que se trata de un hechizo peculiar.")
        pausa_larga()
        print("\nDeseosa de obtener más información que te ayude a escapar, sigues leyendo.")
        pausa_larga()
        print("\n'...Aquel que reúna los ingredientes necesarios en la noche de luna roja, obtendra la Bendición Diurna.'")
        pausa_importante()
        print("Bendición Diurna: Hechizo que le otorga a un vampiro la habilidad de existir bajo el sol, libre del daño de sus rayos.")
        pausa_importante()
        print("\nAquella hija de la luna que desee diambular bajo el sol deberá reunir los ingredientes necesarios en la noche de la luna roja.")
        pausa_importante()
        print("\n...En ese momento te das cuenta de que no has encontrado ni una sola ventana en toda la mansión.")
        pausa_importante()
        print("\nIngredientes:")
        pausa()
        print("•Media docena de lirios blancos.")
        pausa()
        print("•Tres gotas de agua de la fuente de la vitalidad.")
        pausa()
        print("•Una docena de colmillos de murciélago.")
        pausa()
        print("•Mantel de pelaje de licántropo.")
        pausa()
        print("•Velas de fuego rojizo.")
        pausa()
        print("•Daga plateada envuelta en seda.")
        pausa_importante()
        print("\nPara completar el ritual, es necesario bañar los objetos...")
        pausa_importante()
        print("...en la sangre de un humano adulto de corazón puro, durante las doce campanadas de media noche.")
        pausa_larga()
        print("\nAl seguir leyendo, aprendes que la luna roja es un evento importante en la cultura vampira,")
        pausa()
        print("y es costumbre realizar un baile de gala con clanes vecinos.")
        pausa_importante()
        print("\nAl final del hechizo, ves que la fecha programada para la luna roja coincide con la fecha de hoy.")
        pausa_importante()
        print("\nCon pánico, miras alrededor, y ves otra puerta...\n")
        visited_rooms["libreria_personal"] = True
        objetos_recogidos["libro_encantado"] = True 
        pausa_larga()

         ###Diccionario de opciones para personalizarlas según historial de exploración del jugador

    opciones_mostradas = {
        "sur": "reliquias" if visited_rooms["sala_reliquias"] else "sur (puerta no explorada)",
        "oeste": "dormitorio" if visited_rooms["habitacion_principal"] else "oeste"
    }

    print("\n¿A dónde deseas ir?")
    pausa()
    print(f"♥ {opciones_mostradas['sur'].capitalize()}")
    pausa_corta()
    print(f"♥ {opciones_mostradas['oeste'].capitalize()}")
   
    respuesta = ""
    while respuesta not in opciones_mostradas.values():
        pausa()
        respuesta = input("\nSelecciona la puerta:  ").strip().lower()

        if respuesta == "sur" or respuesta == "reliquias":
            posicion_actual = "reliquias"
            sala_reliquias()
        elif respuesta == "oeste" or respuesta == "dormitorio":
            posicion_actual = "habitacion_principal"
            habitacion_principal()
        else:
            print("\n¡Esa no es una puerta! Intenta de nuevo.")
    return posicion_actual
    
    
def habitacion_principal():
    posicion_actual = habitacion_principal
    if visited_rooms["habitacion_principal"]: ## Si ya entraste a esta habitación
        print("\nHas vuelto a la habitación de Carmilla. Aquí es donde iniciaste.")
        if objetos_recogidos.get("velas") and objetos_recogidos.get("mantel") and objetos_recogidos.get("daga_plateada"):
            pausa()
            print("\nSigilosamente, escondes todos los objetos en la habitación y vuelves a acostarte en la cama.")
            pausa_importante()
            print("\nLas horas pasan, y tratas de guardar la calma.")
            pausa_larga()
            print("\nEscuchas cómo van llegando los invitados.")
            pausa()
            print("\nEventualmente, también escuchas el pánico que cunde cuando no encuentran el resto de los ingredientes para el ritual.")
            pausa_importante()
            print("\nCarmilla: No, me rehúso. Sin los ingredientes para el ritual, no tiene caso matarla.")
            pausa_larga()
            print("\nAlgunas voces expresan descontento, pero ceden ante Carmilla.")
            pausa_larga()
            print("\nCarmilla: Es una mujer inocente. Si no puede ayudarnos a completar el ritual, no hay razón para herirla.")
            pausa_larga()
            print("\nDespués de un tiempo, Carmilla toca la puerta y entra a la habitación.")
            pausa_larga()
            print("\nPretendes estar dormida para ver lo que hará.")
            pausa_larga()
            print("\nCarmilla se sienta en la cama a tu lado y comienza a acariciar tu rostro con delicadeza.")
            pausa_importante()
            print("\nCarmilla: Despierta, hermosa. Te saliste con la tuya.")
            pausa_larga()
            print("\nSientes el corazón en la garganta.")
            pausa()
            print("\n¿Sabe que fuí yo?")
            pausa()
            print("\nUna risa escapa de sus labios.")
            pausa_larga()
            print("\nCarmilla: No te haré daño. La ventana para realizar el ritual ha terminado.")
            pausa()
            print("\nCarmilla: La luna roja vino y se fué, y con ella se fué tu utilidad para mí. Eres libre de irte.")
            pausa_importante()
            print("\nFinalmente te animaste a abrir los ojos y verla directamente.")
            pausa_larga()
            print("\nEn su mirada no había engaño o enojo, solo... diversión.")
            pausa_larga()
            print("\nCarmilla: Resulta que capturé a una humana bastante inteligente, ¿hmm?")
            pausa_larga()
            print("\nConvencida de que no estás en peligro, te relajaste en su proximidad.")
            pausa_larga()
            pausa()
            print("\nTú: ¿En verdad puedo irme?")
            print("\nCarmilla se acuesta a tu lado, y con su rostro recargado en una mano te mira sonriendo.")
            pausa_larga()
            print("\nCarmilla: La próxima luna roja no será hasta dentro de alrededor de seis años.")
            pausa_larga()
            print("\nCarmilla: Y para ese entonces lo mejor será elegir a otro humano.")
            pausa_larga()
            print("\nCarmilla: Claro que... si gustas quedarte, tampoco tengo un inconveniente con ello.")
            pausa_larga()
            print("\nCarmilla se acerca ligeramente a ti, como retándote a acercarte más.")
            while True:
                print("\n¿Deseas quedarte?")
                pausa()
                respuesta = input("\nDecide (quedarme/irme): ").strip().lower()
                if respuesta == "quedarme":
                    pausa()
                    print("\nAceptas el reto y te inclinas hacia Carmilla, robándole un beso.")
                    pausa_larga()
                    print("\nSu expresión es extática, y te toma del mentón para angular tu rostro hacia ella.")
                    pausa_importante()
                    print("\nBueno, no por nada terminé en su cama anoche...")
                    pausa_importante()
                    print("\nLograste sobrevivir la noche de luna roja y escapar de la mansión.")
                    pausa_importante()
                    print("\nFinal desbloqueado: Pacífico.")
                    pausa()
                    print("\nLograste esconder todos los objetos para el ritual a tiempo")
                    pausa_importante()
                    print("\nFinal secreto desbloqueado: Amante.")
                    pausa()
                    print("\nDecidiste quedarte con Carmilla en su mansión.")
                    pausa_importante()
                    print("\n¡Fin del juego!\n")
                    pausa()
                    exit()

                elif respuesta == "irme":
                    print("\nDecides no quedarte.")
                    pausa()
                    print("\nTe levantas de la cama, y Carmilla no te detiene.")
                    pausa()
                    print("\nSin embargo, su expresión se ve un poco decepcionada de tu decisión.")
                    pausa_larga()
                    print("\nLogras salir de la mansión caminando, y no te molestan más.")
                    pausa_importante()
                    print("\nLograste sobrevivir la noche de luna roja y escapar de la mansión.")
                    pausa_importante()
                    print("\nFinal desbloqueado: Pacífico.")
                    pausa()
                    print("\nLograste esconder todos los objetos para el ritual a tiempo")
                    pausa_importante()
                    print("\n¡Fin del juego!\n")
                    pausa()
                    exit()
                else:
                    print("\nRespuesta inválida. Intenta de nuevo.")
        elif objetos_recogidos["libro_encantado"]:
            pausa_larga()
            print( + "\nPista: Deberías considerar lo que aprendiste del libro... Explora la mansión y busca una forma de escapar.\n")

    else:
        print("\nCarmilla: La noche de luna roja")
        pausa_importante()
        print("\nJuego e historia desarrollados por Ada Cortez")
        pausa_importante()
        print("\n\n\n\nDespiertas con un dolor de cabeza palpitante y la garganta seca.")
        pausa_larga()
        print("\nEntre gruñidos, te estiras y tratas de recordar qué sucedió anoche.")
        pausa()
        print("\nLos recuerdos son borrosos...")
        pausa()
        print("\nCon esfuerzo, recuerdas haber salido de fiesta con tus amigas a celebrar tu promoción en el trabajo.")
        pausa_importante()
        print("\n¿Qué hora es?\n")
        pausa_media()
        print(".")
        pausa_media()
        print(".")
        pausa_media()
        print(".")
        pausa_importante()
        print("\n¿Dónde está mi celular?")
        pausa_larga()
        print("\nTe tallas los ojos para despertar mejor y buscarlo.")
        pausa()
        print("\nMiras alrededor... y no reconoces nada.")
        pausa_importante()
        print("\n¿EN DÓNDE ESTOY?")
        pausa()
        print("\nLa habitación está decorada con muebles antiguos y visiblemente costosos.")
        pausa()
        print("\nTienen la apariencia de no haber sido movidos por siglos.")
        pausa()
        print("\nTratas de recordar más sobre anoche...")
        pausa()
        print("\nTienes una tenue memoria de una hermosa mujer, alta y pálida, acercándose a ti al final de la noche.")
        pausa()
        print("\nSin embargo, no hay rastro de ella en la habitación.")
        pausa()
        print("\nA tu alrededor ves tres puertas.")
        visited_rooms["habitacion_principal"] = True
        pausa()

        ###Diccionario de opciones para personalizarlas según historial de exploración del jugador
    opciones_mostradas = {
        "norte": "vestidor" if visited_rooms["vestidor"] else "norte (puerta no explorada)",
        "este": "librería" if visited_rooms["libreria_personal"] else "este (puerta no explorada)",
        "oeste": "pasillo" if visited_rooms["pasillo_principal"] else "oeste (puerta no explorada)"
    }

    print("\n¿A dónde deseas ir?")
    pausa()
    print(f"♥ {opciones_mostradas['norte'].capitalize()}")
    pausa_corta()
    print(f"♥ {opciones_mostradas['este'].capitalize()}")
    pausa_corta()
    print(f"♥ {opciones_mostradas['oeste'].capitalize()}")

    respuesta = ""
    while respuesta not in opciones_mostradas.values():
        pausa()
        respuesta = input("\nSelecciona la puerta:  ").strip().lower()

        if respuesta == "norte" or respuesta == "vestidor":
            posicion_actual = "vestidor"
            vestidor()
        elif respuesta == "este" or respuesta == "librería":
            posicion_actual = "libreria_personal"
            libreria_personal()
        elif respuesta == "oeste" or respuesta == "pasillo":
            posicion_actual = "pasillo_principal"
            pasillo_principal()
        else:
            print("\n¡Esa no es una puerta! Intenta de nuevo.")
    return posicion_actual


def bathroom():
    if visited_rooms["bathroom"]:
        pausa_corta()
        print("\nHas vuelto al baño. Ya estuviste aquí antes.\n")
        if objetos_recogidos.get("vestido") and objetos_recogidos.get("maquillaje") and objetos_recogidos.get("libro_encantado"):
            pausa()
            print( + "Pista: Un vestido antiguo y maquillaje pálido...")
            pausa()
            print( + "¡Luces como toda una vampira!\n")
            pausa_corta()
            print( + "\n.")
            pausa_corta()
            print( + "\n.")
            pausa_corta()
            print( + "\n.")
            pausa_importante()
            print( + "\n¿En dónde se reunirán los vampiros...?")
            pausa_importante()
        elif objetos_recogidos.get("vestido") and objetos_recogidos.get("maquillaje"):
            pausa()
            print( + "Pista: Un vestido antiguo y maquillaje pálido...")
            print( + "¡Luces como toda una vampira!\n")
            pausa()
        else:
            pausa()
            print("No hay mucho que hacer aquí...")
    else:
        pausa()
        print("\n¡Has entrado al baño de la recámara!")
        pausa()
        print("\nLa decoración es anticuada, con una tina de gran tamaño y un bello tocador.")
        pausa_larga()
        print("\nNotas que no hay ningún un espejo en la habitación.")
        pausa_importante()
        print("\nAbres los cajones del tocador y encuentras maquillaje de un tono preocupántemente pálido.")
        pausa_larga()
        print("\n¿Cómo se maquilla si no tiene espejos...?")
        pausa_larga()
        if objetos_recogidos.get("libro_encantado") and objetos_recogidos.get("vestido"):
            print( + "\nPista: Maquillaje podría ayudarte a completar tu disfraz...")
            pausa_larga()

        while True:
            print("\n¿Quieres maquillarte?")
            pausa()
            respuesta = input("\nDecide (sí/no): ").strip().lower()
            if respuesta == "sí":
                pausa()
                print("\n¡Te has maquillado!")
                pausa()
                print("\n...Por lo menos lo mejor posible sin espejos.")
                objetos_recogidos["maquillaje"] = True
                pausa()
                if objetos_recogidos.get("libro_encantado"):
                    print( + "\n¡Tu disfraz está completo!")
                    pausa_importante()
                    print("\nMe pregunto en dónde se reunirán los vampiros...")
                    pausa_larga()
                break
            elif respuesta == "no":
                print("\nDecides no maquillarte.\n")
                pausa()
                print( + "Necesitas una estrategia para sobrevivir, sigue explorando...\n")
                pausa_larga()
                break
            else:
                print("\nRespuesta inválida. Intenta de nuevo.")

        visited_rooms["bathroom"] = True

    while True:
        opciones_mostradas = {
            "este": "Vestidor" if visited_rooms["vestidor"] else "este (puerta no explorada)",
            "esperar": "Esperar" if visited_rooms["bathroom"] else "esperar"
        }

        respuesta = ""
        while respuesta not in opciones_mostradas.values():
            print("\n¿A dónde deseas ir?")
            pausa()
            print(f"♥ {opciones_mostradas['este'].capitalize()}")
            pausa_corta()
            print(f"♥ {opciones_mostradas['esperar'].capitalize()}")
            pausa()
            respuesta = input("\nSelecciona tu decisión:  ").strip().lower()

            if respuesta == "este" or respuesta == "vestidor":
                posicion_actual = "vestidor"
                vestidor()
                return posicion_actual
            elif respuesta == "esperar":
                posicion_actual = "bathroom"
                pausa()
                print("\nMiras alrededor un poco más en busca de pistas.")
                pausa_larga()
                pausa_corta()
                print("\n.")
                pausa_corta()
                print("\n.")
                pausa_corta()
                print("\n.")
                pausa_corta()
                print("\nNo aprendes nada muy interesante,")
                pausa()
                print("excepto que a Carmilla aparentemente le gustan mucho")
                pausa()
                print("los productos de higiene con olor a rosas o lirios.\n")
                pausa()
            else:
                print("\n¡Esa no es una puerta! Intenta de nuevo.")

def sala_reliquias():
    if visited_rooms["sala_reliquias"]: ### Si ya entraste en la habitación. 
        print("\nHas vuelto al la sala de reliquias. Ya estuviste aquí antes.")
        if objetos_recogidos.get("daga_plateada") and not objetos_recogidos.get("velas") and not objetos_recogidos.get("mantel"):
            pausa()
            print("\nLa daga plateada que sujetas pesa, y tiene un filo aterrador.")
            pausa_importante()
            print("\nLos vampiros no son inmunes a la plata...")
            pausa_importante()
            print( + "\nTienes la ventaja del elemento sorpresa,")
            pausa()
            print( + "Carmilla no sabe que estás armada.")
            pausa_importante()
            print("\nConsideras tus opciones y la posibilidad de un escape sin violencia...")
            pausa_importante()
            print("\nAprietas tu agarre en la daga.")
            pausa_importante()
            print("\n¿Dónde estás Carmilla?\n")
        elif objetos_recogidos.get("daga_plateada") and objetos_recogidos.get("mantel") and objetos_recogidos.get("velas"):
            pausa_importante()
            print( + "\nPista: Un mantel, velas, una daga...")
            pausa_larga()
            print( + "Hmm... ¿No eran esos los elementos para el ritual de Carmilla?\n")
            pausa_importante()
            print("Me pregunto si podrá completar el hechizo sin todos sus ingredientes...")
            pausa()
        elif objetos_recogidos.get("daga_plateada") and (objetos_recogidos.get("mantel") or objetos_recogidos.get("velas")):
            pausa()
            print( + "\nPista: Estás cerca de un escape pacífico...")
            pausa()
            print( + "Solo un elemento más...\n")
            pausa()
            print("\n.")
            pausa_corta()
            print("\n.")
            pausa_corta()
            print("\n.")
            pausa_importante()
            print("\n¿Cuáles eran los ingredientes del ritual?")
            pausa()
    else:
        pausa()
        print("\n¡Has entrado al salón de reliquias!")
        visited_rooms["sala_reliquias"]=True 
        pausa()
        print("\nUn escalofrío recorre tu espalda al cruzar el umbral.")
        pausa_importante()
        print("\nEl centro de la sala tiene altos pilares con objetos dentro de vitrinas.")
        pausa_importante()
        print( + "\nParece... una colección.")
        pausa()
        print("\n'Reliquias de la luna'")
        pausa()
        print("Lee la inscripción a la entrada de la exposición.")
        pausa_larga()
        print("\nTe das una vuelta por la sala y observas los")
        pausa()
        print("diversos objetos de aspecto curioso que captan tu atención.")
        pausa_larga()
        print("\nLa habitación está repleta de más riquezas de las que podrías imaginar.")
        pausa_importante()
        print("\nVes joyería de aspecto antiguo, retratos al óleo pintados a lo largo de los siglos,")
        pausa_importante()
        print("y vestidos confeccionados con telas suaves y sedosas, provenientes de diversas épocas...")
        pausa_importante()
        print("\nY al fondo de la habitación, algo extraño.")
        pausa_larga()
        print("\nTe acercas para inspeccionar.")
        pausa_corta()
        print("\n.")
        pausa_corta()
        print("\n.")
        pausa_corta()
        print("\n.")
        pausa_importante()
        print("\nEstiras la mano y tocas un cofre metálico, frío al tacto.")
        pausa_importante()
        print("\n¿Por qué está separado del resto de reliquias?")
        pausa_importante()
        print("\nTocas con delicadeza la cerradura del cofre...")
        pausa_larga()
        if objetos_recogidos.get("llave"):
            print("\n¿Podría ser...?")
            pausa_larga()
            print("\nMetes la mano a tu bolsillo y tomas la llave que encontraste.")
            pausa_larga()
            print("\nTratas de insertarla en la cerradura...")
            pausa_importante()
            print("\n. . .")
            pausa_importante()
            print("\n¡Y logras abrir el cofre!")
            pausa_importante()
            print("\nMiras adentro, y pierdes el aliento.")
            pausa_importante()
            print("\nDentro del cofre hay una daga de plata con rubíes en la empuñadura.")
            pausa_larga()
            print("\nDudas por un momento, pero inhalas con profundidad y tomas la daga del cofre.")
            pausa_importante()
            print("\nAhora tienes con qué defenderte...")
            objetos_recogidos["daga_plateada"]=True 
            pausa_importante()
            if objetos_recogidos.get("mantel") and objetos_recogidos.get("velas"):
                pausa_larga()
                print( + "\nPista: Un mantel, velas, una daga...")
                pausa_larga()
                print( + "\n¿No eran esos los ingredientes para el ritual?\n")
                pausa_larga()
            elif objetos_recogidos.get("mantel") or objetos_recogidos.get("velas"):
                pausa_larga()
                print( + "¿Qué podrías hacer con una daga?")
        elif not objetos_recogidos.get("llave"):
            print("\n¿Qué habrá adentro?")
            pausa()
            print("\nLa curiosidad te impulsa.")
            pausa()
            print("\nTratas de abrirlo...")
            pausa_corta()
            print("\n.")
            pausa_corta()
            print("\n.")
            pausa_corta()
            print("\n.")
            pausa_larga()
            print("\n...Pero es inútil. Está cerrado.")
            pausa_larga()
            print( + "\nPista: La llave debe estar en algún lado...\n")
    
    while True:
        opciones_mostradas = {
            "norte": "librería" if visited_rooms["libreria_personal"] else "librería (puerta no explorada)",
            "sur": "sur" if visited_rooms["sala_trofeos"] else "trofeos"
        }

        respuesta = ""
        while respuesta not in opciones_mostradas.values():
            print("\n¿A dónde deseas ir?")
            pausa()
            print(f"♥ {opciones_mostradas['norte'].capitalize()}")
            pausa_corta()
            print(f"♥ {opciones_mostradas['sur'].capitalize()}")
            pausa()
            respuesta = input("\nSelecciona la puerta:  ").strip().lower()

            if respuesta == "norte" or respuesta == "librería":
                posicion_actual = "libreria_personal"
                libreria_personal()
                return posicion_actual
            elif respuesta == "sur" or respuesta == "trofeos":
                posicion_actual = "sala_trofeos"
                sala_trofeos()
                pausa()
            else:
                print("\n¡Esa no es una puerta! Intenta de nuevo.")


def sala_trofeos():
    if visited_rooms["sala_trofeos"]:
        pausa_corta()
        print("\nHas vuelto a la sala de trofeos. Ya estuviste aquí antes.\n")
        pausa()
        print("No hay mucho que hacer aquí. ¡Sigue explorando!")
    else:
        pausa()
        print("\n¡Has entrado a la sala de trofeos!")
        pausa()
        print("\nEl ambiente de la habitación es pesado.")
        pausa()
        print("\nCasi sofocante.")
        pausa()
        print("\nMiras alrededor y observas cápsulas con diversos objetos y placas, cual museo.")
        pausa_larga()
        print("\nAmy Johnson")
        pausa_larga()
        print("\nBrianna Martinez")
        pausa_larga()
        print("\nVanessa Batista")
        pausa_larga()
        print("\nIdalid Cortez")
        pausa_larga()
        print("\nPlacas con más nombres rodean la habitación.")
        pausa()
        print("\nTe acercas a las cápsulas para ver qué contienen.")
        pausa()
        print("\nAlgunas tienen prendas de ropa, otros contienen objetos más... tétricos.")
        pausa_larga()
        print("\nTrozos de cabello... pequeñas botellas con lo que aparenta ser sangre...")
        pausa_importante()
        print("\nSientes un nudo en la garganta.")
        pausa()
        print("\nAl fondo de la habitación ves algo que hace que el corazón se te caiga al suelo.")
        pausa_importante()
        print("\nEs tu propio nombre en una placa.")
        pausa_larga()
        print("\nTe acercas y notas que tu cápsula no está vacía.")
        pausa()
        print("\nEchas un vistazo, y adentro ves un mechón de tu propio pelo.")
        pausa()
        print("\nRápidamente te llevas las manos a tu propio cabello y sientes la asimetría.")
        pausa_larga()
        print("\n¿Qué le habrá hecho a todas estas chicas?")
        pausa()
        print("\nDentro de tu cápsula alcanzas a ver algo más...")
        pausa_corta()
        print("\n.")
        pausa_corta()
        print("\n.")
        pausa_corta()
        print("\n.")
        pausa_corta()
        print("\n¡Es tu celular!")
        pausa()
        while True:
            print("\n¿Quieres tomar tu celular?")
            pausa()
            print( + "\nCuidado con hacer ruido...")
            pausa()
            print( + "\nNo queremos que Carmilla se de cuenta...")
            pausa()
            respuesta = input("\nTomar celular (sí/no): ").strip().lower()
            if respuesta == "sí":
                pausa()
                print("\nLa cápsula no estaba cerrada. ¡Lograste tomar tu celular!")
                pausa_larga()
                print("\nTratas de encenderlo, pero no responde.")
                pausa()
                print("\nLo revisas con detenimiento y ves que le han quitado la batería.")
                objetos_recogidos["celular"] = True
                pausa_larga()
                print( + "\nNo será muy útil.")
                pausa()
                break
            elif respuesta == "no":
                print("\nDecides no intentar tomar tu celular.\n")
                pausa()
                print( + "Necesitas una estrategia para sobrevivir, sigue explorando...\n")
                pausa_larga()
                break
            else:
                print("\nRespuesta inválida. Intenta de nuevo.")

        visited_rooms["sala_trofeos"] = True

    while True:
        opciones_mostradas = {
            "norte": "reliquias" if visited_rooms["sala_reliquias"] else "norte (puerta no explorada)",
            "esperar": "Esperar" if visited_rooms["sala_trofeos"] else "esperar"
        }

        respuesta = ""
        while respuesta not in opciones_mostradas.values():
            print("\n¿A dónde deseas ir?")
            pausa()
            print(f"♥ {opciones_mostradas['norte'].capitalize()}")
            pausa_corta()
            print(f"♥ {opciones_mostradas['esperar'].capitalize()}")
            pausa()
            respuesta = input("\nSelecciona tu decisión:  ").strip().lower()

            if respuesta == "norte" or respuesta == "reliquias":
                posicion_actual = "sala_reliquias"
                sala_reliquias()
                return posicion_actual
            elif respuesta == "esperar":
                posicion_actual = "sala_trofeos"
                pausa()
                print("\nMiras alrededor un poco más en busca de pistas.")
                pausa_larga()
                pausa_corta()
                print("\n.")
                pausa_corta()
                print("\n.")
                pausa_corta()
                print("\n.")
                pausa_corta()
                print("\nNo aprendes nada nuevo,")
                pausa()
                print("excepto que Carmilla aparentemente solo ha secuestrado mujeres.")
                pausa()
                print("... Y que le agrada el cabello largo.\n")
                pausa()
            else:
                print("\n¡Esa no es una puerta! Intenta de nuevo.")


def puerta_principal():
    if visited_rooms["puerta_principal"]:
        print("\n¡Volviste a la puerta principal!")
    else:
        print("\n¡Has encontrado la puerta principal de la mansión!")
        pausa()
        if objetos_recogidos.get("llave"):
            print( + "\n¡Tienes una llave!")
            pausa()
            while True:
                print("\n¿Quieres tratar de abrir la puerta principal?")
                pausa()
                print( + "\nCuidado con hacer ruido...")
                pausa()
                print( + "\nNo queremos que Carmilla se de cuenta...")
                pausa()
                respuesta = input("\nAbrir puerta (sí/no): ").strip().lower()
                if respuesta == "sí":
                    pausa()
                    print("\nIntentas abrir la puerta...")
                    pausa_importante()
                    print("\n¡La llave no entra en la cerradura!")
                    pausa_larga()
                    print("\nDespués de fallar en insertar la llave, trataste de abrir la puerta")
                    pausa()
                    print("de todas maneras, y los seguros y el aldabón causaron un estruendor.")
                    pausa_importante()
                    print("\nEscuchas pasos con tacón que se aproximan con agilidad...")
                    pausa_importante()
                    print("\n¡Es Carmilla!")
                    pausa()
                    print("\n¡CORRE!")
                    pausa_larga()
                    print("\nTrataste de huir, pero no llegaste muy lejos.")
                    pausa_larga()
                    print("\nUna mano helada te tomó de la cintura y te jaló hacia ella.")
                    pausa_larga()
                    print("\nEstás frente a frente con Carmilla, y te sujeta con firmeza.")
                    pausa_larga()
                    print("\nCarmilla: Aww, ¿qué pasó, bonita? ¿Creíste que escapar sería tan fácil?")
                    pausa_importante()
                    print("\nTratas de resistir su agarre, pero es muy fuerte.")
                    pausa_importante()
                    print("\nCarmilla se ríe, y pone una mano alrededor de tu cuello.")
                    pausa_importante()
                    print("\nCarmilla: Lo siento, preciosa. Tengo planes para tí esta noche.")
                    pausa_larga()
                    print("\nSe acerca más a ti e inhala tu aroma, y en un movimiento brusco clava sus colmillos en tu cuello.")
                    pausa_importante()
                    print("\nPronto te desvaneces, y lo último que escuchas es a Carmilla deleitándose en tu sabor.")
                    pausa_importante()
                    print("\n¡Has perdido! No lograste sobrevivir la noche de luna roja.")
                    pausa_larga()
                    print("\n¡Fin del juego!")
                    exit()
                    break
                elif respuesta == "no":
                    print("\nDecides no abrir la puerta.\n")
                    pausa()
                    print( + "Necesitas una estrategia para sobrevivir, sigue explorando...\n")
                    visited_rooms["puerta_principal"]=True
                    pausa_larga()
                    break
                else:
                    print("\nRespuesta inválida. Intenta de nuevo.")

                    
    while True:   
        opciones_mostradas = {
            "norte": "comedor" if visited_rooms["comedor"] else "norte (puerta no explorada)",
            "este": "baile" if visited_rooms["salon_baile"] else "este (puerta no explorada)"
        }

        respuesta = ""
        while respuesta not in opciones_mostradas.values():
            print("\n¿A dónde deseas ir?")
            pausa()
            print(f"♥ {opciones_mostradas['norte'].capitalize()}")
            pausa_corta()
            print(f"♥ {opciones_mostradas['este'].capitalize()}")
            pausa()
            respuesta = input("\nSelecciona tu decisión:  ").strip().lower()

            if respuesta == "norte" or respuesta == "comedor":
                posicion_actual = "comedor"
                comedor()
                return posicion_actual
            elif respuesta == "este" or respuesta == "baile":
                posicion_actual = "salon_baile"
                salon_baile()
                return posicion_actual
            else:
                print("\n¡Esa no es una puerta! Intenta de nuevo.")

def comedor():
    if visited_rooms["comedor"]:
        print("\n¡Volviste al comedor!")
    else:
        print("\n¡Has encontrado el comedor!")
        pausa()
        print("\nUna mesa de banquetes se estira a lo largo de la habitación,")
        pausa()
        print("rodeada de elegantes sillas y decoraciones rojizas.")
        pausa_larga()
        if objetos_recogidos.get("libro_encantado"):
            print("\nTe acercas a la mesa y notas que los manteles tienen una textura interesante.")
            pausa_larga()
            print("Son suaves y...")
            pausa()
            print("\n¿Peludos?")
            pausa()
            while True:
                print("\n¿Quieres tomar los manteles?")
                pausa_larga()
                print( + "\nPista: Recuerda los ingredientes del ritual.")
                respuesta = input("\nTomar manteles (sí/no): ").strip().lower()
                if respuesta == "sí":
                    pausa()
                    print("\nTomaste los manteles de licántropo del comedor.")
                    objetos_recogidos["manteles"] = True
                    if objetos_recogidos.get("velas") and objetos_recogidos.get("daga_plateada"):
                        pausa()
                        print("\n¡Tienes todos los objetos necesarios para el ritual!")
                        pausa_larga()
                        print( + "\nSeguramente Carmilla no podrá completar el hechizo sin ellos...")
                        pausa_larga()
                        print( + "\n¡Rápido, que no te encuentre merodeando por la mansión!")
                        pausa()
                        break
                    elif objetos_recogidos.get("velas") or objetos_recogidos.get("daga_plateada"):
                        pausa()
                        print(+ "\nPista: Estás muy cerca, solo un objeto más...")
                        break
                    else:
                        break
                elif respuesta == "no":
                    print("\nDecides no tomar los manteles.\n")
                    pausa()
                    print( + "Necesitas una estrategia para sobrevivir, sigue explorando...\n")
                    pausa_larga()
                    break
                else:
                    print("\nRespuesta inválida. Intenta de nuevo.")

                    
    while True:   
        opciones_mostradas = {
            "sur": "puerta" if visited_rooms["puerta_principal"] else "sur (puerta no explorada)",
            "este": "pasillo" if visited_rooms["pasillo_principal"] else "este (puerta no explorada)"
        }

        respuesta = ""
        while respuesta not in opciones_mostradas.values():
            print("\n¿A dónde deseas ir?")
            pausa()
            print(f"♥ {opciones_mostradas['sur'].capitalize()}")
            pausa_corta()
            print(f"♥ {opciones_mostradas['este'].capitalize()}")
            pausa()
            respuesta = input("\nSelecciona tu decisión:  ").strip().lower()

            if respuesta == "sur" or respuesta == "puerta":
                posicion_actual = "puerta_principal"
                puerta_principal()
                return posicion_actual
            elif respuesta == "este" or respuesta == "pasillo":
                posicion_actual = "pasillo_principal"
                pasillo_principal()
                return posicion_actual
            else:
                print("\n¡Esa no es una puerta! Intenta de nuevo.")


def salon_baile():
    if visited_rooms["salon_baile"]:
        print("\n¡Has vuelto al salón de baile!")
    else:
        print("\n¡Has encontrado el salón de baile!")
        visited_rooms["salon_baile"]=True
    if objetos_recogidos.get("vestido"):
        pausa()
        print("\n¡Tu hermoso vestido es ideal para la ocasión!")
        pausa_larga()
        print("\nParece que todo está listo para una celebración...")
        if objetos_recogidos.get("libro_encantado") and not objetos_recogidos.get("maquillaje"):
            pausa()
            print( + "\nPista: Con un poco de maquillaje, tu disfraz estaría completo...")
            pausa()
            print("\nRecuerda... esta es una celebración de vampiros.")
        if objetos_recogidos.get("libro_encantado") and objetos_recogidos.get("maquillaje"):
            pausa()
            print("\n¡Has llegado justo a  tiempo!")
            pausa()
            print("\n¡La fiesta está por comenzar!")
            pausa()
            print("\nA tu alrededor, cientos de vampiros danzan en sus atuendos de lujo,")
            pausa_larga()
            print("disfrutando de la noche, los bocadillos y las bebidas que ofrece su host.")
            pausa_larga()
            print("\nCon toda la falsa confianza que puedes concentrar,")
            pausa_larga()
            print("caminas por el salón con pasos decisivos, mezclándote entre los presentes.")
            pausa_larga()
            print("\nPor un momento, temes. Pero nadie a tu alrededor parece notar que no perteneces al clan.")
            pausa_importante()
            print("\n¡Funcionó! No puedo creer que funcionó.")
            pausa_larga()
            print("\nAhora lo único que falta es esperar a que pase la luna roja.")
            pausa_importante()
            print("Y, con suerte, lograr cruzar la salida escondida entre los vampiros invitados.")
            pausa_importante()
            print("\nPronto, tus pensamientos fueron interrumpidos por aplausos.")
            pausa_larga()
            print("\nVolteas para buscar el origen del alboroto.")
            pausa_larga()
            print("\nPosada en la cima de las escaleras con un aire dominante, Carmilla observa a sus invitados con detenimiento.")
            pausa_importante()
            print("\nAbrazada por un vestido carmesí con acentos de encaje negro,")
            pausa_larga()
            print("y adornada por ajustado corset oscuro por su cintura del mismo tono de su largo cabello,")
            pausa_larga()
            print("decides que Carmilla es la mujer más hermosa que jamás hayas visto.")
            pausa_importante()
            print("\nCarmilla desciende, y recibe a sus invitados cálidamente.")
            pausa_larga()
            print("\nTodos se iluminan al verla, y sus ojos la siguen por la habitación.")
            pausa_larga()
            print("\nTe da la impresión de que es profundamente respetada por todos los miembros de su clan.")
            pausa_larga()
            print("\nCarmilla: Bienvenidos sean todos a la mansión von Karnstein.")
            pausa_larga()
            print("\nUna atractiva sonrisa afilada decoró su rostro.")
            pausa_larga()
            print("\nCarmilla: Esta noche marca nuestra vigésima segunda reunión bajo la luna roja.")
            pausa_importante()
            print("\nCarmilla: Hoy tendremos una nueva oportunidad para realizar el hechizo diurno.")
            pausa_importante()
            print("\nEstiró su brazo con elegancia para señalar la luna en el horizonte.")
            pausa_larga()
            print("\nSu sonrisa se debilitó por un momento, y se acercó a un pequeño vampiro")
            pausa_importante()
            print("que la miraba con adoración, cubierto de cicatrices de quemaduras en su joven rostro.")
            pausa_larga()
            print("\nCon delicadeza, Carmilla acarició su mejilla.")
            pausa_importante()
            print("\nCarmilla: No me rendiré hasta lograr el hechizo diurno con éxito. Les doy mi palabra.")
            pausa_importante()
            print("\nCarmilla: Hasta que seamos libres de nuestra prisión nocturna. La cresta von Karnstein los protegerá.")
            pausa_importante()
            print("\nCarmilla tomó una copa y la alzó en el aire, y todos siguieron su liderazgo.")
            pausa_importante()
            print("\nCarmilla: ¡Por un futuro donde podamos caminar bajo el sol con tranquilidad!")
            pausa_importante()
            print("\n'¡Salud!' se escuchó al unísono. '¡Por Carmilla von Karnstein!' agregaron algunos.")
            pausa_importante()
            print("\nLa fiesta siguió con normalidad, y pronto llegó la hora del ritual.")
            pausa_larga()
            print("\nA la distancia, notaste que un vampiro entró al salón y le susurró algo a Carmilla en el oído.")
            pausa_importante()
            print("\nCarmilla: ¿¡PERDIDA!?")
            pausa_larga()
            print("\nAnte las miradas de sus invitados, bajó la voz.")
            pausa_larga()
            print("\nCarmilla: ¿A qué te refieres con perdida? ¡¿En dónde está?!")
            pausa_larga()
            print("\nAlcanzaste a ver cómo la mirada de pánico de Carmilla lentamente se transformó en una de ira.")
            pausa_importante()
            print("\nAntes de que fuera muy tarde, te uniste a un grupo de vampiros que pretendía salir a tomar aire fresco.")
            pausa_larga()
            print("\nCon cautela, los seguiste hacia la puerta principal.")
            pausa_larga()
            print("\nTan cerca...")
            pausa_larga()
            print("\nEl resto del grupo de vampiros cruzó el umbral, podrías sentir la brisa de tu libertad corriendo por la entrada.")
            pausa_importante()
            print("\nDe la nada, una mano te tomó de la muñeca.")
            pausa_larga()
            print("\nCarmilla: Disculpa, me parece no haberte visto por aquí antes.")
            pausa_larga()
            print("\nMantienes una expresión neutra y rezas que Carmilla no pueda detectar tu ansiedad.")
            pausa_larga()
            print("\nNotas que sus ojos te recorren de pies a cabeza con intensidad.")
            pausa_larga()
            print("\nTú: Es mi primera vez asistiendo...")
            pausa_larga()
            print("\nSu mirada te penetra, y te considera en silencio.")
            pausa_larga()
            print("\nCarmilla: Ya veo...")
            pausa_importante()
            print("\nFinalmente, Carmilla te sonríe.")
            pausa_larga()
            print("\nCarmilla: Carmilla von Karnstein, encantada.")
            pausa_larga()
            print("\nCarmilla: Estamos teniendo algunos contratiempos con el ritual, uno de los ingredientes decidió esconderse.")
            pausa_larga()
            print("\nSu mirada rápidamente escaneó los alrededores.")
            pausa_larga()
            print("\nCarmilla: Mantén esos bellos ojos abiertos en caso de que veas una joven humana merodeando por aquí.")
            pausa_importante()
            print("\nCarmilla te guiñó el ojo.")
            pausa()
            print("\nCarmilla: Fue un placer, espero verte de nuevo muy pronto....")
            pausa_larga()
            print("\nOlvidaste presentarte de vuelta.")
            pausa_larga()
            print("\nTú: Laura. El placer es mío.")
            pausa_larga()
            print("\nUna chispa de interés brilló en sus ojos.")
            pausa_larga()
            print("\nCarmilla se inclinó con elegancia y besó tu mano.")
            pausa_importante()
            print("\nDisfruta la fiesta, Laura. Vendré a buscarte después del ritual.")
            pausa_larga()
            print("\nDespués se alejó en dirección a la habitación principal.")
            pausa_larga()
            print("\n¡Se fué! Es ahora o nunca.")
            pausa()
            print("\nAún algo confundida por su comportamiento, te das la vuelta y cruzas por la puerta.")
            pausa_importante()
            print("\nAún sintiendo el calor de sus labios en tu piel, sales de la mansión.")
            pausa_importante()
            print("\nCarmilla von Kernstein...")
            pausa_importante()
            pausa()
            print("\n¡Felicidades! Lograste escapar de la mansión antes del ritual.")
            pausa_larga()
            print("\n¡Has ganado el juego!")
            pausa_larga()
            print("\nFinal desbloqueado: Ingeniosa.")
            pausa()
            print("\nLograste hacerte pasar por vampiro para escapar.")
            pausa_importante()
            print("\n¡Fin del juego!\n")
            pausa()
            exit()
    elif objetos_recogidos.get("libro_encantado") and not objetos_recogidos.get("velas"):
        print("\nEl salón de baile impone poder con sus techos altos y pilares gruesos.")
        pausa_larga()
        print("\nCon cuidado, exploras la habitación en busca de algo útil para tu escape.")
        pausa_larga()
        print("\nEn una mesa al centro del salón, encuentras velas rojizas.")
        pausa()
        print("\nConsideras que podrían resultar útiles, entonces las tomas.")
        objetos_recogidos["velas"]=True
        pausa_larga()
        print("\nEn la misma mesa, encuentras una llave.")
        while True:
                print("\n¿Quieres tomar la llave?")
                pausa_larga()
                print( + "\nPista: Podrías abrir algo especial...")
                respuesta = input("\nTomar llave (sí/no): ").strip().lower()
                if respuesta == "sí":
                    pausa()
                    print("\nTomaste la llave de la mesa.")
                    pausa()
                    objetos_recogidos["llave"] = True
                    break
                elif respuesta == "no":
                    print("\nDecides no tomar la llave.\n")
                    pausa()
                    print( + "Necesitas una estrategia para sobrevivir, sigue explorando...\n")
                    pausa_larga()
                    break
                else:
                    print("\nRespuesta inválida. Intenta de nuevo.")

    else:
        print("\nNo hay mucha actividad en esta habitación.")
                    

    while True:   
        opciones_mostradas = {
            "norte": "pasillo" if visited_rooms["pasillo_principal"] else "norte (puerta no explorada)",
            "sur": "ceremonia" if visited_rooms["salon_ceremonia"] else "sur (puerta no explorada)",
            "oeste": "puerta" if visited_rooms["puerta_principal"] else "oeste (puerta no explorada)"
        }

        respuesta = ""
        while respuesta not in opciones_mostradas.values():
            print("\n¿A dónde deseas ir?")
            pausa()
            print(f"♥ {opciones_mostradas['norte'].capitalize()}")
            pausa_corta()
            print(f"♥ {opciones_mostradas['sur'].capitalize()}")
            pausa_corta()
            print(f"♥ {opciones_mostradas['oeste'].capitalize()}")
            pausa()
            respuesta = input("\nSelecciona tu decisión:  ").strip().lower()

            if respuesta == "norte" or respuesta == "pasillo":
                posicion_actual = "pasillo_principal"
                pasillo_principal()
                return posicion_actual
            elif respuesta == "sur" or respuesta == "ceremonia":
                posicion_actual = "salon_ceremonia"
                salon_ceremonia()
                return posicion_actual
            elif respuesta == "oeste" or respuesta == "puerta":
                posicion_actual = "puerta_principal"
                puerta_principal()
                return posicion_actual
            else:
                print("\n¡Esa no es una puerta! Intenta de nuevo.")


def salon_ceremonia():
    if visited_rooms["salon_ceremonia"]:
        print("\n¡Has vuelto al salón de ceremonias!")
    else:
        print("\n¡Has entrado al salón de ceremonias!")
        pausa()
        print("\nLa habitación se encuentra a oscuras, con la tenue iluminación de un par de lámparas en el techo.")
        pausa_larga()
        print("\nEres silenciosa, y al fondo de la habitación alcanzas a divisar una silueta.")
        pausa_larga()
        print("\nCarmilla está arrodillada frente un altar, inmersa en lo que está haciendo.")
        pausa_larga()

    if objetos_recogidos.get("daga_plateada") and objetos_recogidos.get("libro_encantado"):
        pausa()
        print( + "\nEs tu oportunidad.")
        pausa_larga()
        print("\nTe arrodillas detrás de ella sigilosamente.")
        pausa_larga()
        print("\nAhora que estás cerca, notas que Carmilla está sollozando frente al altar.")
        pausa_importante()
        print("\nSientes un tirón en el pecho al verla llorando, pero necesitas escapar.")
        pausa_importante()
        print("\nDentro de ti, lamentas no tener otra opción.")
        pausa_larga()
        print("\nCon cuidado, extraes la daga plateada de tu bolsillo.")
        pausa_importante()
        print("\nLo harás rápido. Un solo corte en el cuello para evitar sufrimiento.")
        pausa_larga()
        print("\nTus manos comienzan a sudar. Nunca has hecho esto antes.")
        pausa_larga()
        print("\nCarmilla: Eres muy valiente. ¿Sabes?")
        pausa_larga()
        print("\nTus movimientos se congelan al escuchar su voz.")
        pausa_larga()
        if visited_rooms["sala_trofeos"]:
            print("\nCarmilla: Las demás optaron por tratar de escapar por la puerta principal. Algunas nunca salieron de mi habitación.")
            pausa_importante()
            print("\nLas otras chicas...")
        pausa()
        print("\nCarmilla se lanza sobre ti, y te sujeta contra el suelo.")
        pausa_larga()
        print("\nCarmilla: En verdad es una pena, realmente no quiero herirte.")
        pausa()
        print("\nSusurra las palabras, y sus ojos siguen llorosos.")
        pausa_larga()
        print("\nLa miras a los ojos en silencio con la daga aún en tu mano.")
        pausa_larga()
        print("\nParece encontrar algo en tu mirada, porque sus lágrimas comienzan a fluir de nuevo.")
        pausa_importante()
        print("\nCarmilla comienza a reír suavemente mientras sus mejillas se empapan.")
        pausa_larga()
        print("\nCarmilla: No es tu culpa...")
        pausa()
        print("\nCarmilla: Te necesito para mi ritual.")
        pausa_larga()
        print("\nSu voz está llena de dolor, y sientes un apretón en el pecho al escucharla.")
        pausa_larga()
        print("\nTú: Y yo necesito salir de aquí con vida.")
        pausa_larga()
        print("\nJalas a Carmilla hacia ti en un fuerte abrazo.")
        pausa_importante()
        print("...y la daga atraviesa su pecho.")
        pausa_importante()
        print("\nCarmilla no se aleja.")
        pausa()
        print("\nAl contrario, envuelve sus brazos alrededor de ti, e intensifica el abrazo.")
        pausa_larga()
        print("\nCarmilla: ")
        pausa()
        print("\nCarmilla deja salir una risa húmeda en sangre.")
        pausa()
        print("\nSu mirada regresa al altar donde estaba arrodillada.")
        pausa_larga()
        print("\nEn el altar, alcanzas a ver algunas fotografías antiguas de Carmilla rodeada de personas.")
        pausa_larga()
        print("\n'La familia Von Karnstein'.")
        pausa_larga()
        print("Carmilla: Lo lamento...")
        pausa_larga()
        print("\nLa luz se desvanece de tu mirada, y Carmilla deja de respirar en tus brazos.")
        pausa_larga()
        print("\nUna última lágrima recorre su rostro y se une al charco de sangre.")
        pausa_importante()
        print("\nHas matado a Carmilla.")
        pausa()
        print("\nLograste sobrevivir la noche de luna roja y escapar de la mansión.")
        pausa_importante()
        print("\nFinal desbloqueado: Cazadora.")
        pausa()
        print("\nLograste matar a Carmilla y escapar.")
        pausa_importante()
        print("\n¡Fin del juego!\n")
        pausa()
        exit()
    else:
        pausa()
        print("\nCon pánico, tratas de retroceder antes de que te vea.")
        pausa_larga()
        print("Pero al dar un paso atrás, el suelo de madera rechina.")
        pausa_larga()
        print("\nMierda.")
        pausa()
        print("\nCarmilla se levanta, y seca las lágrimas en sus mejillas con rapidez con la manga de su vestido.")
        pausa_importante()
        print("\nDespués de un momento, voltea a verte fijamente.")
        pausa()
        print("\nTratas de moverte, quieres hacerlo, pero tus piernas no te responden.")
        pausa_larga()
        print("\nCarmilla: Aww, la pobrecita humana está temblando de miedo.")
        pausa_larga()
        print("\nCarmilla: Fue un grave error entrar aquí, corazón.")
        pausa_larga()
        print("\nRecibes un golpe y te desvaneces.")
        pausa_larga()
        print("\nTiempo después, gritos y porras te despiertan.")
        pausa()
        print("\nEstas atada a una silla.")
        pausa()
        print("\nA tu alrededor, hay cientos de vampiros mirándote expectantes.")
        pausa_larga()
        print("\nCarmilla: Y ahora para finalizar el ritual... la sangre de la humana.")
        pausa_larga()
        print("\nCarmilla se acerca a ti, y sujeta tu rostro con delicadeza.")
        pausa_larga()
        print("\nCarmilla: No es personal, bonita. Eres solo un ingrediente más.")
        pausa_importante()
        print("\nCarmilla te besa con dulzura en un intento de distraerte del dolor.")
        pausa_larga()
        print("\nLo último que ves es el charco de tu sangre creciendo lentamente, y bañando el resto de los ingredientes del ritual.")
        pausa_importante()
        print("\n¡Has perdido! No lograste sobrevivir la noche de luna roja.")
        pausa_larga()
        print("\n¡Fin del juego!")
        exit()

def pasillo_principal():
    if visited_rooms["pasillo_principal"]:
        print("\n¡Has vuelto al pasillo principal!")
    else:
        print("\n¡Has entrado al pasillo principal!")
        pausa_larga()
    print("\nUn largo pasillo con gruesas alfombras antiguas y retratos polvorientos te presenta tres puertas.")

    while True:   
        opciones_mostradas = {
            "sur": "baile" if visited_rooms["salon_baile"] else "sur (puerta no explorada)",
            "este": "dormitorio" if visited_rooms["habitacion_principal"] else "este (puerta no explorada)",
            "oeste": "comedor" if visited_rooms["comedor"] else "oeste (puerta no explorada)"
        }

        respuesta = ""
        while respuesta not in opciones_mostradas.values():
            print("\n¿A dónde deseas ir?")
            pausa()
            print(f"♥ {opciones_mostradas['sur'].capitalize()}")
            pausa_corta()
            print(f"♥ {opciones_mostradas['este'].capitalize()}")
            pausa_corta()
            print(f"♥ {opciones_mostradas['oeste'].capitalize()}")
            pausa()
            respuesta = input("\nSelecciona tu decisión:  ").strip().lower()

            if respuesta == "sur" or respuesta == "baile":
                posicion_actual = "salon_baile"
                salon_baile()
                return posicion_actual
            elif respuesta == "este" or respuesta == "dormitorio":
                posicion_actual = "habitacion_principal"
                habitacion_principal()
                return posicion_actual
            elif respuesta == "oeste" or respuesta == "comedor":
                posicion_actual = "comedor"
                comedor()
                return posicion_actual
            else:
                print("\n¡Esa no es una puerta! Intenta de nuevo.")

habitacion_principal()