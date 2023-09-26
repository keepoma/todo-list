import functions as fu
import PySimpleGUI as sg

label = sg.Text("To-do")
input_box = sg.Input(tooltip="Type here", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=fu.read_file(), key='todos',
                      enable_events=True, size=(40, 12))
edit_button = sg.Button("Edit")

window = sg.Window("My To-Do App",
                   layout=[[label, input_box, add_button],
                           [list_box, edit_button]],
                   font=("Helvetica", 16))

while True:
    event, values = window.read()
    print("Event:", event)
    print("Values", values)
    print("---")
    match event:
        case 'Add':
            todos = fu.read_file()
            todos.append(values["todo"] + "\n")
            fu.write_file(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            new_todo = values['todo']
            todo_to_edit = values['todos'][0]
            todos = fu.read_file()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            fu.write_file(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
