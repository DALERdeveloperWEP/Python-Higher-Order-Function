# numbers = [4, -2, 0, 7, -9, 3, -1, 5]

# print(list(filter(lambda num: num > 0, numbers)))

products = [
    {
        "name": "samsung s22",
        "price": 310,
        "quantity": 6
    },
    {
        "name": "samsung s23",
        "price": 350,
        "quantity": 4
    },
    {
        "name": "samsung s24",
        "price": 430,
        "quantity": 3
    },
]

result = []

print(list(filter(lambda product: (product['price'] * product['quantity']) > 1450, products)))
