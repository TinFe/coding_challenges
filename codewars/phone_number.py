def create_phone_number(n):
    
    phone_number_string = ''
    for i in n:
        phone_number_string += str(i)
        
    output = f"({phone_number_string[0:3]}) {phone_number_string[3:6]}-{phone_number_string[6:10]}"
    return output
    
