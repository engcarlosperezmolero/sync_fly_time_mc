from machine      import Pin
from time         import ticks_ms
from helpers      import detectar_saltos, iniciar_access_point
import usocket


# inicializando variables importantes

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

sock_server = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
sock_server.bind(('192.168.4.1', 8197))
sock_server.listen(3)



# estableciendo loop principal
while True:
    try:
        sc, addr = sock_server.accept()
        print(f"direccion = {addr}")
        while True:
            mensaje = sc.recv(64)
            print(mensaje)
            if not mensaje:
                break
        sc.close()
            
        
        if ticks_ms() - tiempo_previo >= tiempo_espera:
            tiempo_previo = ticks_ms()
            
            estado_anterior_1, contador_1 = detectar_saltos(estado_anterior_1, infra_1, contador_1, "rojo")
            estado_anterior_2, contador_2 = detectar_saltos(estado_anterior_2, infra_2, contador_2, "amarillo")
            
    except:
        sock_server.close()
        print("conexion finalizada ")
        break
