#elaboro samuel 22/010/18

class Banco:
#En esta clase es donde convergen todos nuestros metodos    
    def __init__(self,nombre,ubicacion,cliente):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__cliente = cliente
    #metodo constructor


    def __str__( self ):
        tmp = ""
        tmp += "Nombre del Banco::" + str( self.__nombre)
        tmp += "\nUbicacion::" + str( self.__ubicacion)
        tmp += "\nCliente::" + str( self.__cliente)
        
        return tmp   

   # metodo str que imprime nuetros atributos del objeto          
