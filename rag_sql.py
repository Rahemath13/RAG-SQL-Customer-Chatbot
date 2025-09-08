from openai import OpenAI
import re

# ✅ Use your API key properly
client = OpenAI( "ADD YOUR API KEY HERE")
def ask_question(question):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a SQL assistant for a customer database. "
                    "Always explain the answer and then output the SQL query in this exact format:\n"
                    "`SQL query is: <your SQL>`"
                )
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    result = response.choices[0].message.content

    # ✅ If the AI follows the format
    if "SQL query is:" in result:
        sql_query = result.split("SQL query is:")[1].strip()
    else:
        # ✅ Fallback: regex to find any SELECT ... ;
        sql_match = re.search(r"SELECT[\s\S]*?;", result, re.IGNORECASE)
        if sql_match:
            sql_query = sql_match.group().strip()
        else:
            sql_query = "No SQL query found."

    return result, sql_query
