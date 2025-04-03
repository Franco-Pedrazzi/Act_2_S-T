class Nodo():
    def __init__(self,nombre):
        self.nombre=nombre
        self.conexiones=[]

    def agregar_conexiones(self,nodo):
        self.conexiones.append(nodo)

    def enviar_mensaje(self,mensaje):
        print(f"{self.nombre} envia: {mensaje}")
        for conexion in self.conexiones:
            conexion.recibir_mensaje(mensaje)

    def recibir_mensaje(self,mensaje):
        print(f"{self.nombre} recibe: {mensaje}")   

    def eliminar_conexion(self,nodo):
        self.conexiones.remove(nodo)
        time.sleep(3)
        print(f"{nodo.nombre} salio del server")

if __name__=="__main__":
    import time

    servidor=Nodo("Servidor")
    cliente1=Nodo("Cliente1")
    cliente2=Nodo("Cliente2")
    cliente3=Nodo("Cliente3")

    servidor.agregar_conexiones(cliente1)
    servidor.agregar_conexiones(cliente2)
    servidor.agregar_conexiones(cliente3)

    cliente1.agregar_conexiones(servidor)
    cliente2.agregar_conexiones(servidor)
    cliente3.agregar_conexiones(servidor)

    servidor.enviar_mensaje("hola a todos")

    print(" ")

    servidor.eliminar_conexion(cliente1)
    servidor.eliminar_conexion(cliente2)
    servidor.eliminar_conexion(cliente3)

    print(" ")

    servidor.agregar_conexiones(cliente1)
    servidor.agregar_conexiones(cliente2)
    servidor.agregar_conexiones(cliente3)

    servidor.enviar_mensaje("hola a todos de nuevo")