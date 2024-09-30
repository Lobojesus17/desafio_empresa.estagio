#questao05


class Lampada:
    def __init__(self):
        self.estado = False 
        self.quente = False  

class SalaDasLampadas:
    def __init__(self):
        self.lampadas = [Lampada() for _ in range(3)]

    def ligar(self, index):
        self.lampadas[index].estado = True
        self.lampadas[index].quente = True  

    def desligar(self, index):
        self.lampadas[index].estado = False

    def verificar_lampadas(self):
        resultado = []
        for lamp in self.lampadas:
            if lamp.estado:
                resultado.append("acesa")
            elif not lamp.estado and lamp.quente:
                resultado.append("desligada e quente")
            else:
                resultado.append("desligada e fria")
        return resultado



sala = SalaDasLampadas()


sala.ligar(0)


sala.desligar(0)
sala.ligar(1)


estado_lampadas = sala.verificar_lampadas()


for i, estado in enumerate(estado_lampadas):
    print(f"Lâmpada {i+1}: {estado}")

