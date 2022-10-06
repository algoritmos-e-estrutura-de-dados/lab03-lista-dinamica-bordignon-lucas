
from lista import Lista

lista = Lista()

lista.add(1)
lista.add(2, inicio=True)
lista.add(3)
lista.add(4, inicio=True)
lista.add(5)
lista.add(6)
lista.add(7, inicio=True)
lista.add(8)
lista.add(9, inicio=True)

lista.show()

lista.remove(3)
lista.remove(8)
lista.remove(6)

lista.show()
