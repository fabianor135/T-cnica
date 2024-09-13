import json


def carregar_dados_faturamento(arquivo):
    with open(arquivo, 'r') as f:
        dados = json.load(f)
    return dados['faturamento_diario']


def analisar_faturamento(dados_faturamento):
    faturamentos = [dia['faturamento']
                    for dia in dados_faturamento if dia['faturamento'] > 0]

    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)

    media_faturamento = sum(faturamentos) / len(faturamentos)

    dias_acima_da_media = sum(
        1 for faturamento in faturamentos if faturamento > media_faturamento)

    return menor_faturamento, maior_faturamento, media_faturamento, dias_acima_da_media


arquivo_json = 'faturamento.json'
faturamento_diario = carregar_dados_faturamento(arquivo_json)


menor_faturamento, maior_faturamento, media_faturamento, dias_acima_da_media = analisar_faturamento(
    faturamento_diario)


print(f"Menor faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento: R$ {maior_faturamento:.2f}")
print(f"Média de faturamento: R$ {media_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
