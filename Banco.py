#elaboro samuel 22/010/18
#En esta clase es donde convergen todos nuestros metodos 
class Banco:
   #metodo constructor
    def __init__(self,nombre,ubicacion):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.clientes = []
    

#metodo que imprime los datos del banco
    def __str__( self ):
        tmp = ""
        tmp += "Nombre del Banco::" + str( self.__nombre)
        tmp += "\nUbicacion::" + str( self.__ubicacion)
        tmp += "\n" +self.banctes()
        
        return tmp
#metodo que agrega un cliente
    def agregarClientes(self,cliente):
        self.clientes.append(cliente)

#metodo que elimina un cliente
    def eliminarClientes(self,cliente):
        del self.clientes[cliente]
#metodo que accede a un cliente del banco
    def getCliente(self,index):
        return self.clientes[index]
#metodo que imprime un cliente
    def banctes( self ):
        straux = ""
        for i in range( len(self.clientes)):
            straux = straux + "cliente:"+ str(i) +"\n"+ str(self.clientes[i]  )  
        return straux
    
    
    
    
    #for i in self.clientes
     #   print(i)
               

   # metodo str que imprime nuetros atributos del objeto          
