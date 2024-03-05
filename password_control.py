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
