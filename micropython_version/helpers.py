"""Helper functions"""
import network as nw

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


def iniciar_access_point(ssid, password):
    """
    Inicia un access point en el esp32    
    """
    ap = nw.WLAN(nw.AP_IF)
    ap.active(True)
    ap.config(essid=ssid)
    ap.config(authmode=3, password=password)
    while not ap.active():
        pass
    print(f"Configuracion red: {ap.ifconfig()}")