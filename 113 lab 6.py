# 1 : for'la dene
def main():
    n = int(input("Which rank of the number do you want to know?"))
def f(n):
    n_1 = 0
    n_2 = 1
    if n == 1:
        n_3 = 0
    elif n == 2:
        n_3 = 1
    while n > 2:
        n_3 = n_1 + n_2
        n_1 = n_2
        n_2 = n_3
        n -= 1
    return n_3
print (f(n))
main()




# 2 :
def main():
    pw = input("Enter your password. ")
    sec(pw)
def sec(pw):
    n = 0
    for d in pw:
        n += 1
        sec_level = 0
        if d == " " or n < 8:
            sec_level = 0
        elif d.isalpha() or d.isdigit() or d == "!" or d == "*" or d == "?":
            sec_level = 1
    print(sec_level)
main()
