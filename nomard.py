# print("Hello world!")

# a = 2
# b = 3
# c = a + b
# print(c)

# my_name = "Jioh"
# age = 28
# dead = False
# print("hello my name is", my_name)
# print("and I'm ", age, " years old")

# print("asdf")
# print(True)
# print("hello")
# print(12)

# def say_hello(name, age= 28):
#   print("hello", name)
#   print("You are", age , "years old")

# say_hello("jioh", 28)
# # say_hello(input("what your name?"))

# def say_bye():
#   print("bye bye")


# def tax_calculator(pay):
#   return pay * 0.35

# def pay_tax(tax):
#   print("thank you for paying", tax)

# to_pay = tax_calculator(1500000)
# pay_tax(to_pay)

# tax_calculator(input("How much money did you make this year? $ "))

# # 1/24
# def say_hello(name = "anonymous"):
#   print("Hello", name)

# say_hello("Jioh")
# say_hello()

# def plus(a,b):
#   print(a + b)


# def pay_tax(tax):
#   print("thank you for paying", tax)

# to_pay = tax_calculator(1500000)
# pay_tax(to_pay)

# my_name = "Jioh"
# my_age = 28
# my_color_eyes = "brown"

# print(f"Hello i'm {my_name}, I have {my_age} years old, {my_color_eyes} is my eye color.")

# def make_juice(fruit):
#   return f"{fruit} + J"

# def add_ice(juice):
#   return f"{juice} + I"

# def add_sugar(ice_juice):
#   return f"{ice_juice} + S"

# juice = make_juice("사과")
# cold_juice = add_ice(juice)
# perfect_juice = add_sugar(cold_juice)

# print(perfect_juice)


from random import randint

print("welcome to Python Casino")
pc_choice = randint(1,50)

playing = True

while playing:
  user_choice = int(input("Choose number:"))
  
  if user_choice == pc_choice:
    print("You win!")
    playing = False
  elif user_choice > pc_choice:
    print("Lower! Computer chose" , pc_choice)
  
  elif user_choice < pc_choice:
    print("Higher! Computer chose" , pc_choice)