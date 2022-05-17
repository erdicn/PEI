import sympy
import math

def moyenne(Les_mesures : list):
    tot = 0
    for xi in Les_mesures:
        tot += xi
    return tot/len-Les_mesures

def sum_x_moins_moy(Les_mesures : list):
    sum = 0
    moy_Lesmesures = moyenne(Les_mesures)
    for xi in Les_mesures:
        sum += abs(xi - moy_Lesmesures)
    return sum

def sum_x_moins_moy_avec_caree(Les_mesures : list):
    sum = 0
    moy_Lesmesures = moyenne(Les_mesures)
    for xi in Les_mesures:
        sum += (xi - moy_Lesmesures)*(xi - moy_Lesmesures)
    return sum

def dispersion(Les_mesures : list):
    return sum_x_moins_moy/len(Les_mesures)

def ecart_type(Les_mesures : list):
    return math.sqrt(sum_x_moins_moy_avec_caree/(len(Les_mesures) - 1))

