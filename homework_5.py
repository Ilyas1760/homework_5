immutable_var= (1, 2, 3, 'appel', 2.0 )
print(immutable_var)
#immutable_var[0] = 5 # так как это кортеж замена не возможна, это не изменяемый объект
mutable_list = (['home', 'maus', 5, 20.5])
print(mutable_list)
mutable_list[0]= 'work'
print(mutable_list)
mutable_list.extend(["book"])
print(mutable_list)
mutable_list.remove(5)
print(mutable_list)
