import streamlit as st
import functions

todos= functions.get_todos()

def add_todo():
    todo=st.session_state["new_todos"] +"\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("MY TODO APP")
st.subheader("This is my todo app:")
st.write("this app is increase your productivity:")


for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="enter a todo",placeholder="add new todo here...",
              on_change=add_todo,key="new_todos")