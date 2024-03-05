# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ HW 3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# student id: 310201107
import os, glob


def get_query():
    query_input = input("What is your query? ")
    return query_input


def create(file_name, column_names):
    filename = file_name + ".hw3"
    if "id" in column_names:
        return "You cannot create a file with attribute 'id'.", []
    elif not os.path.exists(filename):
        file = open(filename, 'a')
        column_names = "id," + column_names + "\n"
        file.writelines(column_names)
        file.close()
        return "Corresponding file was successfully created.", file
    else:
        file = open(filename, 'w')
        column_names = "id," + column_names + "\n"
        file.writelines(column_names)
        file.close()
        return "There was already such a file. It is removed and then created again.", file


def delete(file_name):
    filename = file_name + ".hw3"
    if not os.path.exists(filename):
        return "There is no such file."
    else:
        os.remove(filename)
        return "Corresponding file was successfully deleted."


def display():
    files_hw = []
    for file in glob.glob("*.hw3"):
        files_hw.append(file)
    files = dict()
    for file_name in files_hw:
        file = open(file_name, 'r')
        contents = file.readlines(1)
        files[file_name] = contents[0]
    return files


def add(new_line, file_name):
    filename = file_name + ".hw3"
    if not os.path.exists(filename):
        return "There is no such file."
    else:
        file = open(filename, "r")
        x = file.readlines(1)
        y = x[0]
        if len(y.split(",")) - 1 != len(new_line.split(",")):
            file.close()
            return "Numbers of attributes do not match."
        else:
            line_number = 0
            for i in file.readlines():
                line_number += 1
            file.close()
            file = open(filename, "a")
            file.writelines(f"{line_number + 1},{new_line}\n")
            file.close()
            print_line = f"New line was successfully added to students with id = {line_number + 1}."
            return print_line


def remove(file_name, condition):
    filename = file_name + ".hw3"
    if not os.path.exists(filename):
        return "There is no such file."
    else:
        file = open(filename, "r")
        file_line = file.readlines(1)
        attributes = file_line[0].strip("\n").split(",")
        condition_separate = condition.split(" ")
        if not condition_separate[0] in attributes:
            return "Your query contains an unknown attribute."
        else:
            count = 0
            for i in attributes:
                if condition_separate[0] != i:
                    count += 1
                else:
                    file_lines = file.readlines()
                    for i in file_lines:
                        j = i.strip("\n").split(",")
                        if condition_separate[1] == "==":
                            if j[count] != condition_separate[2]:
                                line_number = 0
                                for k in file.readlines():
                                    line_number += 1
                                file.close()
                                file = open(filename, 'w')
                                column_names = file_line[0]
                                file.writelines(f"{column_names}\n")
                                line = ""
                                for n in j[0]:
                                    if n != j[0]:
                                        line += "," + n
                                file.writelines(f"{line_number + 1},{j}")
                        elif condition_separate[1] == "!=":
                            if j[count] == condition[2]:
                                line_number = 0
                                for k in file.readlines():
                                    line_number += 1
                                file.close()
                                file = open(filename, 'w')
                                column_names = file_line[0] + "\n"
                                file.writelines(column_names)
                                file.writelines(f"{line_number + 1},{i}\n")
            file.close()




def modify():
    pass


def fetch():
    pass


def main():
    question = ""
    while question != "x":
        question = get_query()
        query_line = question.strip("/n").split(" ")
        query = query_line[0]

        if query == 'create':
            if query_line[1] != "file" or query_line[3] != "with":
                print("Invalid query.")
            else:
                file_name = query_line[2]
                column_names = query_line[4]
                a, b = create(file_name, column_names)
                print(a)

        elif query == 'delete':
            if query_line[1] != "file":
                print("Invalid query.")
            else:
                file_name = query_line[2]
                print(delete(file_name))

        elif query == 'display':
            if query_line[1] != "files":
                print("Invalid query.")
            else:
                files = display()
                print("Number of files:", len(files))
                count = 1
                for i in files:
                    j = i.strip(".hw3")
                    print(f"{count}) {j}: {files[i]}")
                    count += 1

        elif query == 'add':
            if query_line[2] != "into":
                print("Invalid query.")
            else:
                new_line = query_line[1]
                file_name = query_line[3]
                print(add(new_line, file_name))

        elif query == 'remove':
            if query_line[1] != "lines" or query_line[2] != "from" or query_line[4] != "where":
                print("Invalid query.")
            else:
                file_name = query_line[3]
                condition = f"{query_line[5]} {query_line[6]} {query_line[7]}"
                remove(file_name, condition)

        elif query == 'modify':
            if query_line[2] != "in" or query_line[4] != "as" or query_line[6] != "where":
                print("Invalid query.")
            else:
                column_name1 = query_line[1]
                file_name = query_line[3]
                new_name = query_line[5]
                condition = query_line[7] + query_line[8] + query_line[9]
                modify(column_name1, file_name, new_name, condition)

        elif query == 'fetch':
            if query_line[2] != "from" or query_line[4] != "where":
                print("Invalid query.")
            else:
                columns = query_line[1].split(",")
                file_name = query_line[3]
                condition = query_line[5] + query_line[6] + query_line[7]
                fetch(columns, file_name, condition)

        else:
            print("Invalid query.")


main()