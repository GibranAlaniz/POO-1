class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.titular=titular
        self.__saldo=saldo
        
    def depositar(self,cantidad):
        if cantidad>0:
            self.__saldo+=cantidad
            return True
        return False
    
    def retirar(self,cantidad):
        if 0<cantidad<=self.__saldo:
            self.__saldo-=cantidad
            return True
        return False
    
    def consultar(self):
        return self.__saldo