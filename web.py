import streamlit as sl
import functions as fu

todos = fu.read_file()

def add_todo():
    todos.append(sl.session_state["new_todo"] + '\n')
    fu.write_file(todos)


sl.title("My To-Do App")
sl.subheader("A little experiment")

for todo in todos:
    sl.checkbox(todo)

sl.text_input(label="", placeholder="Write new todo here...",
              key="new_todo", on_change=add_todo)

sl.session_state
