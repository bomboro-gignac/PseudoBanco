from Cuenta import *
from Cliente import *
from CuentaHija import *
from CuentaCredito import *
from CuentaDeAhorro import *
#importamos las clases
class Pruebas:
    pass
print ("Desde las pruebas")
print()
"""Cuenta1 = Cuenta(300)
print()
print (Cuenta1.consulta())
Cuenta1.depositar(330)
Cuenta1.retirar(1000)
print (Cuenta1.consulta())

print()

Cuenta2 = Cuenta(4000)
print (Cuenta2)

Cuenta2.setCantidad(200)
print(Cuenta2)
print()

Cuenta3 = CuentaHija(2000, "credito" )
print(Cuenta3)
Cuenta3.depositar(330)
Cuenta3.retirar(10000)

print()

Cliente1 = Cliente ("Juan", 34, "coyoacan", Cuenta1)

Cliente1.setdireccion("Xochimilco")
Cliente2 = Cliente ("Tommy",23,"tlalpan", Cuenta2)
print(Cliente1)
Cliente2.setedad(45)
print()

print(Cliente2)

print()
Cuenta8 = CuentaCredito(200,1000)
Cuenta8.retirar(1300)

print()

print(Cuenta8)
a = Cuenta8.getSobregiro()
print(a)

Cliente9 = Cliente ("pepe", 36, "coyoacan", Cuenta8)

print()

print(Cliente9)


Cuenta9 = CuentaDeAhorro(200,.02)
Cliente10 = Cliente ("Aldo", 39, "Sta ursula", Cuenta9)
print()

print(Cliente10)

print()
Cuenta10 = CuentaCredito(300,3000)
Cuenta10.retirar(200)
print(Cuenta10)

print()
Cuenta11 = CuentaCredito(400,3000)
Cuenta11.retirar(400)
print(Cuenta11)

print()

Cuenta12 = CuentaCredito(500,2000)
Cuenta12.retirar(600)
print(Cuenta12)"""

Cuenta13 = CuentaCredito(400,800)

Cuenta14 = CuentaDeAhorro(400,.1)
Cliente1 = Cliente ("Juan", 34, "coyoacan")
Cliente1.agregarCuentas(Cuenta13)
Cliente1.agregarCuentas(Cuenta14)
print(Cliente1)