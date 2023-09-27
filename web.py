import streamlit as sl
import functions as fu

todos = fu.read_file()

def add_todo():
    todos.append(sl.session_state["new_todo"] + '\n')
    fu.write_file(todos)

sl.title("My To-Do App")
sl.subheader("A little experiment")

for index, todo in enumerate(todos):
    todo_in_list = str(index) + todo
    print(todo_in_list)
    checkbox = sl.checkbox(label=todo, key=todo_in_list)
    if checkbox:
        todos.pop(index)
        fu.write_file(todos)
        del sl.session_state[todo_in_list]
        sl.experimental_rerun()


sl.text_input(label="", placeholder="Write new todo here...",
              key="new_todo", on_change=add_todo)

sl.session_state
