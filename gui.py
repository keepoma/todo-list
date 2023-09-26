import functions as fu
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.Input(tooltip="Type here", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label, input_box, add_button]],
                   font=("Helvetica", 16))

while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = fu.read_file()
            todos.append(values["todo"] + "\n")
            fu.write_file(todos)
        case sg.WIN_CLOSED:
            break

window.close()
