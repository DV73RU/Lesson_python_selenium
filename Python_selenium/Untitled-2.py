data = {'value_1': 10, 'value_2': 20, 'value_3': 30}

for name, value in data.items():
    vars()[name] = value
    print(name, "=", value)
