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