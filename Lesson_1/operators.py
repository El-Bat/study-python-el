#1. Створити змінні таких типів: string, integer, float, bool, list, dict, tuple, None
string = "orange"
print(type(string))

num_1 = 12
print(type(num_1))

num_2 = 10.5
print(type(num_2))

checking = False
print(type(checking))

lst = ["orange", "banana", "kiwi"]
print(type(lst))

dct = {"Name": "Nick", "Age": "35", "height": "185"}
print(type(dct))

tpl = (1, 2, 3)
print(type(tpl))

print(type(None))

#2. Використати вивчені оператори та порівняти між собою числа, рядки, булеві значення, списки, словники і кортежі
num_3 = 5
num_4 = 7
num_5 = num_3 + num_4
print(num_5)
num_6 = num_3 * num_4
print(num_6)
num_7 = num_3 / num_4
print(num_7)
num_8 = num_3 - num_4
print(num_8)

num_9 = num_3 == num_4
print(num_9)
num_10 = num_3 != num_4
print(num_10)
num_11 = num_3 > num_4
print(num_11)
num_12 = num_3 < num_4
print(num_12)

num = 25
name = "Elvin"
word = "ananas"

result = num != 10 or name == "Nick"
print(result)
print(num == 25 and "i" in name or word != "orange")

lst = [1, 2, 3, 4, 5, 6]
dct = {"name": "Nick", "age": "6"}
tpl = ("1", "a", "3", "4")

print(dct["age"] == lst.index(5))
print(lst.index(3) or tpl.index(-1))


#3. Використати вивчені функції Python:
#Робота з рядками:
# 1. Cтворити змінну num_str = 125, перевести її в тип string за допогою функції str()
num_str = 125
print(str(num_str))

# 2. Cтворити зміну message = 'Hi, my name is Python!' За допомогою функції replace() замінити
#усі букви 'y' на '0' та 'i' на '1'.
message = 'Hi, my name is Python!'
print(message.replace("y","0"))
print(message.replace( "i", "1"))

# 3. Cтворити зміну split_test = 'This is a split test' і розділити її по пробілах за
#допомогою функції split(), а потім знову обʼєднати у строку за допомогою функції join() у змінну string_join
split_test = 'This is a split test'
print(split_test.split())
string_join = "".join(split_test)
print(string_join)

# 4. Визначити довжину рядку string_join за допомогою функції len()
print(len(string_join))

#Робота зі списками:
# 1. Cтворити змінну list_append = [1, 2, 3] і за допомогою функції append() додати туди спочатку 4, а потім 5
list_append = [1, 2, 3]
list_append.append(4)
print(list_append)
list_append.append(5)
print(list_append)

# 2. Cтворити змінну list_extend = [4, 5, 6] і розширити цей список іншим списком [7, 8, 9] за допомогою функції extend()
list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print(list_extend)

# 3. Визначити індекс елемента 6 у списку list_extend за допомогою функції index()
print(list_extend.index(6))

# 4. Визначити довжину списку list_append за допомогою функції len()
print(len(list_append))

#Робота зі словниками:
# 1. Cтворити змінну dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'} та вивести на екран дані, які знаходяться в ключах car та where
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test.get('car','where'))

# 2. За допомогою функцій keys() і values() вивести на екран ключі та їх значення
print(dict_test.keys())
print(dict_test.values())

# 3. За допомогою функції items() вивести на екран пари ключ - значення
print(dict_test.items())