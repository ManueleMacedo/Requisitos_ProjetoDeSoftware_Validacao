class NotificacaoEmail:
    def enviar(self):
        return "Enviando E-mail: 'Ola, sua conta chegou!'"

class NotificacaoSMS:
    def enviar(self):
        return "Enviando SMS: 'Seu codigo e 1234'"

# Essa é a nossa Fábrica
def fabrica_de_notificacoes(tipo):
    if tipo == "email":
        return NotificacaoEmail()
    elif tipo == "sms":
        return NotificacaoSMS()


servico = fabrica_de_notificacoes("sms")
print(servico.enviar())