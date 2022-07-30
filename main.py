import os

def read_reciept(name):
    with open(name, mode='r', encoding='utf-8') as f:
        cook_book = {}
        name = f.readline().strip()
        for line in f:
            quantity = int(line.strip())
            lines = []
            for item in range(quantity):
                data = f.readline().strip().split(' | ')
                lines.append({'ingredient_name': data[0],
                              'quantity': int(data[1]),
                              'measure': data[2]})
            cook_book[name] = lines
            f.readline()
            name = f.readline().strip()
    return cook_book

def rec_reciept(book, name='reciept.txt'):
    f = open(name, mode='w', encoding='utf-8')
    for dish, recipe in book.items():
        f.write(dish + '\n')
        f.write(str(len(recipe)) + '\n')
        for ingridients in recipe:
            f.write(' | '.join(map(str, ingridients.values())) + '\n')
        f.write('\n')
    f.close()
def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for i in dishes:
        if i in cook_book:
            for reciept in cook_book[i]:
                if reciept['ingredient_name'] in result:
                    result[reciept['ingredient_name']]['quantity'] += reciept['quantity'] * person_count
                else:
                    result[reciept['ingredient_name']] = {'measure': reciept['measure'],
                                                          'quantity': reciept['quantity'] * person_count}
    return result

# Задача 3
def add_files(lst_files):
    work_zone = []
    for i in lst_files:
        with open(os.path.join(text_direct, i), mode='r', encoding='utf-8') as f:
            work_zone.append((i, len(f.readlines())))
    work_zone.sort(key=lambda x: x[1])
    f = open('result.txt', 'w', encoding='utf-8')
    for name, lenght in work_zone:
        with open(os.path.join(text_direct, name), mode='r', encoding='utf-8') as work_file:
            print(name + '\n' + str(lenght), file=f)
            for line in work_file:
                print(line.rstrip(), file=f)
    f.close()


reciept_direct = os.path.join(os.getcwd(), 'reciepts')
text_direct = os.path.join(os.getcwd(), 'texts')
lst_files = os.listdir(text_direct)
cook_book = read_reciept(os.path.join(reciept_direct, 'dish recipe'))
add_files(lst_files)


