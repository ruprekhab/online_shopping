from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Database configuration
db_config = {
    'dbname': 'online_shopping',
    'user': 'postgres',
    'password': 'password',
    'host': 'localhost',
    'port': 5432
}

#################################################
# Database Setup
#################################################
conn = psycopg2.connect(**db_config)

# Home page
@app.route('/')
def home():
    """Display instructions on how to construct query strings"""
    instructions = """
    <h1>Welcome to the API</h1>
    <p>This API allows you to query data from three tables: <strong>customer</strong>, <strong>product</strong>, and <strong>transaction</strong>.</p>
    <h3>How to Construct Query Strings:</h3>
    <ul>
        <li>To get all data from a table, use the following format:</li>
        <pre>/customer</pre>
        <pre>/product</pre>
        <pre>/transaction</pre>
        <li>To fetch transaction by date range, use the following format:</li>
        <pre>/api/transaction_date_range/<strong>YYYY-MM-DD</strong>/<strong>YYYY-MM-DD</strong></pre>
       
    </ul>
    
    """
    
    return(instructions)
    


# Dynamic API endpoint to fetch data based on table selected
@app.route('/<select_table>')
def get_data(select_table):
    tables = ['customer', 'product', 'transaction']
    if select_table in tables:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(f"SELECT * FROM {select_table}")
        data = cursor.fetchall()
        return jsonify(data)
         
     

    else:
         return jsonify({
            "error": "Invalid table name",
            "message": f"Valid table names: {tables}"
           
        })
    


# # API endpoint to fetch transactions by date range
@app.route("/api/transaction_date_range/<start>/<end>")
def date_range(start, end):
    # Define acceptable date range for transactions_date_range end point
    min_date = "2019-01-01"
    max_date = "2019-12-31"

    # Check if dates are within the acceptable range
    if start < min_date or end > max_date:
        return jsonify({
        "error": "Date range out of bounds.",
        "message": "Accepted date range: 2019-01-01 to 2019-12-31."
        })
    else:
        # Connect to the database
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        # Execute the query with parameters
        query = """
        SELECT * 
        FROM transaction 
        WHERE transaction_date >= %s AND transaction_date <= %s
        """
        cursor.execute(query, (start, end))
        
        # Fetch all results
        transactions = cursor.fetchall()
        
        # Return JSON response
        return jsonify(transactions)
        

if __name__ == '__main__':
    app.run(debug=True)