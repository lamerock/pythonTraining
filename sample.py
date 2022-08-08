import math

print("My first python program!")

# assigning values to the variables
name = "Gerard James"
age = 18

# concatenation
print("My name is " + name)
print("My age is " + str(age))

# changing the value from string to number
number1 = "10"
number2 = "20"
print(int(number1) * int(number2))

# accepting user inputs
name = input("Enter full name: ")
email = input("Enter email address: ")
print("Name: " + name)
print("Email: " + email)

# string manipulations using escape characters
# \' - display single quotes
# \" - display double quotes
# \n - new line
print('I don\'t like vegetables')
print("I don't like vegetables")
print("I said, \"Hey!\"")
print("This is the first line. \nThis is the second line.")

# memory location using index
word = "PRoGraMming language"
print(word[0])
print(word[3])
print(word[-11])
print(word[3:7])
print(word[3:])
print(word[:3])
print(word[:3] + word[6])

# length of the string
print(len(word))

name = "Jane"
food = "Adobo"
game = "Volleyball"
sampleText1 = "My name is {} i love {} and playing {}"
sampleText1a = sampleText1.format(name, food, game)
print(sampleText1a)

sampleText1 = "My name is {2} i love {0} and playing {1}"
sampleText1a = sampleText1.format(name, food, game)
print(sampleText1a)

sampleText1 = "My name is {newname} i love {newfood} and playing {newgame}"
sampleText1a = sampleText1.format(newname="James", newfood="Spaghetti", newgame="Chess")
print(sampleText1a)

item = "Milk"
cost = 35.50
sampleText4 = "The product %s costs %.2f" %(item, cost)
print(sampleText4)

sampleText5 = f"The product {item} costs {cost * 100} pesos"
print(sampleText5)

num = 0
num = 5
print(num)

ngaran = "python proGRAMming"
print(ngaran.upper())
print(ngaran.lower())
print(ngaran.capitalize())
print(ngaran.title())

# +, -, *, /
# PEMDAS
print(5 + 2)
print(12 * 5)
print(16-9)
print(100 - 12 * 5 + 2 * 6)
print(5 + 2.0) # int + float = float

print(10 / 4) # with fractional part
print(10 // 4) # disregard the fractional part
print(11 % 4) # modulus - getting the remainder

grade1 = 95.50
grade2 = 95.20
print(round(grade1, 0))
print(round(grade2, 0))




print(math.ceil(grade1))
print(math.ceil(grade2))
print(math.floor(grade1))
print(math.floor(grade2))
print(pow(2,3))
print(2**3)
print(math.sqrt(16))

a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print(c)
