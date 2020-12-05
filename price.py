def format_price(price):
    price = int(price)
    res = 'Цена:'+str(price)+'  ssdfруб.'
    return res

a = input('Enter the value')
result = format_price(56.24)
print(result)