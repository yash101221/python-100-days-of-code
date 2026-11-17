for number in range(1, 101):
    # 1. Check for both FIRST
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # 2. Then check for 3
    elif number % 3 == 0:
        print("Fizz")
    # 3. Then check for 5
    elif number % 5 == 0:
        print("Buzz")
    # 4. Otherwise print the number
    else:
        print(number)
