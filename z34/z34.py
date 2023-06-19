vinni = str(input('Введите стихотворение: '))
print(vinni)

glasn = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', ' ']

def glasn_filter(let: str):
    for letter in let:
        if letter in glasn:
            return True
    
my_str = ''.join(list(filter(glasn_filter, vinni))).split()
new_str = list()
for i in range(len(my_str)):
    new_str.append(len(my_str[i]))

def res(num): 
    if all(x == new_str[0] for x in new_str):
        print('Парам пам-пам')
    else:
        print('Пам парам')


print(my_str)
print(new_str)
res(new_str)
