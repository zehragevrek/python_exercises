# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Assignment 4 : Task Management ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# For this assignment, your objective is to create a Python program for a team manager to efficiently manage the team tasks. 
# The system should allow users to perform the following operations, adding tasks, assigning team members, completing tasks, generating a report with
# overall and task times The project tasks are organized in a recursive structure.
    
def init_tasks():
    return [
        {'id': 1, 'description': "Complete Project Proposal", 'assigned_to': "John Doe", "subtasks": [
            {'id': 2, 'description': "Research", 'assigned_to': "Alice Brown", 'time_estimate': 5},
            {'id': 3, 'description': "Outline", 'assigned_to': "Bob Johnson", 'subtasks': [
                {'id': 4, 'description': "Introduction", 'assigned_to': "Jane Smith", 'time_estimate': 3},
                {'id': 5, 'description': "Body", 'assigned_to': "Jane Smith", 'time_estimate': 6},
                {'id': 6, 'description': "Conclusion", 'assigned_to': "David Wilson", 'time_estimate': 2}
            ]}
        ]}]


def get_user_input():
    selection = input("Operations:\n"
"   1. Add a new task\n"
"   2. Assign a task to a team member\n"
"   3. Complete a task\n"
"   4. Generate report\n"
"   5. Exit\n"
"Please select an operation: ")

    return selection


def display_tasks(tasks, recursion_number):
    for i in tasks:
        if recursion_number != 0:
            print("--" * recursion_number, end="")
        print(f"{i['id']}. {i['description']} ({i['assigned_to']})")

        if 'subtasks' in i:
            recursion_number += 1
            return f"{display_tasks(i['subtasks'], recursion_number)}"


def add_task_recursive(tasks, new_id, new_description, new_assigned_to, new_time_estimate):
    if new_id == "0":
        for i in tasks:
            pass
        max_id = display_tasks(tasks, 0)[-1]['id']
        tasks.append({'id': max_id + 1, 'description': new_description, 'assigned_to': new_assigned_to, 'time_estimate': new_time_estimate})
    else:
        for i in tasks:
            if i['id'] == new_id - 1:
                if 'subtasks' not in i:
                    i['subtasks'] = [{'id': new_id, 'description': new_description, 'assigned_to': new_assigned_to, 'time_estimate': new_time_estimate}]
                else:
                    pass
            elif 'subtasks' in i:
                add_task_recursive(i['subtasks'], new_id, new_description, new_assigned_to, new_time_estimate)



def assign_task(tasks, selected_id, new_assigned_to):
    for i in tasks:
        if i['id'] == int(selected_id):
            i['assigned_to'] = new_assigned_to
            return i['description']
        elif 'subtasks' in i:
            return assign_task(i['subtasks'], selected_id, new_assigned_to)


def complete_task_recursive(tasks, selected_id):
    for i in tasks:
        if i['id'] == int(selected_id):
            i['completed'] = True
            return i['description']
        elif 'subtasks' in i:
            return complete_task_recursive(i['subtasks'], selected_id)


def calculate_time_recursive(tasks, total_time, remained_time):
    for i in tasks:
        if 'time_estimate' not in i:
            i['total_time'], i['remainded_time'] = calculate_time_recursive(i['subtasks'], 0, 0)
        elif 'completed' in i:
            total_time += i['time_estimate']
        else:
            total_time += i['time_estimate']
            remained_time += i['time_estimate']

        return total_time, remained_time


def generate_report_recursive(tasks, recursion_number):

    for i in tasks:
        if recursion_number != 0:
            print("--" * recursion_number)
        if 'subtasks' not in i:
            time = i['time_estimate']
            if 'completed' in i:
                print(f"{i['id']}. {i['description']} ({i['assigned_to']}) -- Estimated Time to Finish: "
                      f"0 out of {time} hours, Completed")
            else:
                print(f"{i['id']}. {i['description']} ({i['assigned_to']}) -- Estimated Time to Finish: "
                      f"{time} out of {time} hours, Pending")
        else:
            recursion_number += 1
            total_time, remained_time = calculate_time_recursive(i['subtasks'], 0, 0)
            if remained_time == 0:
                print(f"{i['id']}. {i['description']} ({i['assigned_to']}) -- Estimated Time to Finish: "
                      f"0 out of {total_time} hours, Completed")
            else:
                print(f"{i['id']}. {i['description']} ({i['assigned_to']}) -- Estimated Time to Finish: "
                      f"{remained_time} out of {total_time} hours, Pending")





def main(selection=None):


    while selection != "5":
        if selection == None:
            tasks = init_tasks()

        selection = get_user_input()

        if selection == "1":
            print("0. New Task")
            display_tasks(tasks, 0)
            new_id = input("To add a new task, enter 0. To add a subtask, select the task ID: ")
            new_description = input("Please enter the task description: ")
            new_assigned_to = input("Please enter the task responsible: ")
            new_time_estimate = input("Please enter the estimated time for the task: ")
            add_task_recursive(tasks, new_id, new_description, new_assigned_to, new_time_estimate)
            print("New task Xs added.")




        elif selection == "2":
            display_tasks(tasks, 0)
            selected_id = input("Please select a task: ")
            new_assigned_to = input("Please enter the new team members name: ")
            task_name = assign_task(tasks, selected_id, new_assigned_to)
            print(f"Task {task_name} assigned to {new_assigned_to}.")




        elif selection == "3":
            display_tasks(tasks, 0)
            selected_id = input("Enter task ID: ")
            task_name = complete_task_recursive(tasks, selected_id)
            print(f"Task '{task_name}' marked as completed.\nPlease press enter to continue.")


        elif selection == "4":
            generate_report_recursive(tasks, 0)


        elif selection == "5":
            break
        else:
            print("Invalid input. Please enter a selection again.")
            selection = get_user_input()

main()


