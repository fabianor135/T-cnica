def inverter_string(s):

    invertida = []

    for i in range(len(s) - 1, -1, -1):
        invertida.append(s[i])

    return ''.join(invertida)


entrada = input("Digite uma string para inverter: ")


print("String invertida:", inverter_string(entrada))
