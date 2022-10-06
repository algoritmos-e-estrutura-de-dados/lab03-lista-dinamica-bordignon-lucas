
from node import Node

class Lista:
    inicio = None

    def __init__(self):
        self.inicio = None


    def add(self, value, inicio=False):
        if inicio:
            self.addStart(value)
        else:
            self.addEnd(value)

    def addStart(self, value):
        new = Node(value)
        new.next = self.inicio
        self.inicio = new

    def addEnd(self, value):
        if self.inicio == None:
            self.inicio = Node(value, None)
        else:
            aux = self.inicio
            while aux.next != None:
                aux = aux.next

            aux.next = Node(value, None)
            aux.next.anterior = aux

    def remove(self, value):
        aux = self.inicio
        if aux.value == value:
            # aux.value = None
            self.inicio = aux.next
        else:
            while aux.next != None:
                aux = aux.next
                if aux.value == value:
                    aux.anterior.next = aux.next

    def show(self):
        aux = self.inicio
        print("[", end='')
        while aux.next != None:
            print(f"{aux.value}", end=', ')
            aux = aux.next
        print(f"{aux.value}]")