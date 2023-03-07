import json

with open("/content/dados.json") as f:
    dados = json.load(f)

menor_valor = dados[0]["valor"]
dia_menor_valor = dados[0]["dia"]

for obj in dados:
    if obj["valor"] < menor_valor and obj["valor"] > 0:
        menor_valor = obj["valor"]
        dia_menor_valor = obj["dia"]

print("O menor valor foi encontrado no dia", dia_menor_valor, "e é:", menor_valor)

maior_valor = dados[0]["valor"]
dia_maior_valor = dados[0]["dia"]

for obj in dados:
    if obj["valor"] > maior_valor:
        maior_valor = obj["valor"]
        dia_maior_valor = obj["dia"]

print("O maior valor foi encontrado no dia", dia_maior_valor, "e é:", maior_valor)

faturamento_diario = [d['valor'] for d in dados]
media_diaria = sum(faturamento_diario) / len(faturamento_diario)

dias_acima_media = 0
for d in dados:
    if d['valor'] > media_diaria:
        dias_acima_media += 1

print('Número de dias em que o faturamento diário foi superior à média diária:', dias_acima_media)