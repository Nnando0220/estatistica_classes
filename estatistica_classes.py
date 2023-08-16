from functools import reduce
from tabulate import tabulate
import math
import matplotlib.pyplot as plt
classes = []
resp = 's'

def grafico_freq_acu(classes):
    inter_cla = [f"{classe[0]} - {classe[1]}" for classe in classes]
    x = list(range(1, len(classes)+1))
    y = [classe[3] for classe in classes]
    plt.plot(x, y, marker='o')
    plt.xticks(x, inter_cla, rotation='vertical')
    plt.ylabel('Frequencia acumulada')
    plt.xlabel('Classes')
    plt.title('Grafico das frequencias acumuladas por classes')
    plt.tight_layout()
    plt.show()

def imp_table(classes, tipo_dado):
    headers=["Limite inferior","Limite superior","Frequncia absoluta","Frequncia acumulada"]
    freq_acum_classe(classes)
    tabela = tabulate(classes, headers, tablefmt="grid")
    print(tipo_dado)
    print(tabela)

def tirar_media(classes, frequencia):
    soma=0
    for classe in classes:
        soma+=(((classe[0]+classe[1])/2)*(classe[2]))
    return soma/frequencia

def tirar_mediana(classes, frequencia):
    classe_mediana = None
    classe_anterior = None
    if frequencia%2==0:
        pri_mediana = frequencia/2
        sec_mediana = pri_mediana + 1
        mediana = (pri_mediana + sec_mediana)/2
    else:
        mediana = frequencia/2
    for classe in classes:
        if classe[3]<mediana:
            classe_anterior = classe
        elif classe[3]>=mediana:
            classe_mediana = classe
            break
    if classe_mediana is not None and classe_anterior is not None:
        mediana = classe_mediana[0]+((mediana - classe_anterior[3]) * ((classe_mediana[1]-classe_mediana[0]) / classe_mediana[2]))
        return mediana
    else:
        print("MEDIANA NAO PODERA SER ENCONTRADA!!!")

def maior_frequencia(classes):
    frequencia = [classe[2] for classe in classes]
    return max(frequencia)

def tirar_moda(classes):
    classe_moda = None
    classe_anterior = None
    classe_posterior = []
    modas = []
    max_freq = maior_frequencia(classes)
    for i, classe in enumerate(classes):
        if classe[2]==max_freq:
            classe_moda = classe
            classe_anterior = classes[i - 1].copy()
            if(classe_anterior==classes[-1]):
                classe_anterior[2]=0
            if i + 1 < len(classes):
                classe_posterior = classes[i + 1].copy()
            else:
                classe_posterior = [0, 0, 0]
            if classe_moda is not None:
                moda = classe_moda[0] + ((classe_moda[2] - classe_anterior[2]) / ((classe_moda[2] - classe_anterior[2]) + (classe_moda[2] - classe_posterior[2]))) * (classe_moda[1] - classe_moda[0])
                modas.append(moda)
            else:
                print("Não foi possível calcular a moda")
    return modas

def freq_acumulada(classes):
    frequencia = [classe[2] for classe in classes]
    frequencia = reduce(lambda x, y: x + y, frequencia)
    return frequencia

def dsv_medio(classes, media, freq_acu):
    soma = 0
    for classe in classes:
        soma+=(abs((((classe[0] + classe[1]) / 2) - media)) * classe[2])
    return soma/freq_acu

def tirar_variancia(classes, media, freq_acu):
    soma = 0
    for classe in classes:
        soma+=(pow(((((classe[0] + classe[1]) / 2) - (media))),2) * classe[2])
    return soma/(freq_acu-1)

def dsv_pad(variancia):
    return math.sqrt(variancia)

def freq_acum_classe(classes):
    soma = 0
    for classe in classes:
        soma+=classe[2]
        classe.append(soma)
    return classes

def coef_var(desvio_padrao, media):
    return ((desvio_padrao/media)*100)

tipo_pesquisa = input("DIGITE O NOME PARA PESQUISA:")
while resp.lower() == 's':
    try:
        val_Inf = float(input("DIGITE O LIMITE INFERIOR DA CLASSE:"))
        val_sup = float(input("DIGITE O LIMITE SUPERIOR DA CLASSE:"))
        freq_classe = int(input("DIGITE A FREQUENCIA DA CLASSE:"))
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
        continue
    classes.append([val_Inf, val_sup, freq_classe])
    resp = input("DESEJA ADICIONAR OUTRA CLASSE? [s/n]: ")
    while resp.lower() not in ['s', 'n']:
        print("Resposta inválida. Por favor, digite 's' para Sim ou 'n' para Não.")
        resp = input("DESEJA ADICIONAR OUTRA CLASSE? [s/n]: ")

imp_table(classes, tipo_pesquisa)
freq_acu = freq_acumulada(classes)
print("FREQUENCIA ACUMULADA: ", freq_acu)
media = tirar_media(classes, freq_acu)
print("MEDIA: ", media)
print("MEDIANA: ", tirar_mediana(classes, freq_acu))
print("MODA: ", tirar_moda(classes))
desvio_medio = dsv_medio(classes, media, freq_acu)
print("DESVIO MEDIO: ", desvio_medio)
variancia = tirar_variancia(classes, media, freq_acu)
print("VARIANCIA: ", variancia)
desvio_padrao = dsv_pad(variancia)
print("DESVIO PADRÃO: ", desvio_padrao)
print("COEFICIENTE DE VARIAÇÃO: ", coef_var(desvio_padrao, media),"%")
grafico_freq_acu(classes)


