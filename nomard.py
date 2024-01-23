print("Hello world!")

a = 2
b = 3
c = a + b
print(c)

my_name = "Jioh"
age = 28
dead = False
print("hello my name is", my_name)
print("and I'm ", age, " years old")

print("asdf")
print(True)
print("hello")
print(12)

def say_hello(name, age):
  print("hello", name)
  print("You are", age , "years old")

say_hello("jioh", 28)
say_hello(input("what your name?"))

def say_bye():
  print("bye bye")


def tax_calculator(pay):
  print("Yours tax is $" , float(pay) *0.35)

tax_calculator(input("How much money did you make this year? $ "))