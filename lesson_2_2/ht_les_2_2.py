# Hometask for Lesson 2.2
# Со звездочкой:
# 1. Добавить до каждого из заданий 3 варианта развитий событий (elif)


# 1. Пользователь вводит 3 числа. В зависимости от выбора нужно найти сумму или произведение чисел.
# Asking for information
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
    print("You have chosen something that I can not do.")


# Null variable that I used before next task
a = None
b = None
c = None



# 2. Пользователь вводит 3 числа. В зависимости от выбора нужно найти максимальное или минимальное значение.
# Asking for information
print("Let's try to check what number bigger or less!")
a = float(input("Enter A: "))
b = float(input("Enter B: "))
c = float(input("Enter C: "))

# We know that we should find bigger or less number so we make a list
min_or_max_list = [a, b, c]

# Asking about action and doind chosen action
what_to_do_var_q2 = int(input("What do you want to do? (1 = Find bigger, 2 = Find less) "))
if what_to_do_var_q2 == 1:
    print("The bigger number is: ", max(min_or_max_list))
elif what_to_do_var_q2 == 2:
    print("The less number is: ", min(min_or_max_list))
else:
    print("You have chosen something that I can not do.")


# 3. Пользователь вводит количество метров. В зависимости от выбора нужно конвертировать данные в километры или миллиметры.
# Asking for information
meters = float(input("Enter meters, please: "))

# Asking about action and doind chosen action
what_to_do_var_q3 = int(input("What do you want to do? (1 = Find kilometers, 2 = Find milimeters) "))
if what_to_do_var_q3 == 1:
    print(meters, "in kilometers is: ", meters / 1000)
elif what_to_do_var_q3 == 2:
    print(meters, "in milimeters is: ", meters * 1000)
else:
    print("You have chosen something that I can not do.")