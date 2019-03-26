def combinaciones(lista1, lista2):
    if isinstance(lista1, list) and isinstance(lista2, list):
        return combin(lista1, lista2, lista2)
    else: return "Error en los parametros"

def combin(lista1, lista2, lista2_aux):
    if lista2 == []:
        return combin(lista1[1:], lista2_aux, lista2_aux)
    elif lista1 == []:
        return []
    else: return [lista1[0]+lista2[0]] + combin(lista1, lista2[1:], lista2_aux)

#-----------------------------------------------------------------------------#
import math
#//"math" lo escribi con "M" mayuscula en el examen//
def std(lista, avg):
    if isinstance(lista, list) and isinstance(avg, float):
        return math.sqrt(std_aux(lista, avg)/(len(lista)-1))
    else: return "Error, el promedio debe ser float"

def std_aux(lista, avg):
    if lista == []:
        return 0
    else: return (lista[0]-avg)**2 + std_aux(lista[1:], avg)
#Nota: En la explicacion del examen sale como resultado "63.97" pero eso seria
# "S^2" asi que se le saca raiz cuadrada

#-----------------------------------------------------------------------------#
def zScore(lista, S, avg):
    if isinstance(lista, list) and isinstance(S, float) and isinstance(avg, float):
        return zScore_aux(lista, S, avg)
    else: return "Error, 'S' y promedio deben ser float"

def zScore_aux(lista, S, avg):
    if lista == []:
        return []
    else: return [(lista[0]-avg)/S] + zScore_aux(lista[1:], S, avg)

#-----------------------------------------------------------------------------#
def rScore(lista1, lista2):
    if isinstance(lista1, list) and isinstance(lista2, list):
        return rScore_aux(lista1, lista2)/(len(lista1)-1)
    else: return "Error"

def rScore_aux(lista1, lista2):
    if lista1 == []:
        return 0
    else: return(lista1[0]*lista2[0]) + rScore_aux(lista1[1:], lista2[1:])


    
