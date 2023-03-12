import json

def calcula_faturamento(vetor_faturamento):
    # Filtra apenas os dias em que o valor é maior que 0
    vetor_faturamento_filtrado = [valor for valor in vetor_faturamento if valor['valor'] > 0]
    
    # Calcula as informações solicitadas
    menor_valor = min(vetor_faturamento_filtrado, key=lambda x: x['valor'])['valor']
    maior_valor = max(vetor_faturamento_filtrado, key=lambda x: x['valor'])['valor']
    soma = sum(valor['valor'] for valor in vetor_faturamento_filtrado)
    media = soma / len(vetor_faturamento_filtrado)
    dias_acima_da_media = sum(valor['valor'] > media for valor in vetor_faturamento_filtrado)
    
    return menor_valor, maior_valor, dias_acima_da_media

# Carrega a lista de faturamento a partir do arquivo JSON
with open('dados.json') as f:
    lista_faturamento = json.load(f)

# Ordena a lista de faturamento por valor de faturamento diário
lista_faturamento_ordenada = sorted(lista_faturamento, key=lambda x: x['valor'])

# Calcula as informações solicitadas
menor_valor, maior_valor, dias_acima_da_media = calcula_faturamento(lista_faturamento_ordenada)

# Imprime os resultados
print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Dias acima da média: {dias_acima_da_media}")
