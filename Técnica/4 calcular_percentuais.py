import json


with open('dados_faturamento.json', 'r') as file:
    data = json.load(file)


total = sum(data.values())


percentages = {state: (value / total) * 100 for state, value in data.items()}


for state, percentage in percentages.items():
    print(f"{state}: {percentage:.2f}%")
