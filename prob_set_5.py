# 1 Simple Exercise
# 1. 2
# 2. ['aa', 'ba', 'ca']
# 3. -------
# 4. 6
# 5. -------
# 6. [True, True, True, False, False, True]
# 7. -------
# 8. [9, 8, 7, 3]
# 9. ['e', 'o', 'e', 'o', 'e', 'o', 'e', 'o']
# 10. [0, 1, 2, 3, 4, 5, 6, 7]
# 11. ['1', '3', '5', '7', '9']
# 12. '[36, 48, 64, 81]'
# 2. 2500>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>10

# 2 Short Programming Question
# 3. foo(5) = lambda a: a(5)(a)
#    foo(5)(bar) = bar(5)(bar)
#    bar(x) = lambda a: a(x + 1)
#    bar(5) = lambda a: a(6)
#    bar(5)(bar) = bar(6) = lambda a: a(7)
#    foo(5)(bar) = lambda a: a(7)
#    foo(5)(bar)(lambda x: x) = 7
#    6>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>7 is ok

# 4.
def sum(term, a, next, b):
    if (a > b):
        return 0
    return term(a) + sum(term, next(a), next, b)
def accumulate(fn, init, ls, get):
    if not ls:
        return init
    return fn(get(ls), accumulate(fn, init, ls[1:], get))
def fold(op, f, n):
    if n == 0:
        return f(0)
    return op(f(n), fold(op, f, n - 1))

def knocked_down(game):
# you may define t1, t2, t3 and t4 here.
# you are only allowed to return the following. return sum(t1, t2, t3, t4)
    def t1(x):
        if game[x] == 'X':
            return 10
        elif game[x] == '/':
            return 10 - int(game[x - 1])
        else:
            return int(game[x])
    t2 = 0
    t3 = lambda x: x + 1
    t4 = len(game) - 1
    
    return sum(t1, t2, t3, t4)

def score(game):
# you may define t1, t2, t3 and t4 here.
# you are only allowed to return the following. return accumulate(t1, t2, t3, t4)
    t1 = lambda x, y: x + y
    t2 = 0
    t3 = game
    def t4(x):
        if x[0] == 'X':
            return 30
        elif x[0] == '/':
            return 0
        else:
            if x[1] == '/':
                return 20
            else:
                return int(x[0])
    return accumulate(t1, t2, t3, t4)

def has_triple(game):
# you may define t1, t2, and t3 here.
# you are only allowed to return the following. return fold(t1, t2, t3)
    t1 = lambda x, y: x or y
    def t2(x):
        return game[x] == 'X' and game[x + 1] == 'X' and game[x + 2] == 'X'
    t3 = len(game) - 3
    return fold(t1, t2, t3)

# print(has_triple('XXXXXXXXXX'))

# 5.
def burger_price(burger):
    ingredient_price = {
        'B': 50,
        'C': 80,
        'P': 150,
        'V': 70,
        'O': 40,
        'M': 90
    }
    acc = 0
    for ing in burger:
        acc += ingredient_price[ing]
    return acc
ingredient_price = {
    'B': 50,
    'C': 80,
    'P': 150,
    'V': 70,
    'O': 40,
    'M': 90
}
# recursion
def burger_price_recursion(burger):
    if not burger:
        return 0
    return ingredient_price[burger[0]] + burger_price_recursion(burger[1:])
# map, filter, reduce
def burger_price_highorder(burger):
    get_price = lambda x: ingredient_price[x]
    return sum(list(map(get_price, burger)))

# 6.
def scale(ls, n):
    get_scale = lambda base: base * n
    return sum(map(get_scale, ls))
def scale_recursion(ls, n):
    if not ls:
        return 0
    return ls[0] * n + scale_recursion(ls[1:], n)

# 7. 
def bfs(d, src, dst):
    visited = set()
    def check(current, dst, frontier):
        if not frontier:
            return False
        if current in visited: 
            current = frontier.pop(0)
        if current == dst:
            return True
        visited.add(current)
        frontier.extend(d[current])
        return check(frontier.pop(0), dst, frontier)
    return check(src, dst, list(d[src]))