def my_keys(var):
    print('var =', var)
    b = var.values()
    c = var.keys()
    return list(b), list(c)


a = {'spartak': 'moscow', 'dynamo': 'minsk'}
b = {'1': '5', '2': '10'}

x = my_keys(a)
num_return = my_keys(b)

