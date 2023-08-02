import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"   # st.session stores value entered by user.
    todos.append(todo)
    functions.write_todos(todos)

# order matters here
st.title("My To Do App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]  #it deletes from session_state
        st.experimental_rerun()



st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")  # label should always be given something even an empty string.
