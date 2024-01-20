import os
## load all the environemnt variables
from dotenv import load_dotenv
load_dotenv() 

import streamlit as st
import pandas as pd
import mysql.connector

## Configure Genai Key
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text


# Function To retrieve query results from the database
def read_sql_query(sql, db_config):
    try:
        conn = mysql.connector.connect(**db_config)
        # Check if the response contains "Wrong Input" before attempting to execute
        if "Wrong Input" in sql:
            raise ValueError("Wrong Input: The input provided is not understood. Please enter a valid question.")

        result_df = pd.read_sql(sql, conn)  # Use pandas to read SQL results into a DataFrame
        conn.close()
        return result_df
    except mysql.connector.Error as err:
        st.error(f"DatabaseError: {err}")

    except ValueError as verr:
        st.error(f"ValueError: {verr}")

## Defining the Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name Employee and has the following columns - id,name,gender,salary, 
    department \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM employee ;
    \nExample 2 - Select and print all records from the employee table, 
    the SQL command will be something like this SELECT * FROM employee; 
    \n Example 3 - Select members count for each department, 
    the SQL command will be something like this SELECT department, COUNT(*) as member_count FROM employee GROUP BY department;
    also the sql code should not have ``` in beginning or end and sql word in output
    \n If you did not understand the text entered display "Wrong Input"

    """


]

## Streamlit App

st.set_page_config(page_title="Retrieval of Any SQL query")
st.header("Retrieval of SQL Query and Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Retrieve Data")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)

    st.write(" **Query for the above text:** :sunglasses:\n \n",response)
    # Define MySQL database configuration
    mysql_config = {
        "host": "localhost",
        "user": "root",
        "password": "Srav@96*#97",
        "database": "Employee"
    }

    response_df = read_sql_query(response, mysql_config)
    st.subheader("Result")

    # Check if response_df is not None before performing operations
    if response_df is not None:
        # Display the result as a table with custom column names
        st.table(response_df.rename(columns={"id": "Employee ID", "name": "Employee Name", "gender": "Gender", "salary": "Salary", "department": "Department"}))
    else:
        st.warning("No data returned from the SQL query.")