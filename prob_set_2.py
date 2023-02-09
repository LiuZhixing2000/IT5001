# question 5
def cab_fare(ride, distance):
    if ride == 'Grab':
        flagDownFare = 3
        perKmRate = 0.5
    elif ride == 'Gojek':
        flagDownFare = 2.5
        perKmRate = 0.6
    ans = flagDownFare + distance * perKmRate
    return ans

# question 6
def burger_price(burger):
    ans = 0
    for e in burger:
        if e == 'B':
            ans += 0.5
        elif e == 'C':
            ans += 0.8
        elif e == 'P':
            ans += 1.5
        elif e == 'V':
            ans += 0.7
        elif e == 'O':
            ans += 0.4
        elif e == 'M':
            ans += 0.9
    return ans

# question 7 
def parking(space):
    if space <= 0:
        return 0
    elif space == 1:
        return 1
    elif space == 2:
        return 2
    else:
        return parking(space - 1) + parking(space - 2)

# question 8
def approx_pi(delta):
    i = 0
    ans = 0
    while True:
        ans_i = ans + 4 * (-1)**i / (2*i + 1)
        if abs(ans_i - ans) < delta:
            return ans_i
        ans = ans_i
        i += 1
    
# question 9
def sum_digits_while(n):
    # while loop
    ans = 0
    while n > 0:
        ans += n % 10
        n = n // 10
    return ans

def sum_digits_for(n):
    # for loop
    ans = 0
    s_n = str(n)
    for e in s_n:
        ans += int(e)
    return ans
def sum_digits_recursion(n):
    # recursion
    if n % 10 == n:
        return n
    else:
        return n % 10 + sum_digits_recursion(n // 10)

# question 10
def all_odd_while(n):
    while n > 0:
        digit = n % 10
        if not digit % 2:
            return False
        n = n // 10
    return True
def all_odd_loop(n):
    s_n = str(n)
    for e in s_n:
        digit = int(e)
        if not digit % 2:
            return False
    return True
def all_odd_recursion(n):
    if n % 10 == n:
        if not n % 2:
            return False
        else:
            return True
    else:
        return all_odd_recursion(n % 10) and all_odd_recursion(n // 10)
    
# question 11
def fibonacci_iteratively(n):
    a = 1
    b = 1
    c = 1
    while n > 1:
        c = a + b
        a = b
        b = c
        n -= 1
    return c

def fibonacci_recursively(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci_recursively(n - 1) + fibonacci_recursively(n - 2)

# question 12
def can_be_float(s):
    try:
        float(s)
    except:
        return False
    return True

# question 14
from random import randint
# def game():
#     ans = randint(1, 100)
#     num = int(input('Make a guess: '))
#     if num == ans:
#         output = 'Correct!'
#     else:
#         output = 'Wrong!'
#     print(output)

# question 15
# def game():
#     ans = randint(1, 100)
#     while True:
#         num = int(input('Make a guess: '))
#         if num == ans:
#             print('Correct!')
#             break
#         elif num < ans:
#             output = 'Too small'
#         elif num > ans:
#             output = 'Too big'
#         print(output)

# question 16
def game():
    ans = randint(1, 100)
    chance  = 3
    while True:
        try:
            num = int(input('Make a guess: '))
        except:
            continue
        if num == ans:
            print('Correct!')
            break
        elif num < ans:
            output = 'Too small'
        elif num > ans:
            output = 'Too big'
        print(output)
        chance -= 1
        if chance <= 0:
            print('The answer was ' + str(ans) + '!')
            break
        
game()