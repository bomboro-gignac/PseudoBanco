#elaboró samuel
#14/10/18
from Cuenta import *

class CuentaCredito(Cuenta):
    #def __init__(self,valor) :
    #    Cuenta.__init__(self, valor)
     #   self.__sobregiro = 0
    #No pude encontrar una solucion para sobrecargar el metodo init    
        
    def __init__(self,valor, sobregiro):
        Cuenta.__init__(self, valor)
        self.__sobregiro = sobregiro
        # el banco permite retirar cierta cantidad de dinero a pesar de que sobrepase la cantidad original que tuviera en un inicio  


    def retirar (self,retiro):
        varcantidad = self.getCantidad()
        varetiro = 0
        if retiro >= 0:    
            if retiro <= self.__sobregiro + varcantidad :
                if retiro >= varcantidad:
                    self.__sobregiro = self.__sobregiro + varcantidad - retiro
                
                    print("Cantidad a retirar "+str(retiro))
                    self.setCantidad(0);
                    print ("Nuevo saldo:",self.getCantidad())
                else: 
                    varetiro =  varcantidad - retiro
                    print("Cantidad a retirar: "+str(retiro))
                    self.setCantidad(varetiro);
                    print ("Nuevo saldo:",self.getCantidad())
            else:
                print ("El banco no puede liberarte esa cantidad de dinero") 

        else: 
            print ("tu numero es negativo")
        return
# Se sobreescribe el metodo retirar pues ahora tenemos nuevas condiciones sobre este.  
    
  
    def getSobregiro(self):
        return self.__sobregiro 

    def setSobregiro(self,sobregiro):
        self.sobregiro = sobregiro
        return      

    def __str__( self ):
        tmp = " \n\n===================\n Cuenta credito\n"
        tmp += "Cantidad disponible en la cuenta:" + str( self.getCantidad())
        tmp += "\nSobregiro:" + str( self.__sobregiro)
        return tmp    
    def datos(self):
        return "C,"+str(self.getCantidad())+","+str(self.__sobregiro)
#de igual manera se sobreescribe el metodo str pues tenemo que imprimir un nuevo atributo que es el de sobregiro        