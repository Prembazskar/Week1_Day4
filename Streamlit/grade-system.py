import streamlit as st


# -----------------------------
# Grade calculation
# -----------------------------
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# -----------------------------
# Initialize session state
# -----------------------------
if "students" not in st.session_state:
    st.session_state.students = []


# -----------------------------
# Page title
# -----------------------------
st.title("🎓 Student Grade Manager")

st.write("Add student marks and view the class performance.")


# -----------------------------
# Student input form
# -----------------------------
with st.form("student_form"):

    st.subheader("Add Student")

    name = st.text_input("Student Name")

    st.write("Enter marks for 5 subjects:")

    col1, col2 = st.columns(2)

    with col1:
        mark1 = st.number_input(
            "Subject 1",
            min_value=0.0,
            max_value=100.0,
            step=1.0
        )

        mark2 = st.number_input(
            "Subject 2",
            min_value=0.0,
            max_value=100.0,
            step=1.0
        )

        mark3 = st.number_input(
            "Subject 3",
            min_value=0.0,
            max_value=100.0,
            step=1.0
        )

    with col2:
        mark4 = st.number_input(
            "Subject 4",
            min_value=0.0,
            max_value=100.0,
            step=1.0
        )

        mark5 = st.number_input(
            "Subject 5",
            min_value=0.0,
            max_value=100.0,
            step=1.0
        )

    submitted = st.form_submit_button("Add Student")


# -----------------------------
# Process student
# -----------------------------
if submitted:

    if not name.strip():
        st.error("Please enter the student name.")

    else:

        total = mark1 + mark2 + mark3 + mark4 + mark5

        average = total / 5

        grade = calculate_grade(average)

        result = "FAIL" if grade == "F" else "PASS"

        student = {
            "Student Name": name,
            "Total": total,
            "Average": round(average, 2),
            "Grade": grade,
            "Result": result
        }

        st.session_state.students.append(student)

        st.success(f"{name} added successfully!")


# -----------------------------
# Display student results
# -----------------------------
st.subheader("📊 Student Results")

if st.session_state.students:

    st.table(st.session_state.students)

    # Get averages
    averages = [
        student["Average"]
        for student in st.session_state.students
    ]

    # Class calculations
    class_average = sum(averages) / len(averages)
    highest_average = max(averages)
    lowest_average = min(averages)

    # Display metrics
    st.subheader("📈 Class Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Class Average",
        f"{class_average:.2f}"
    )

    col2.metric(
        "Highest Average",
        f"{highest_average:.2f}"
    )

    col3.metric(
        "Lowest Average",
        f"{lowest_average:.2f}"
    )

else:

    st.info("No students added yet.")
