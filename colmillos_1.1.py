import time 
import random 
import colorama 
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

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
    "vestidor": True,
    "bathroom": True,
    "libreria_personal": False,
    "sala_reliquias": False,
    "sala_trofeos": False,
    "pasillo_principal": True,
    "salon_baile": False,
    "salon_ceremonia": False,
    "comedor": False,
    "puerta_principal": False
}

objetos_recogidos = {
    "vestido": True,
    "maquillaje": False,
    "libro_encantado": True,
    "daga_plateada": True,
    "celular": False,
    "velas": True,
    "llave": False,
    "mantel": True,
}

### Funciones place-holder para avanzar 

def sala_reliquias():
    print("Estás en la sala de reliquias.")
    return "sala_reliquias" 

def sala_trofeos():
    print("Estás en la sala de trofeos.")
    return "sala_trofeos"  

def comedor():
    print("Estás en el comedor.")
    return "comedor" 

def puerta_principal():
    print("Has encontrado la puerta principal.")
    return "puerta_principal"  

def salon_baile():
    print("Estás en el salón de baile.")
    return "salon_baile" 

def salon_ceremonia():
    print("Has encontrado el salón de ceremonias.") 

def pasillo_principal():
    print("Has encontrado el pasillo principal.")


### Funciones completas 

def vestidor():
    if visited_rooms["vestidor"]: ## Si ya entraste a esta habitación
        print(Fore.YELLOW + "\nHas vuelto al vestidor. Ya estuviste aquí antes.\n")
        if objetos_recogidos.get("vestido"):
            pausa()
            print("Por cierto, ¡el vestido te queda lindo!")
            pausa()
            if objetos_recogidos.get("libro_encantado") and objetos_recogidos.get("vestido") and not objetos_recogidos.get("maquillaje"):
                pausa_importante()
                print(Fore.LIGHTMAGENTA_EX + "\nYa tienes un vestido antiguo...")
                pausa()
                print(Fore.LIGHTMAGENTA_EX + "Tal vez necesitas algo más para completar tu disfraz...\n")
                pausa()
            elif objetos_recogidos.get("libro_encantado") and objetos_recogidos.get("vestido") and objetos_recogidos.get("maquillaje"):
                pausa()
                print(Fore.LIGHTMAGENTA_EX + "\nUn vestido antiguo y maquillaje pálido...")
                pausa()
                print(Fore.LIGHTMAGENTA_EX + "¡Luces como toda una vampira!\n")
                pausa()

        opciones_mostradas = {
            "sur": "Dormitorio" if visited_rooms["habitacion_principal"] else "sur (puerta no explorada)",
            "oeste": "Baño" if visited_rooms["bathroom"] else "oeste"
        }

        print(Style.BRIGHT + "\n¿A dónde deseas ir?")
        pausa()
        print(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX} ♥ {opciones_mostradas['sur'].capitalize()}")
        pausa_corta()
        print(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX} ♥ {opciones_mostradas['oeste'].capitalize()}")
    
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
                print(Back.RED + "\n¡Esa no es una puerta! Intenta de nuevo.")
        return posicion_actual

    # Primer ingreso a la habitación
    print(Style.BRIGHT + "\n¡Has entrado al vestidor de Carmilla!")
    visited_rooms["vestidor"] = True
    pausa()
    print("\nVes cientos de hermosos y antiguos vestidos de gala colgando ordenadamente.")
    pausa()

    if objetos_recogidos.get("libro_encantado"):
        print(Fore.LIGHTMAGENTA_EX + "\n...Un vestido antiguo podría ser útil como disfraz para pasar desapercibida.")
        pausa_larga()

    while True:
        print(Style.BRIGHT + "\n¿Quieres tomar uno?")
        pausa()
        respuesta = input(Style.NORMAL + "\nDecide (sí/no): ").strip().lower()
        if respuesta == "sí":
            pausa()
            print(Style.NORMAL + "\n¡Has tomado un vestido!")
            objetos_recogidos["vestido"] = True
            pausa()
            if objetos_recogidos.get("libro_encantado"):
                print(Fore.LIGHTMAGENTA_EX + "\nYa tienes un vestido antiguo...")
                pausa()
                print(Fore.LIGHTMAGENTA_EX + "Tal vez necesitas algo más para completar tu disfraz...\n")
                pausa()
            break

        elif respuesta == "no":
            print(Style.NORMAL + "\nDecides no tomar ningún vestido.\n")
            pausa()
            print(Fore.LIGHTMAGENTA_EX + "Necesitas una estrategia para sobrevivir, sigue explorando...\n")
            pausa_larga()
            break

        else:
            print(Style.NORMAL + Back.RED + "\nRespuesta inválida. Intenta de nuevo.")

    
        ###Diccionario de opciones para personalizarlas según historial de exploración del jugador

    opciones_mostradas = {
        "sur": "Dormitorio" if visited_rooms["habitacion_principal"] else "sur (puerta no explorada)",
        "oeste": "Baño" if visited_rooms["bathroom"] else "oeste"
    }

    print(Style.BRIGHT + "\n¿A dónde deseas ir?")
    pausa()
    print(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX} ♥ {opciones_mostradas['sur'].capitalize()}")
    pausa_corta()
    print(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX} ♥ {opciones_mostradas['oeste'].capitalize()}")
   
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
            print(Back.RED + "\n¡Esa no es una puerta! Intenta de nuevo.")
    return posicion_actual


def libreria_personal():
    posicion_actual = libreria_personal
    if visited_rooms["libreria_personal"]: ## Si ya entraste a esta habitación
        print(Fore.YELLOW + "\nHas vuelto a la librería de Carmilla. Ya estuviste aquí antes.")
        if objetos_recogidos["libro_encantado"]:
            pausa_larga()
            print(Fore.MAGENTA + "\nDeberías considerar lo que aprendiste del libro...\n")
    else:
        print(Style.BRIGHT + "\nHas entrado a la librería personal.")
        pausa_larga()
        print("\nEstanterías imponentes se alzan a lo largo de todas las paredes, envolviendo la habitación por completo.")
        pausa_importante()
        print("\nAl centro de la habitación observas un libro peculiar con páginas que emiten luz.")
        pausa_importante()
        print(Style.BRIGHT + Fore.RED + "\n'El ritual de la Luna Roja'")
        pausa()
        print("lee el título de la página en tinta bermellón.")
        pausa_importante()
        print("\nRápidamente escanéas las páginas del libro, y descubres que se trata de un hechizo peculiar.")
        pausa_larga()
        print("\nDeseosa de obtener más información que te ayude a escapar, sigues leyendo.")
        pausa_larga()
        print(Style.BRIGHT + "\n'...Aquel que reúna los ingredientes necesarios en la noche de luna roja, obtendra la Bendición Diurna.'")
        pausa_importante()
        print(Style.BRIGHT + Fore.YELLOW +"Bendición Diurna: Hechizo que le otorga a un vampiro la habilidad de existir bajo el sol, libre del daño de sus rayos.")
        pausa_importante()
        print(Style.BRIGHT + "\nAquella hija de la luna que desee diambular bajo el sol deberá reunir los ingredientes necesarios en la noche de la luna roja.")
        pausa_importante()
        print("\n...En ese momento te das cuenta de que no has encontrado ni una sola ventana en toda la mansión.")
        pausa_importante()
        print(Style.BRIGHT + "\nIngredientes:")
        pausa()
        print(Style.BRIGHT + "•Media docena de lirios blancos.")
        pausa()
        print(Style.BRIGHT + "•Tres gotas de agua de la fuente de la vitalidad.")
        pausa()
        print(Style.BRIGHT + "•Una docena de colmillos de murciélago.")
        pausa()
        print(Style.BRIGHT + "•Mantel de pelaje de licántropo.")
        pausa()
        print(Style.BRIGHT + "•Velas de fuego rojizo.")
        pausa()
        print(Style.BRIGHT + "•Daga plateada envuelta en seda.")
        pausa_importante()
        print(Style.BRIGHT + "\nPara completar el ritual, es necesario bañar los objetos...")
        pausa_importante()
        print(Style.BRIGHT + Fore.RED + "...en la sangre de un humano adulto de corazón puro, durante las doce campanadas de media noche.")
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

    print(Style.BRIGHT + "\n¿A dónde deseas ir?")
    pausa()
    print(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX} ♥ {opciones_mostradas['sur'].capitalize()}")
    pausa_corta()
    print(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX} ♥ {opciones_mostradas['oeste'].capitalize()}")
   
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
            print(Back.RED + "\n¡Esa no es una puerta! Intenta de nuevo.")
    return posicion_actual
    
    
def habitacion_principal():
    posicion_actual = habitacion_principal
    if visited_rooms["habitacion_principal"]: ## Si ya entraste a esta habitación
        print(Fore.YELLOW + "\nHas vuelto a la habitación de Carmilla. Aquí es donde iniciaste.")
        if objetos_recogidos["libro_encantado"]:
            pausa_larga()
            print(Fore.LIGHTMAGENTA_EX + "\nDeberías considerar lo que aprendiste del libro... Explora la mansión y busca una forma de escapar.\n")
    else:
        print("\nDespiertas con un dolor de cabeza palpitante y la garganta seca.")
        pausa_larga()
        print("\nEntre gruñidos, te estiras y tratas de recordar qué sucedió anoche.")
        pausa()
        print("\nLos recuerdos son borrosos...")
        pausa()
        print("\nCon esfuerzo, recuerdas haber salido de fiesta con tus amigas a celebrar tu promoción en el trabajo.")
        pausa_importante()
        print(Fore.BLUE + "\n¿Qué hora es?\n")
        pausa_media()
        print(".")
        pausa_media()
        print(".")
        pausa_media()
        print(".")
        pausa_importante()
        print(Fore.BLUE + "\n¿Dónde está mi celular?")
        pausa_larga()
        print("\nTe tallas los ojos para despertar mejor y buscarlo.")
        pausa()
        print("\nMiras alrededor... y no reconoces nada.")
        pausa_importante()
        print(Fore.BLUE + "\n¿EN DÓNDE ESTOY?")
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

    print(Style.BRIGHT + "\n¿A dónde deseas ir?")
    pausa()
    print(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX} ♥ {opciones_mostradas['norte'].capitalize()}")
    pausa_corta()
    print(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX} ♥ {opciones_mostradas['este'].capitalize()}")
    pausa_corta()
    print(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX} ♥ {opciones_mostradas['oeste'].capitalize()}")

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
            print(Back.RED + "\n¡Esa no es una puerta! Intenta de nuevo.")
    return posicion_actual


def bathroom():
    if visited_rooms["bathroom"]:
        pausa_corta()
        print(Fore.YELLOW + "\nHas vuelto al baño. Ya estuviste aquí antes.\n")
        if objetos_recogidos.get("vestido") and objetos_recogidos.get("maquillaje") and objetos_recogidos.get("libro_encantado"):
            pausa()
            print(Fore.LIGHTMAGENTA_EX + "Un vestido antiguo y maquillaje pálido...")
            pausa()
            print(Fore.LIGHTMAGENTA_EX + "¡Luces como toda una vampira!\n")
            pausa_corta()
            print(Fore.LIGHTMAGENTA_EX + "\n.")
            pausa_corta()
            print(Fore.LIGHTMAGENTA_EX + "\n.")
            pausa_corta()
            print(Fore.LIGHTMAGENTA_EX + "\n.")
            pausa_importante()
            print(Fore.LIGHTMAGENTA_EX + "\n¿En dónde se reunirán los vampiros...?")
            pausa_importante()
        elif objetos_recogidos.get("vestido") and objetos_recogidos.get("maquillaje"):
            pausa()
            print(Fore.LIGHTMAGENTA_EX + "Un vestido antiguo y maquillaje pálido...")
            print(Fore.LIGHTMAGENTA_EX + "¡Luces como toda una vampira!\n")
            pausa()
        else:
            pausa()
            print("No hay mucho que hacer aquí...")
    else:
        pausa()
        print(Style.BRIGHT + "\n¡Has entrado al baño de la recámara!")
        pausa()
        print("\nLa decoración es anticuada, con una tina de gran tamaño y un bello tocador.")
        pausa_larga()
        print(Fore.RED + "\nNotas que no hay ningún un espejo en la habitación.")
        pausa_importante()
        print("\nAbres los cajones del tocador y encuentras maquillaje de un tono preocupántemente pálido.")
        pausa_larga()
        print(Fore.BLUE + "\n¿Cómo se maquilla si no tiene espejos...?")
        pausa_larga()
        if objetos_recogidos.get("libro_encantado") and objetos_recogidos.get("vestido"):
            print(Fore.LIGHTMAGENTA_EX + "\nMaquillaje podría ayudarte a completar tu disfraz...")
            pausa_larga()

        while True:
            print(Style.BRIGHT + "\n¿Quieres maquillarte?")
            pausa()
            respuesta = input(Style.NORMAL + "\nDecide (sí/no): ").strip().lower()
            if respuesta == "sí":
                pausa()
                print(Style.NORMAL + "\n¡Te has maquillado!")
                pausa()
                print("\n...Por lo menos lo mejor posible sin espejos.")
                objetos_recogidos["maquillaje"] = True
                pausa()
                if objetos_recogidos.get("libro_encantado"):
                    print(Fore.LIGHTMAGENTA_EX + "\n¡Tu disfraz está completo!")
                    pausa_importante()
                    print(Fore.BLUE + "\nMe pregunto en dónde se reunirán los vampiros...")
                    pausa_larga()
                break
            elif respuesta == "no":
                print(Style.NORMAL + "\nDecides no maquillarte.\n")
                pausa()
                print(Fore.LIGHTMAGENTA_EX + "Necesitas una estrategia para sobrevivir, sigue explorando...\n")
                pausa_larga()
                break
            else:
                print(Style.NORMAL + Back.RED + "\nRespuesta inválida. Intenta de nuevo.")

        visited_rooms["bathroom"] = True

    while True:
        opciones_mostradas = {
            "este": "Vestidor" if visited_rooms["vestidor"] else "este (puerta no explorada)",
            "esperar": "Esperar" if visited_rooms["bathroom"] else "esperar"
        }

        respuesta = ""
        while respuesta not in opciones_mostradas.values():
            print(Style.BRIGHT + "\n¿A dónde deseas ir?")
            pausa()
            print(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX} ♥ {opciones_mostradas['este'].capitalize()}")
            pausa_corta()
            print(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX} ♥ {opciones_mostradas['esperar'].capitalize()}")
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
                print(Back.RED + "\n¡Esa no es una puerta! Intenta de nuevo.")

def sala_reliquias():
    if visited_rooms["sala_reliquias"]: ### Si ya entraste en la habitación. 
        print(Fore.YELLOW + "\nHas vuelto al la sala de reliquias. Ya estuviste aquí antes.")
        if objetos_recogidos.get("daga_plateada") and not objetos_recogidos.get("velas") and not objetos_recogidos.get("mantel"):
            pausa()
            print("\nLa daga plateada que sujetas pesa, y tiene un filo aterrador.")
            pausa_importante()
            print(Fore.BLUE + "\nLos vampiros no son inmunes a la plata...")
            pausa_importante()
            print(Fore.LIGHTMAGENTA_EX + "\nTienes la ventaja del elemento sorpresa,")
            pausa()
            print(Fore.LIGHTMAGENTA_EX + "Carmilla no sabe que estás armada.")
            pausa_importante()
            print("\nConsideras tus opciones y la posibilidad de un escape sin violencia...")
            pausa_importante()
            print("\nAprietas tu agarre en la daga.")
            pausa_importante()
            print(Style.BRIGHT + Fore.BLUE + "\n¿Dónde estás Carmilla?\n")
        elif objetos_recogidos.get("daga_plateada") and objetos_recogidos.get("mantel") and objetos_recogidos.get("velas"):
            pausa_importante()
            print(Fore.LIGHTMAGENTA_EX + "\nUn mantel, velas, una daga...")
            pausa_larga()
            print(Fore.LIGHTMAGENTA_EX + "¿No eran esos los elementos para el ritual?\n")
            pausa_importante()
            print(Fore.BLUE + "Me pregunto si Carmilla podrá hacer el hechizo sin sus ingredientes...")
            pausa()
        elif objetos_recogidos.get("daga_plateada") and (objetos_recogidos.get("mantel") or objetos_recogidos.get("velas")):
            pausa()
            print(Fore.LIGHTMAGENTA_EX + "\nEstás cerca de un escape pacífico...")
            pausa()
            print(Fore.LIGHTMAGENTA_EX + "Solo un elemento más...\n")
            pausa()
            print(Fore.BLUE +"\n.")
            pausa_corta()
            print(Fore.BLUE +"\n.")
            pausa_corta()
            print(Fore.BLUE +"\n.")
            pausa_importante()
            print(Fore.BLUE + "\n¿Cuáles eran los ingredientes del ritual?")
            pausa()
        return
    else:
        pausa()
        print(Style.BRIGHT + "\n¡Has entrado al salón de reliquias!")
        visited_rooms["sala_reliquias"]=True 
        pausa()
        print("\nUn escalofrío recorre tu espalda al cruzar el umbral.")
        pausa_importante()
        print("\nEl centro de la sala tiene altos pilares con objetos dentro de vitrinas.")
        pausa_importante()
        print(Fore.LIGHTMAGENTA_EX + "\nParece... una colección.")
        pausa()
        print(Style.BRIGHT + "\n'Reliquias de la luna'")
        pausa()
        print("Lee la inscripción a la entrada de la exposición.")
        pausa_larga()
        print("\nTe das una vuelta por la sala y observas los")
        pausa()
        print("diversos objetos de aspecto curioso que captan tu atención.")
        pausa_larga()
        print("\nLa sala está repleta de más riquezas de las que podrías imaginar.")
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
        print(Fore.BLUE + "\n¿Por qué está separado del resto de reliquias?")
        pausa_importante()
        print("\nTocas con delicadeza la cerradura del cofre...")
        pausa_larga()
        if objetos_recogidos.get("llave"):
            print(Fore.BLUE + "\n¿Podría ser...?")
            pausa_larga()
            print("\nMetes la mano a tu bolsillo y tomas la llave que encontraste.")
            pausa_larga()
            print("\nTratas de insertarla en la cerradura...")
            pausa_importante()
            print("\n. . .")
            pausa_importante()
            print(Style.BRIGHT + "\n¡Y logras abrir el cofre!")
            pausa_importante()
            print("\nMiras adentro, y pierdes el aliento.")
            pausa_importante()
            print("\nDentro del cofre hay una daga de plata con rubíes en la empuñadura.")
            pausa_larga()
            print("\nDudas por un momento, pero inhalas con profundidad y tomas la daga del cofre.")
            pausa_importante()
            print(Fore.RED + "\nAhora tienes con qué defenderte...")
            pausa_importante()
            if objetos_recogidos.get("mantel") and objetos_recogidos.get("velas"):
                print(Fore.LIGHTMAGENTA_EX + "\nUn mantel, velas, una daga...")
                pausa_larga()
                print(Fore.LIGHTMAGENTA_EX + "\n¿No eran esos los elementos para el ritual?\n")
                pausa_larga()
            elif objetos_recogidos.get("mantel") or objetos_recogidos.get("velas"):
        elif not objetos_recogidos.get("llave"):
            print("\nTratas de abrirlo, pero es inútil. Está cerrado.")
            pausa_larga()
            print(Fore.LIGHTMAGENTA_EX + "\nLa llave debe estar en algún lado...\n")

sala_reliquias()