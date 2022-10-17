def convert_roman_to_decimal(roman_number):
    
    dic_roman = {"I":1, "V":5, "X":10, "L":50, "C":100}
    num_decimal = 0
    
    for digit in range(len(roman_number)):
        num_decimal += dic_roman[roman_number[digit]]
        if  digit > 0 and dic_roman[roman_number[digit]] > dic_roman[roman_number[digit - 1]]:
            num_decimal -=  2*dic_roman[roman_number[digit - 1]]    
    
    return num_decimal
