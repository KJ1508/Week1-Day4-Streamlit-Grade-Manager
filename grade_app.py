
import streamlit as st


def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    return "F"


st.set_page_config(page_title="Student Grade Manager")
st.title("Student Grade Manager")

if "students" not in st.session_state:
    st.session_state.students = []

with st.form("student_form", clear_on_submit=True):
    name = st.text_input("Student Name")
    mark = st.number_input("Mark", value=0, step=1)
    submitted = st.form_submit_button("Add Student")

if submitted:
    if not name.strip():
        st.error("Please enter a student name.")
    elif not 0 <= mark <= 100:
        st.error("Mark must be between 0 and 100.")
    else:
        st.session_state.students.append({
            "Name": name.strip(),
            "Mark": mark,
            "Grade": get_grade(mark)
        })
        st.success("Student added successfully!")

students = st.session_state.students

if students:
    st.subheader("Student Results")
    st.table(students)

    marks = [student["Mark"] for student in students]
    col1, col2, col3 = st.columns(3)

    col1.metric("Class Average", f"{sum(marks) / len(marks):.1f}")
    col2.metric("Highest Mark", max(marks))
    col3.metric("Lowest Mark", min(marks))
else:
    st.info("Add students to see their results.")