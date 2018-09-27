a_list = 'this is a  long string'.split(" ")
a_list.append("emmanuel")
print(a_list)

def first_function(): 
    print("this is my first function")
    print("see your head")
    first_variable = 1
    secondVariable = 2
    sum = first_variable + secondVariable
    print(sum)

first_function()


def igpay(sample_string):
    vowels = 'aeiouAEIOU'

    if sample_string[0] in vowels:
        print(sample_string + "way")
    else:
        print(sample_string[1:] + sample_string[0] + "ay")


igpay("pig")
igpay("apple")
igpay("dinosaur")

b = bytes()

greeting = b"hello emmanuel"
print(greeting)

for c in greeting: print(c)

cats = {'adrian': 2, "bob": 1, "julia": '3'}
cats.get('bob')
cats["julia"] = 6
cats['julia']

del cats['bob']

cats.pop('adrian')

cats

try:
    num = input("Enter a number: ")
    num_int = int(num)
except ValueError: print("something went wrong")