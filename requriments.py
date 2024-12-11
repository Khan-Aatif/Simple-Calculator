import streamlit as st

def calculator():
    st.title("Simple Calculator")

    # Operation Selection
    operation = st.selectbox("Choose an operation:", ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"])

    # Input Numbers
    num1 = st.number_input("Enter the first number:", value=0.0)
    num2 = st.number_input("Enter the second number:", value=0.0)

    # Perform Calculation
    result = None
    if st.button("Calculate"):
        if operation == "Addition (+)":
            result = num1 + num2
        elif operation == "Subtraction (-)":
            result = num1 - num2
        elif operation == "Multiplication (*)":
            result = num1 * num2
        elif operation == "Division (/)":
            if num2 == 0:
                st.error("Division by zero is not allowed.")
            else:
                result = num1 / num2

        # Display the Result
        if result is not None:
            st.success(f"The result is: {result}")

calculator()
