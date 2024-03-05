#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Part 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def find_num(line):
    num = ""
    for i in line:
        if i.isdigit() == True:
            num += i
    return num[0] + num[-1]





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Part 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def find_num2(line):
    numbers_dict = {"one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    for j in numbers_dict:
        new_line = line.replace(j, numbers_dict[j])
        line = new_line
    x = find_num(new_line)
    return x



file = open("adventofcode_2023_1.txt", "r")
lines = file.readlines()
sum = 0
line_int = 0
for line in lines:
    num = find_num2(line)
    sum += int(num)
file.close()
print(sum)

