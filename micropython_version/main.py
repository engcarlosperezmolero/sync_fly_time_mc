from machine import Pin
from time import ticks_ms


infra_1 = Pin(25, Pin.IN)
infra_2 = Pin(26, Pin.IN)

estado_anterior_1 = 1
estado_anterior_2 = 1

contador_1 = 0
contador_2 = 0

tiempo_previo = ticks_ms()
tiempo_espera = 5


def detectar_saltos(estado_anterior, infra, contador, trampolin):
    """
    Detecta cuando el gimnasta aterriza en la lona y cuando despega.
    Si el infrarrojo es 0 esta en la lona, de lo contrario esta en el aire.
    Retorna el estado_anterior actualizado y el contador de saltos.
    """
    if infra.value() == 0 and estado_anterior == 1:
        contador += 1
        print(f"Aterrizo {trampolin}, salto {contador}")
        estado_anterior = 0
    
    if infra.value() == 1 and estado_anterior == 0:
        print(f"Despego {trampolin}, salto {contador}\n")
        estado_anterior = 1
        
    return estado_anterior, contador

        
while True:
    try:
        if ticks_ms() - tiempo_previo >= tiempo_espera:
            tiempo_previo = ticks_ms()
            estado_anterior_1, contador_1 = detectar_saltos(estado_anterior_1, infra_1, contador_1, "rojo")
            estado_anterior_2, contador_2 = detectar_saltos(estado_anterior_2, infra_2, contador_2, "amarillo")
    except:
        break

