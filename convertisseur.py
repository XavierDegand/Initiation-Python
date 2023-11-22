
import time
def decimal_to_binary(input_dec):
    debut = time.time()
    quotient = -1
    result = ''
    while quotient != 0:
        quotient = input_dec // 2
        rest = input_dec % 2
        result = str(rest) + result
        input_dec = quotient
    fin = time.time()
    return 'premier',result, fin - debut

def optimise_decimal_to_binary(input_dec):
    """Convertit un nombre en binaire"""
    first = time.time()
    if input_dec == 0:
        return '0'
    result = ''
    while input_dec != 0 : input_dec, result = input_dec >> 1, str(input_dec & 1) + result
    end = time.time()
    return 'deuxième',result, end - first