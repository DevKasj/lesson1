def get_summ(one,two,delimiter = '&'):
    one = str(one)
    two = str(two)
    result = one + delimiter +two
    

    new_result = result.upper()
    new_result = str(new_result )
    return new_result

print(get_summ('Learn','python'))


