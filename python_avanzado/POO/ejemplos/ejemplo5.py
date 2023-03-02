class Pago:
    def __init__(self,saldo):
        self.saldo=saldo
    def pagar(self,pago):
        self.saldo=self.saldo-pago
    def __str__(self):
        return f"Saldo restante {self.saldo}"
    
class Descuento(Pago):
    def __init__(self,saldo,descuento):
        super().__init__(saldo)
        self.descuento=descuento
    def pagar(self,pago):
        self.saldo = self.saldo-(pago-(pago+self.descuento))