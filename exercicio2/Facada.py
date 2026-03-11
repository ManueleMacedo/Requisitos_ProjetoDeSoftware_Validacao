# Subsistemas Complexos
class EstoquePecas:
    def separar_por_cor(self): print("Peças separadas por cor.")

class BracosRoboticos:
    def montar_base(self): print("Base do castelo montada.")
    def colocar_torres(self): print("Torres posicionadas.")

class VerificadorQualidade:
    def checar_estabilidade(self): print("Castelo firme e forte!")

# A FACADE
class ManualFacilCastelo:
    def __init__(self):
        self.estoque = EstoquePecas()
        self.robos = BracosRoboticos()
        self.qualidade = VerificadorQualidade()

    def construir_castelo_completo(self):
        print("--- Iniciando construção rápida ---")
        self.estoque.separar_por_cor()
        self.robos.montar_base()
        self.robos.colocar_torres()
        self.qualidade.checar_estabilidade()
        print("--- Castelo pronto para brincar! ---")

projeto = ManualFacilCastelo()
projeto.construir_castelo_completo()