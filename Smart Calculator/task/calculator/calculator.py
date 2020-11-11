# write your code here
while True:
    user_input = input()
    if user_input == "/exit":
        break
    try:
        number1, number2 = user_input.split(" ")
        print(int(number1) + int(number2))
    except ValueError:
        if user_input != "":
            print(user_input)
print("Bye!")
