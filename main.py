#Итераторы, генераторы, замыкание, декораторы
import random

numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
     print(number)

iterator = iter(numbers) #итер - превращает список в итератор
print(next(iterator)) #некст возвращает след. элемент из итератора
print(next(iterator))
print(next(iterator))
print(next(iterator))

print("------------------------------------------------------")

class Counter: #Manji kick??
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration

        return self.i

print("------------------------------------------------------")

counter = Counter(10)

for count in counter:
    print(count)

print("------------------------------------------------------")

print("Task 1")

print("------------------------------------------------------")

text = input("Введите слово:")

try:
    iterator = iter(text)
    for i in text:
        print(next(iterator))

except:
    print("AN EROR OCURED AN EROR OCURED SIR!!")

text2 = input("Введите слово:")
iterator = iter(text2)
try:
    while True:
        print(next(iterator))

except StopIteration:
    print("End")

print("------------------------------------------------------")
print("Task 3")
print("------------------------------------------------------")
def rN():
    a = random.randint(1,10)
    return a

nums = [rN(),rN(),rN(),rN(),rN()]
print(nums)

iterator = iter(nums)
try:
    while True:
        print(next(iterator)**2)

except StopIteration:
    print("End")
print("------------------------------------------------------")
print("Generators")
print("------------------------------------------------------")
#Generators
#Generator that creates numbers
def generate_numbers():
    for i in range(6):
        yield i #Не останавливая работу выведет всё, yield makes function to generator
def generate_numbers2():
    for i in range(5):
        return i #Ретёрн - выведет только 0, ведь он останавливает работу

print(generate_numbers2())
gen = generate_numbers()
print(next(gen))
print(next(gen))
print(next(gen))

print("------------------------------------------------------")
print("Generators Task 1")
print("------------------------------------------------------")

gen = generate_numbers()
print(next(gen)**2)
print(next(gen)**2)
print(next(gen)**2)
print(next(gen)**2)
print(next(gen)**2)
print(next(gen)**2)