Exercício 1: Padrões de Projeto (Criacionais)
Este repositório contém exemplos práticos e simples de dois padrões de projeto criacionais feitos em Python. O foco aqui foi entender como organizar a criação de objetos de forma inteligente.

📌 Padrões Implementados
1. Singleton (O "Exclusivo")
O que faz: Garante que uma classe tenha apenas uma única instância no programa inteiro.
Exemplo no código: Criei um GerenciadorConfig. Não importa quantas vezes você tente criar um novo, ele sempre te devolve o mesmo objeto. Isso evita gasto de memória e conflito de dados.

2. Factory Method (O "Fabricante")
O que faz: Tira do código principal a responsabilidade de saber "como" criar um objeto. Você apenas pede o que precisa e a "fábrica" resolve.
Exemplo no código: Um sistema de notificações. Eu peço um "SMS" ou um "Email" para a função fábrica, e ela me entrega o objeto prontinho para usar, sem eu precisar configurar nada manualmente.

🏗️ Exercício 2: Padrões Estruturais
Este repositório também contém exemplos práticos de dois padrões estruturais. O foco aqui foi entender como montar e conectar objetos de forma que o sistema seja flexível e fácil de manter.

📌 Padrões Implementados
1. Adapter (O "Benjamim")
O que faz: Permite que objetos com interfaces incompatíveis trabalhem juntos, funcionando como um tradutor.
Exemplo no código: Criei um AdaptadorDeMotor. Imagine que você tem uma peça de outra marca que não encaixa no seu Lego; o adaptador faz a ponte entre o encaixe estranho e o pino padrão, permitindo que tudo funcione sem mudar o código original.

2. Facade (A "Fachada")
O que faz: Fornece uma interface simplificada para um sistema complexo, escondendo a bagunça dos bastidores.
Exemplo no código: Criei um ManualFacilCastelo. Em vez de o usuário ter que lidar com várias classes difíceis (motores, sensores, estoque), ele usa apenas um método simples da "Fachada" para realizar uma tarefa completa, deixando o uso muito mais amigável.