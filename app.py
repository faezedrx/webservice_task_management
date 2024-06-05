import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from datetime import datetime

# تنظیمات احراز هویت
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)

# لینک به گوگل شیت شما
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1GB0HaR13Ygb14qe_wTc4DBNs_QWxegfhbRVMv-4WNto/edit?pli=1#gid=0"

# باز کردن شیت
spreadsheet = client.open_by_url(spreadsheet_url)
worksheet = spreadsheet.sheet1

# تابع برای خواندن داده‌ها از گوگل شیت
def read_data():
    data = worksheet.get_all_records()
    return pd.DataFrame(data)

# تابع برای افزودن وظیفه جدید به گوگل شیت
def add_task(task):
    df = read_data()
    new_task = pd.DataFrame([[task, '', 'pending']], columns=['Task', 'Date', 'Completed'])
    updated_df = pd.concat([df, new_task], ignore_index=True)
    worksheet.update([updated_df.columns.values.tolist()] + updated_df.values.tolist())

# تابع برای تکمیل وظیفه
def complete_task(index):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    worksheet.update_cell(index + 2, 2, current_time)  # ستون تاریخ و زمان
    worksheet.update_cell(index + 2, 3, 'done')  # ستون وضعیت

# تابع برای حذف وظیفه
def delete_task(index):
    worksheet.delete_rows(index + 2)  # +2 به دلیل اینکه گوگل شیت از ردیف 1 شروع می‌شود و ردیف هدر هم وجود دارد

# نمایش داده‌ها
data = read_data()

# فرم برای افزودن وظیفه جدید
st.header("Task Management App")
with st.form(key='add_form'):
    new_task = st.text_input('New Task')
    submit_button = st.form_submit_button(label='Add Task')

if submit_button and new_task:
    add_task(new_task)
    st.success('Task added successfully!')
    st.experimental_rerun()

# نمایش لیستی از وظایف
st.header("Tasks List")
if len(data) > 0:
    for index, row in data.iterrows():
        task_text = row['Task']
        task_date = row['Date']
        is_completed = row['Completed'] == 'done'
        
        col1, col2, col3, col4 = st.columns([4, 3, 2, 2])
        
        with col1:
            checkbox = st.checkbox(f"{task_text} (Completed on: {task_date})", value=is_completed, key=f"task_{index}")
        with col2:
            if st.button("Delete", key=f"delete_{index}"):
                delete_task(index)
                st.experimental_rerun()
        
        if checkbox and not is_completed:
            complete_task(index)
            st.experimental_rerun()
else:
    st.write("No tasks found.")

# نمایش داده‌ها به صورت جدول
st.header("Tasks Data")
st.dataframe(data)
