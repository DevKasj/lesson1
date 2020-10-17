def discounted(price,discount,max_discount=50):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError("Максимальная скидка не может быть большу 99%")
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - price*discount /100
    return price_with_discount

print(discounted(100,60,500))

product = {"name":"iphone","price":100}
print(product['price'])
product['with_discount'] = discounted(product['price'],20)
print(product)