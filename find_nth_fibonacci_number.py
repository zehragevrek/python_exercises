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
