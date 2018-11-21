from Cuenta import *
from Cliente import *
from CuentaHija import *
from CuentaCredito import *
from CuentaDeAhorro import *
from MenuUsuario import *
from MenuBanco import *
from Banco import *
#importamos las clases
class Pruebas:
    pass
print ("Desde las pruebas")
print()



cliente_01= Cliente("Hercules",32,"Xochimilco")
Cuenta16 = CuentaCredito(3000,0)
Cuenta17 = CuentaDeAhorro(2000,.05)
Cuenta18 = CuentaCredito(9000,20000)
cliente_01.agregarCuentas(Cuenta16)
cliente_01.agregarCuentas(Cuenta17)
cliente_01.agregarCuentas(Cuenta18)
print(cliente_01)
cliente_01.eliminarCuentas(1)
print(cliente_01)
print("===============================")

banco_1 = Banco("Bansur","Av Aztecas")
cliente1 = Cliente ("Natalia", 24, "Polanco")
cliente2 = Cliente ("Julia", 74, "Magdalena Cont.")
cliente3 = Cliente ("Cassandra", 20, "Sta Ursula")
banco_1.agregarClientes(cliente1)
banco_1.agregarClientes(cliente2)
banco_1.agregarClientes(cliente3)
print(banco_1)
banco_1.eliminarClientes(0)
print(banco_1)
print("==============================")

cliente = Cliente("carlos",22,"Santo Domingo")
Cuenta13 = CuentaCredito(400,800)
Cuenta14 = CuentaDeAhorro(400,.1)
cliente.agregarCuentas(Cuenta13)
cliente.agregarCuentas(Cuenta14)
mu = MenuUsuario ()
mu.MenuCuenta(cliente)
print("===============================")

banco = Banco("Babamex","Polanco")
cliente_18 = Cliente ("George", 64, "ixtapaluca")
cliente_19 = Cliente ("Benji", 58, "Roma")
banco.agregarClientes(cliente_18)
banco.agregarClientes(cliente_19)
Mu = MenuBanco()
while True:
    Mu.MenuBanco(banco)


