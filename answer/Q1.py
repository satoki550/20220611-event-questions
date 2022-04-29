for num in range(1, 101):
    string = f'{num}'

    # ここから記述
    if num%3==0:
        string='Fizz'
    if num%5==0:
        string='Buzz'
    if num%15==0:
        string='FizzBuzz'

    # ここまで記述

    print(string)
