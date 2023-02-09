# question 5
def q5(str1, str2):
    if str1[-1] == str2[-1]:
        return True
    else:
        return False
    
# question 6
def q6(num1, num2, num3):
    ave = (num1 + num2 + num3) / 3
    smallest = min(num1, num2, num3)
    return smallest <= ave

# question 7
def q7(num):
    if num:
        print(1)
    else:
        print(0)

# question 8       
def q8(n, d):
    s_n = str(n)
    cut_s_n = s_n[:-(d + 1)]
    return int(cut_s_n)
   
# question 9
def q9(t, n):
    n = n % 24
    hour = int(t[0:2])
    hour += n
    hour = hour % 24
    if hour <= 9:
        ans = '0' + str(hour) + t[2:]
    else:
        ans = str(hour) + t[2:]
    return ans

