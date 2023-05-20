import numpy as np
from functools import reduce
import statistics as st

def moda(array):
    return st.mode(array)

def mediana(array):
    return np.median(array)

def tirar_media(array):
    soma = reduce(lambda x, y: x + y, array)
    return soma/len(array)

def tirar_amplitude(array):
    return array[-1]-array[0]

def val_maior(array):
    val = int(input("DIGITE O NUMERO PARA A PORCENTAGEM DE NUMERO(S) MAIORES QUE:"))
    while(val > array.max()):
        val = int(input("DIGITE O NUMERO PARA A PORCENTAGEM DE NUMERO(S) MAIORES QUE:"))
    count = reduce(lambda count, x: count+1, filter(lambda x: x<val, array), 0)
    print("PORCENTAGEM: ",(count/len(array)*100),"%")

def desvio_medio(array, media):
    ds_medio=list(map(lambda x: abs(x-media),array))
    soma_medio=np.array(ds_medio)
    soma = reduce(lambda x,y: x+y,soma_medio)
    return soma/len(array)

def tirar_variancia(array, media):
    variancia = list(map(lambda x: abs(x - media) ** 2, array))
    soma = reduce(lambda x, y: x + y, variancia)
    return soma/(len(array)-1)

def desvio_padrao(array):
    return np.std(array, ddof=1)

rol=np.sort(np.array([4,5,4,20,21,4,7,10,11,23]))
print("\nROL: ",rol)
print("\nMODA: ",moda(rol))
print("\nMEDIANA: ",mediana(rol))
print("\nAMPLITUDE: ",tirar_amplitude(rol))
media=tirar_media(rol)
val_maior(rol)
print("\nMEDIA:",media)
print("\nDESVIO MEDIO: ",desvio_medio(rol, media))
print("\nVARIANCIA: ",tirar_variancia(rol, media))
print("\nDESVIO PADRÃO: ",desvio_padrao(rol))