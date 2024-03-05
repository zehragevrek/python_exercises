#######################################CENG 113 – Programming Basics: Assignment 2######################################

#the function prepareInfo for getting items in the text files and store the items according to the selections of user:
def prepareInfo(file_name, selection=None, check=None):
    file = open(file_name, "r")
    first_column = []
    pre_second_column = []
    pre_third_column = []
    second_column = []
    third_column = []

    # adding all the info from file to the lists:
    for lines in file.readlines():
        line = lines.strip('\n').strip('#').split(';')
        if selection == None:        # in this case if the file is categories.txt
            second_column.append(line[1])
            third_column.append(line[0])
        else:
            first_column.append(line[0])
            pre_second_column.append(line[1])
            pre_third_column.append(line[2])

    # adding the items that selected:
    if selection != None:
        for i in range(len(first_column)):
            if first_column[i] == check[int(selection) - 1]:     # checking the items in currennt list and the selection from previous one
                second_column.append(pre_second_column[i])                        # add the item if it is selected
                third_column.append(pre_third_column[i])
    return second_column, third_column


# the function printMenu for printing the selections with numbers starting from 1:
def printMenu(menu):
    a = 1
    for i in menu:
        print(f"{a}. {i}")
        a += 1




# the function getUserInput for getting the selection from user as an input and checking if input is valid or not:
def getUserInput(state, max_value=None):
    while True:
        i = input(f"Please select the {state}: ")
        if max_value is None or (i.isdigit() and 1 <= int(i) <= max_value):
            return i
        else:
            print("Invalid input. Please enter a valid option.")


# the main function, where we specifize what we want:
def main():
    print("--------------------------------------------------")
    print("Welcome to the Store")
    print("--------------------------------------------------")
    order = []
    total_pri = 0
    category_names, category_codes = prepareInfo("categories.txt")
    while True:
        printMenu(category_names)               # displaying the categories
        user_selection_from_categories = getUserInput("category", len(category_names))    # getting input from user
        print("--------------------------------------------------")
        print(category_names[int(user_selection_from_categories) - 1])         # printing the selection
        print("--------------------------------------------------")


        product_names, product_codes = prepareInfo("products.txt", user_selection_from_categories, category_codes)
        printMenu(product_names)               # displaying the products
        user_selection_from_products = getUserInput("product", len(product_names))    # getting input from user
        print("--------------------------------------------------")
        print((product_names[int(user_selection_from_products) - 1]))         # printing the selection
        print("--------------------------------------------------")


        portion_names, prices = prepareInfo("portions.txt", user_selection_from_products, product_codes)
        printMenu(portion_names)               # displaying the portions
        user_selection_from_portions = getUserInput("portion", len(portion_names))    # getting input from user
        print("--------------------------------------------------")

        # to calculate the total price:
        price = prices[int(user_selection_from_portions) - 1]
        total_pri += float(price)

        # putting all selections into a list named order to printing all selections at the end:
        order.append(((category_names[int(user_selection_from_categories) - 1], product_names[int(user_selection_from_products) - 1], portion_names[int(user_selection_from_portions) - 1], price)))

        # asking user if s/he want to complete or not:
        complete_order = input("Would you like to complete the order (y, n)? ").lower()
        print("--------------------------------------------------")
        if complete_order == 'y':
            break

    # printing all selections like an invoice:
    print("                                                              ")
    print("                                                              ")
    print("Order Recipe")
    print("==============================================================================================")

    for i in order:
        #print(f"{i[0]}    {i[1]}    {i[2]}    {i[3]}$")
        print(f"{i[0]}" + " " * (30 - len(i[0])) + f"{i[1]}" + " " * (40 - len(i[1])) + f"{i[2]}" + " " * (20 - len(i[2])) + f"{i[3]}" + " " * (20 - len(i[3])))
    print("==============================================================================================")
    print(f"Total: {total_pri:.2f}$")

main()
