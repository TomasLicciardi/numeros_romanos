def convert_decimal_to_roman(decimal_number):
    roman = ''
    
    menor_a_10 = decimal_number % 10
    multiplos_10 = decimal_number // 10
    variable_1 = ''
    variable_2 = ''
    result_1_2_3 = ''
    result_4 = ''
    result_5 = ''
    result_6_7_8 = '' 
    result_9 = ''
    result_10 = ''
    result_50 = ''
    result_100 = ''

    if 0 < multiplos_10 < 4:
        for digit in range(multiplos_10):
            result_10 += 'X'

    if menor_a_10 < 4:
        for digit in range(menor_a_10):
            result_1_2_3 += 'I'
    
    if menor_a_10 == 5:
        result_5 = 'V' 

    if menor_a_10 == 4:
        result_4 = 'IV' 

    if menor_a_10 == 9:
        result_9 = 'IX' 

    if 5 < menor_a_10 < 9:
        for digit in range(menor_a_10-5):
            variable_2 = 'V'
            variable_1 += 'I'
            result_6_7_8 = variable_2 + variable_1
    
    if multiplos_10 == 5:
        result_50 = 'L' 

    if 9 < multiplos_10 < 20:
        result_100 = 'C'

    result = result_100 + result_50 + result_10 + result_9 + result_4+ result_5 + result_6_7_8 + result_1_2_3
    return result
