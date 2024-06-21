import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from datetime import datetime

# Authentication settings
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)

# Link to your Google Sheet
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1GB0HaR13Ygb14qe_wTc4DBNs_QWxegfhbRVMv-4WNto/edit?pli=1#gid=0"

# Open the sheet
spreadsheet = client.open_by_url(spreadsheet_url)
worksheet = spreadsheet.sheet1

# Function to read data from Google Sheet
def read_data():
    data = worksheet.get_all_records()
    return pd.DataFrame(data)

# Function to add a new task to Google Sheet
def add_task(task):
    df = read_data()
    new_task = pd.DataFrame([[task, '', 'pending']], columns=['Task', 'Date', 'Completed'])
    updated_df = pd.concat([df, new_task], ignore_index=True)
    worksheet.update([updated_df.columns.values.tolist()] + updated_df.values.tolist())
    st.success('Task added successfully!')
    st.balloons()  # Show balloons effect
    st.experimental_rerun()  # Rerun to show the updated tasks

# Function to complete a task
def complete_task(index):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    worksheet.update_cell(index + 2, 2, current_time)  # Date and time column
    worksheet.update_cell(index + 2, 3, 'done')  # Status column
    st.success('Task completed successfully!')
    st.experimental_rerun()

# Function to delete a task
def delete_task(index):
    worksheet.delete_rows(index + 2)  # +2 because Google Sheets starts from row 1 and there's a header row
    st.success('Task deleted successfully!')
    st.experimental_rerun()

# Function to edit a task
def edit_task(index, new_title):
    try:
        worksheet.update_cell(index + 2, 1, new_title)  # Title column
        st.success('Task title updated successfully!')
        st.experimental_rerun()
    except Exception as e:
        st.error(f"Error editing task title: {e}")

# Display data
st.header("Task Management App")

# Form to add a new task
with st.form(key='add_form'):
    new_task = st.text_input('New Task')
    submit_button = st.form_submit_button(label='Add Task')

if submit_button and new_task:
    add_task(new_task)

# Display task list
st.header("Tasks List")
data = read_data()
if not data.empty:
    for index, row in data.iterrows():
        task_text = row['Task']
        task_date = row['Date']
        is_completed = row['Completed'] == 'done'
        
        col1, col2, col3, col4 = st.columns([4, 3, 2, 1])
        
        with col1:
            new_task_title = st.text_input('Edit Task Title', value=task_text, key=f"edit_{index}")
            if st.button("Update Title", key=f"update_{index}"):
                edit_task(index, new_task_title)

        with col2:
            checkbox = st.checkbox(f"{task_text} (Completed on: {task_date})", value=is_completed, key=f"task_{index}")

        with col3:
            if st.button("Delete", key=f"delete_{index}"):
                delete_task(index)

        if checkbox and not is_completed:
            complete_task(index)

else:
    st.write("No tasks found.")

# Display data as a table
st.header("Tasks Data")
st.dataframe(data)
