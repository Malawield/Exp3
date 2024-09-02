# 1.Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params('start', 5 < 4, 3)
print_params(12, 5)
print_params(53.2)
print_params(b=25)
print_params(c=[1, 2, 3])

# 2.Распаковка параметров:
values_list = ['str', False, 11]
values_dict = {'a': False, 'b': 8, 'c': 'Denis'}

print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
values_list2 = [True, 33.3]

print_params(*values_list2, 42)
