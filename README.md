Pesquisa de Padrões de Projeto (Criacionais)
Este repositório contém exemplos práticos e simples de dois padrões de projeto criacionais feitos em Python. O foco aqui foi entender como organizar a criação de objetos de forma inteligente.

📌 Padrões Implementados
1. Singleton (O "Exclusivo")
O que faz: Garante que uma classe tenha apenas uma única instância no programa inteiro.
Exemplo no código: Criei um GerenciadorConfig. Não importa quantas vezes você tente criar um novo, ele sempre te devolve o mesmo objeto. Isso evita gasto de memória e conflito de dados.

2. Factory Method (O "Fabricante")
O que faz: Tira do código principal a responsabilidade de saber "como" criar um objeto. Você apenas pede o que precisa e a "fábrica" resolve.
Exemplo no código: Um sistema de notificações. Eu peço um "SMS" ou um "Email" para a função fábrica, e ela me entrega o objeto prontinho para usar, sem eu precisar configurar nada manualmente.
