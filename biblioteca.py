class ContaBancaria():
    def __init__(self, numero, nome, tipo):
        self.nome = nome
        self.numero = numero
        self.tipo = tipo
        self.saldo=0
        self.status = False
        self.limite=0

    def AtivarConta(self):
        if self.status == False:
            print ("Conta Ativada")
            self.status=True
        else:
            print ("A conta já está ativa")
    def Depositar(self,deposito):
        if self.status == False:
            print ("A conta não está ativa")
        else:
            self.saldo += deposito
            print(f" O valor do deposito é {deposito}")
    def VerificarSaldo(self):
        if self.status == False:
            print ("A conta não está ativa")
        else:
            print(f"O seu saldo é {self.saldo}")
    def Sacar(self,saque):
        if self.status == False:
            print ("A conta não está ativa")
        else:
            soma=0
            soma=self.saldo+self.limite
            print(soma,self.saldo)
            if soma < saque:
                print("Valor Indisponivel")
            else:
                self.saldo -= saque
                print (f"Você sacou {saque} ")

    def AjustarLimite(self,limite):
        if self.status ==False:
            print ("A conta não está ativa")
        else:
            self.limite=limite
            print("Limite ajustado")


