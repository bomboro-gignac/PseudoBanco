#elaboro samuel 22/010/18

class Cuenta:
    
    def __init__(self, valor):
        self.__cantidad = valor
    
    def depositar(self,valor):
        if valor >= 0:
           self.__cantidad += valor
           print ("Deposito exitoso") 
        else:
           print ("La cantidad es negativa")  
    
    def retirar (self,valor):
      if valor >= 0:
        if valor <= self.__cantidad:
           self.__cantidad = self.__cantidad - valor
           print ("Nuevo saldo",self.__cantidad)
        else:
           print ("saldo insuficiente")
      else: 
        print ("tu numero es negativo")
        
    def __str__( self ):
        tmp = ""
        tmp += "Cantidad::" + str( self.__cantidad)
        return tmp
    
    def consulta(self):
        return self.__cantidad

    """def mostrarDetalles(self):
        print("\n   Detalles cuenta")
        print("\n    Saldo: ",self.__cantidad)"""
        #este metodo fue sustituido por el etodo str

    def setCantidad(self, valor):
        self.__cantidad = valor

    def getCantidad (self):
        return self.__cantidad 
    #decidi poner los metodos setter y getter para el atributo de valor porque
    #pienso que es algo que se puede ir modificando constatemente a lo largo del tiempo"""          
    
         



