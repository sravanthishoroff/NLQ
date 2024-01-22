# SQL Query Retrieval App 🚀
 - Welcome to the Gemini SQL Query Retrieval App! This Streamlit-powered application utilizes Google's Gemini AI to convert English questions into SQL queries and retrieve data from a MySQL database.

## How It Works
Ask a Question: Enter an English question related to the Employee database.
AI Magic: Google's Gemini AI generates a SQL query based on your question.
Database Query: The app executes the generated SQL query on a MySQL database.
Results Display: View the query results presented in a table format.
Getting Started
Clone the Repository:

```bash
git clone https://github.com/sravanthishoroff/NLQ.git
cd gemini-sql-query-retrieval

Setup Environment:

- Install the required dependencies:
```bash
pip install -r requirements.txt
```

- Create a .env file and add your Google API key:
```makefile
GOOGLE_API_KEY=your_google_api_key
```
- Run the App:
```bash
streamlit run app.py
```
 Example Questions to Try
- "How many entries of records are present?"
- "Select and print all records from the employee table."
- "Select members count for each department."
  
## Error Handling
- If you provide a wrong or inappropriate input, the app will gracefully display an error message, guiding you to enter a valid question.

## Next Steps: Azure Deployment
- Stay tuned for more updates as we plan to deploy this app on Microsoft Azure for enhanced scalability and accessibility.

## Acknowledgments
Special thanks to Streamlit, Google Generative AI, and MySQL for making this project possible.
