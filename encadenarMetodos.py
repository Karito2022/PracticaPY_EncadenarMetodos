class Usuario:
    # Atributos de clase - Definidos en clase
    bank_name = "Banco Dojo"
    # Metodo"__init__"
    def __init__(self, name):
        self.name = name
        self.amount = 0 
    # Metodo "hacer deposito"
    def hacer_deposito(self, amount):
        self.amount += amount
        return self
    # Metodo "hacer retiro"
    def hacer_retiro(self, amount):
        self.amount -= amount
        return self
    # Metodo "mostrar el balance de usuario"
    def mostrar_balance_usuario(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self
    # Metodo "transferir dinero"
    def transferir_dinero(self, usuario, amount):
        self.amount -= amount
        usuario.amount += amount
        self.mostrar_balance_usuario()
        usuario.mostrar_balance_usuario()
        return self

#Crear 3 instancias de la clase Usuario
vizcarra = Usuario("Martin Vizcarra")
toledo = Usuario("Alejandro Toledo")
fujimori = Usuario("Keiko Fujimori")

vizcarra.hacer_deposito(8000).hacer_deposito(4400).hacer_deposito(5500).hacer_retiro(1800).mostrar_balance_usuario()
toledo.hacer_deposito(50000).hacer_deposito(1000).hacer_retiro(100).hacer_retiro(1800).mostrar_balance_usuario()
fujimori.hacer_deposito(10500).hacer_retiro(1200).hacer_retiro(3000).hacer_retiro(185).mostrar_balance_usuario()

# BONUS - Transferir dinero
vizcarra.transferir_dinero(fujimori, 1100)