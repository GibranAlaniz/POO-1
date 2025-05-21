import threading
import time

class hilo(threading.Thread):
    def __init__(self,nombre,intervalo):
        super().__init__()
        self.nombre=nombre
        self.intervalo=intervalo
            
    def run(self):
        print(f"el hilo {self.nombre} ha comenzado")
        for i in range (5):
            print(f"el hilo {self.nombre} se encuentra en iteracion {i}")
            time.sleep(self.intervalo)
        print(f"{self.nombre} ha finalizado")
            
hilo1=hilo("hilo",2)
hilo2=hilo("hilo",4)
hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()