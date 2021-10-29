class NodoArbol(object):
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None
        self.altura = 1

class ArbolAVL(object):
    def insertar(self, raiz, key):
        if not raiz:
            return NodoArbol(key)
        elif key < raiz.valor:
            raiz.left = self.insertar(raiz.left, key)
        else:
            raiz.right = self.insertar(raiz.right, key)
        raiz.altura = 1 + max(self.getAltura(raiz.left), self.getAltura(raiz.right))
        b = self.getBalance(raiz)

        if b > 1 and key < raiz.left.valor:
            return self.rightRotar(raiz)

        if b < -1 and key > raiz.right.valor:
            return self.leftRotar(raiz)

        if b > 1 and key > raiz.left.valor:
            raiz.left = self.leftRotar(raiz.left)
            return self.rightRotar(raiz)

        if b < -1 and key < raiz.right.valor:
            raiz.right = self.rightRotar(raiz.right)
            return self.leftRotar(raiz)

        return raiz



    def leftRotar(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.altura = 1 + max(self.getAltura(z.left), self.getAltura(z.right))
        y.altura = 1 + max(self.getAltura(y.left), self.getAltura(y.right))

        return y

    def rightRotar(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.altura = 1 + max(self.getAltura(z.left), self.getAltura(z.right))
        y.altura = 1 + max(self.getAltura(y.left), self.getAltura(y.right))

        return y

    def getAltura(self, raiz):
        if not raiz:
            return 0
        return raiz.altura

    def getBalance(self, raiz):
        if not raiz:
            return 0
        return self.getAltura(raiz.left) - self.getAltura(raiz.right)

    def preOrden(self, raiz):
        if not raiz:
            return
        print("{0} ".format(raiz.valor), end="")
        self.preOrden(raiz.left)
        self.preOrden(raiz.right)

Arbol = ArbolAVL()
raiz = None
raiz = Arbol.insertar(raiz, 1)
raiz = Arbol.insertar(raiz, 2)
raiz = Arbol.insertar(raiz, 3)
raiz = Arbol.insertar(raiz, 4)
raiz = Arbol.insertar(raiz, 5)
raiz = Arbol.insertar(raiz, 6)

print("Recorrido Transversal PreOrden del Arbol AVL es: ")
Arbol.preOrden(raiz)
print()