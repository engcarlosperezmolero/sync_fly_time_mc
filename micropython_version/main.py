from machine import Pin
from time    import ticks_ms
from helpers import detectar_saltos, iniciar_access_point

# inicializando variables importantes ===

infra_1 = Pin(25, Pin.IN)
infra_2 = Pin(26, Pin.IN)

estado_anterior_1 = 1
estado_anterior_2 = 1

contador_1 = 0
contador_2 = 0

tiempo_previo = ticks_ms()
tiempo_espera = 5

# iniciando access point para crear red wifi
iniciar_access_point("LETRAMP-TIEMPO-VUELO-1", "123456789")



# estableciendo loop principal
while True:
    try:
        if ticks_ms() - tiempo_previo >= tiempo_espera:
            tiempo_previo = ticks_ms()
            
            estado_anterior_1, contador_1 = detectar_saltos(estado_anterior_1, infra_1, contador_1, "rojo")
            estado_anterior_2, contador_2 = detectar_saltos(estado_anterior_2, infra_2, contador_2, "amarillo")
            
    except:
        break

