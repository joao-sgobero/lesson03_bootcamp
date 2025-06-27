### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

qtd = float(input("Digite a quantidade: "))
preco = float(input("Digite o preço: "))

if qtd > 0 and preco > 0:
    print("Dados válidos")
else:
    print("Dados inválidos")


### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

temperatura = 22

if temperatura < 18:
    print("Temperatura está baixa.")
elif temperatura >= 18 and temperatura <= 26:
    print("Temperatura está normal")
else:
    print("A temperatura está elevada")

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

log = {
    'timestamp': '2021-06-23 10:00:00',
    'level': 'ERROR',
    'message': 'Falha na conexão'
}

if log['level'] == 'ERROR':
    print(log['message'])

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

idade_usuario = 28
email = "joao.sgobero@gmail.com"

if idade_usuario < 18 or idade_usuario > 65:
    print("Sua idade está fora das diretrizes da empresa.")
elif "@" not in email:
    print("O email é invalido pois não contem '@'.")
elif "." not in email:
    print("O email é invalido pois não contem '.'.")
else:
    print("Os dados são válidos")


### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

transacao = {'valor': 12000, 'hora': 20}

if transacao['valor'] > 10000 or (transacao['hora'] < 9 or transacao['hora'] > 18):
    print("Essa transação é suspeita")
else:
    print("Transação aprovada.")


### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto_sujo = "Olá, mundo! O mundo é belo. Belo, belo mundo."
print(f"Texto original: {texto_sujo}")

#Limpeza e Preparação de Dados
texto_quase_limpo = texto_sujo.lower()
pontuacoes_a_remover = ",.!?;:"

for pontuacao in pontuacoes_a_remover:
    # ...substitua essa pontuação por nada no nosso texto.
    texto_quase_limpo = texto_quase_limpo.replace(pontuacao, "")

texto_limpo = texto_quase_limpo
print(f"Texto limpo: {texto_limpo}")

#Quebrar o texto limpo em palavras
lista_de_palavras = texto_limpo.split()

#Preparar o "contador
contagem_palavras = {}

#O Loop de Contagem (permanece exatamente o mesmo!)
for palavra in lista_de_palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

#Apresentar o resultado
print("\nContagem final de palavras (versão 2.0):")
print(contagem_palavras)

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

numeros = [10, 20, 30, 40, 50]
minimo = min(numeros)  # 10
maximo = max(numeros)  # 50

normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]
print(normalizados)


### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

usuarios = [
    {"nome": "Ana", "idade": 25, "email": "ana@email.com"},
    {"nome": "Bruno", "idade": 30},
    {"nome": "Carla", "idade": 28, "email": "carla@email.com"},
    {"nome": "Diego"},
]

campo = "email"

usuarios_com_campo_faltando = []

for usuario in usuarios:
    #Verifica se o campo está ausente
    if campo not in usuario:
        usuarios_com_campo_faltando.append(usuario)

print(usuarios_com_campo_faltando)

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.