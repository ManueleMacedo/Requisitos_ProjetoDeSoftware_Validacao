class PecaLego:
    def conectar_pino_redondo(self):
        return "Conectado via pino redondo padrão!"

class MotorEstranho:
    def encaixar_entrada_quadrada(self):
        return "Encaixado via entrada quadrada esquisita."

# O ADAPTER: A peça que traduz o quadrado para o redondo
class AdaptadorDeMotor(PecaLego):
    def __init__(self, motor_estranho):
        self.motor_estranho = motor_estranho

    def conectar_pino_redondo(self):
        return self.motor_estranho.encaixar_entrada_quadrada()


motor_ruim = MotorEstranho()
peca_adaptada = AdaptadorDeMotor(motor_ruim)

print(peca_adaptada.conectar_pino_redondo())