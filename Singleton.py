class GerenciadorConfig:
    _instancia = None

    def __new__(cls):
        # Se ainda não existe uma instância, eu crio uma
        if cls._instancia is None:
            cls._instancia = super(GerenciadorConfig, cls).__new__(cls)
            cls._instancia.tema = "Escuro"
        
        # Se já existe, eu só devolvo a que já estava pronta
        return cls._instancia


config1 = GerenciadorConfig()
config2 = GerenciadorConfig()

print(config1.tema) 


config2.tema = "Claro"


print(config1.tema) 
print(config1 is config2) 