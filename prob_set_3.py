# question 6
def is_all_lower_alphabet(ls):
    for e in ls:
        if not (e >= 'a' and e <= 'z'):
            return False
    return True

# question 7
def r_iteration(ls):
    ans = []
    for i in ls:
        if not ans:
            ans.append(i)
        else:
            if i != ans[-1]:
                ans.append(i)
    return ans

def r_recursion(ls):
    ls = ls[:]
    if len(ls) <= 1:
        return ls
    ls[1:] = r_recursion(ls[1:])
    if ls[0] == ls[1]:
        del ls[0]
    return ls

# question 8
def head(tp):
    return tp[0]
def tail(tp):
    return tp[1:]
def cons(el, tp):
    return (el,) + tp
def empty(tp):
    return not tp
def concat(tp1, tp2):
    if empty(tp1):
        return tp2
    return cons(head(tp1), concat(tail(tp1), tp2))

print(concat((1, 2), (3, 4)))
 