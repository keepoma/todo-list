from functions import read_file, write_file
import time

now = time.strftime("%Y, %b. %d,  %H:%M,%S")
print(f"It's {now}")
while True:
    user_action = input("Do you want to add, view, edit, complete or exit? ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = read_file()
        if ',' in todo:
            temp_todos = todo.split(', ')
            [todos.append(i.capitalize() + "\n") for i in temp_todos]
        else:
            todos.append(todo.capitalize() + "\n")
        write_file(todos)

    elif user_action.startswith("view"):
        todos = read_file()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            printed = f"{index + 1}. {item}"
            print(printed)

    elif user_action.startswith("edit"):
        todos = read_file()
        try:
            to_edit = int(user_action[5:])
            to_edit = to_edit - 1
            todo_to_remove = todos[to_edit].strip("\n")
            replacement = input("What should we edit it to? ")
            todos[to_edit] = replacement + "\n"
            print(f"Todo {todo_to_remove} has been replaced with {replacement}")
            write_file(todos)

        except ValueError:
            print("Your command is not valid.")

    elif user_action.startswith("complete"):
        todos = read_file()
        try:
            to_complete = user_action[9:]
            to_complete = to_complete.replace(",", "")
            for i in to_complete:
                i = int(i)
                todos.pop(i - 1)
            for index, item in enumerate(todos):
                item = item.strip("\n")
                printed = f"{index + 1}. {item}"
                print(printed)
            write_file(todos)

        except IndexError:
            print("No such value.")

        except ValueError:
            print("Please input the number of the todo to complete")

    elif user_action.startswith("exit"):
        break

    else:
        print("Undefined command")

print("Bye!")
