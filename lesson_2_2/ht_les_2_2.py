# Hometask for Lesson 2.2
# 1. Пользователь вводит 3 числа. В зависимости от выбора нужно найти сумму или произведение чисел.
# 2. Пользователь вводит 3 числа. В зависимости от выбора нужно найти максимальное или минимальное значение.
# 3. Пользователь вводит количество метров. В зависимости от выбора нужно конвертировать данные в километры или миллиметры.
# Со звездочкой:
# 1. Добавить до каждого из заданий 3 варианта развитий событий (elif)

# Asking for information (1 question)

print("Let's try to sum or multiplacate!")
a = float(input("Enter A: "))
b = float(input("Enter B: "))
c = float(input("Enter C: "))

# Asking about action and doind chosen action

what_to_do_var_q1 = int(input("What do you want to do? (1 = sum, 2 = multiplication) "))
if what_to_do_var_q1 == 1:
    print("A + B + C = ", a + b + c)
elif what_to_do_var_q1 == 2:
    print("A * B * C = ", a * b * c)
else:
    print("You have chosen something what I can not do.")

# Null variable that I used
a = None
b = None
c = None

# Asking for information (2 question)

print("Let's try to check what number bigger or less!")
a = float(input("Enter A: "))
b = float(input("Enter B: "))
c = float(input("Enter C: "))

# Asking about action and doind chosen action

what_to_do_var_q2 = int(input("What do you want to do? (1 = Find bigger, 2 = Find less) "))
if what_to_do_var_q2 == 1:
    if a >= b
elif what_to_do_var_q2 == 2:
else:
    print("You have chosen something what I can not do.")