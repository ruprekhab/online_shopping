# Data Engineering Project: E-commerce Sales Data Pipeline
## Authors: Ruprekha Baruah, Vidushi Bundhooa, Saba Alaeddini 
## Project Overview
This project demonstrates a comprehensive data engineering pipeline designed to analyze e-commerce sales data. The project follows best practices in data cleaning, normalization, and database design, enabling efficient storage and retrieval for further analysis. A Flask API has been created to interface with the database.

## Data Source: 
The dataset for this project was sourced from Kaggle. It includes information on customer transactions, products, and customer demographics. Link to the database:
https://www.kaggle.com/datasets/jacksondivakarr/online-shopping-dataset

## Files and Folders:
1) Images Folder
    * Contains the image of the Entity-Relationship Diagram (ERD) that represents the database schema, a functional block diagram illustrating the operational workflow, a system block diagram for the API, detailing its components and their interactions..
2) Output Folder
    * Stores the customer, product, and transaction CSV files. These files are prepared for import into the PostgreSQL database.
3) Resources Folder
    * Holds the raw data in a CSV format, which serves as the starting point for the data processing workflow.
4) App.py
    * Contains the FLASK API script used to provide endpoints for interacting with the processed data.
5) data_new.js
    * Includes the processed data, which is used for creating interactive visualizations with JavaScript and HTML.
6) data_visualization.py
    * Connects to the PostgreSQL database using SQLAlchemy and queries the tables using Pandas.
    * Further processes the data and exports it as a JavaScript file (data_new.js) for use in interactive visualizations.   
7) Data.ipynb
    * A Jupyter Notebook used for data cleaning and preparation.
    * Normalization forms were applied to create the customer, product, and transaction data frames.
    * These data frames are exported as CSV files in the Output Folder for later use in PostgreSQL.
8) index.html
    * The HTML file that runs the JavaScript script (data_new.js) to render the visualizations.
9) Plot.js
    * Contains the JavaScript code to create interactive visualizations.
10) schema.sql
    * Contains the PostgreSQL database schema, including the table definitions and relationships.
    * Used to set up the database structure before importing the processed data.
11) installed_packages.txt  
    * A text file listing all Python packages installed in the environment.
    * It can be used to replicate the environment using pip install -r installed_packages.txt
    


## Extact, Transform, Load 
1. Data Extraction: The raw CSV file was imported and loaded into a Pandas DataFrame for further processing and analysis.
2. Data Cleaning: The data cleaning process was performed in Python using the Pandas library. The following steps were undertaken to ensure the dataset's quality and usability:
    * Unnecessary Columns Removal: Dropped irrelevant or redundant columns that were not required for the analysis.
    * Data Type Conversion: Converted the transaction_date column to the appropriate datetime format for accurate temporal analysis.
    * Handling Missing Data: Rows with missing values were removed to maintain data integrity, ensuring reliable results in subsequent analysis.
    * Column Renaming: Renamed columns to more descriptive and standardized names for better readability and consistency.
      
3. Data Normalization: To design our database, we implemented normalization up to the Third Normal Form (3NF) to ensure data consistency, reduce redundancy, and simplify maintenance.
    * First Normal Form (1NF): We ensured all columns contain atomic values.
    * Second Normal Form (2NF): All non-key attributes were made fully functionally dependent on the primary key. A new id column with unique values was added as a primary key to the tranasction table. 
    * Third Normal Form (3NF): We verified the absence of transitive dependencies, ensuring that all non-key attributes directly depend solely on the primary key and not on any other non-key attributes.

4. Output: Normalized tables were exported as CSV files for further processing and integration into the database.
5. Database Schema Design: The database schema was designed using QuickDBD for relational datsbase design. Primary keys were assigned to uniquely identify each record in a table, while foreign keys were established to define relationships between tables. 
6. Database Creation: A new PostgreSQL database was created using the designed schema.
The exported CSV files were imported into the corresponding tables, populating the database with cleaned, normalized data.
7. Flask API Development: API built with Flask interfaces with the PostgreSQL database, providing endpoints for retrieving specific datasets. The API's home page offers detailed instructions on how to query the database for different use cases.
8. Interactive Visualizations: The data was further processed and exported to Javascript file. An interactive vizualization was created using HTML and JavaScript where users can explore sales per category by selecting a month from a dropdown menu.

   
## Advantages of Choosing PostgreSQL for This Project
PostgreSQL was chosen for this project due to its robust features and suitability for handling complex data relationships in a relational database. Key reasons include:
* Advanced Features: PostgreSQL supports a wide range of data types, powerful querying capabilities, making it ideal for managing and analyzing structured datasets.
* Reliability and Scalability: Known for its high reliability, PostgreSQL efficiently handles large datasets and concurrent users, ensuring scalability for future growth.
* Open Source: As an open-source database, PostgreSQL provides a cost-effective solution.
* Compatibility with Analytical Tools: PostgreSQL seamlessly integrates with Python libraries such as Pandas and SQLAlchemy, enabling efficient data extraction and analysis.
* Data Normalization: PostgreSQL's relational structure allows adherence to normalization principles, ensuring minimal redundancy and optimal storage.

## Ethical Considerations Addressed in the Project:
The data used in this project was sourced from Kaggle, a reputable platform for public datasets. The dataset did not include any personal information about customers, maintaining privacy and compliance. Efforts were made to ensure that the results accurately reflected the characteristics and patterns within the dataset without favoring any particular outcome or demographic.The analysis was conducted to avoid introducing or reinforcing any biases that could lead to misleading conclusions. 

## Instructions for Using the Project
1. Clone the Repository:
git clone https://github.com/ruprekhab/online_shopping.git

2. Set Up the Environment:
    * Install the required Python libraries:
        pip install -r installed_packages.txt
    * Ensure PostgreSQL is installed and running. Import the database schema from schema.sql file and data using the CSV files in the output folder.

3. Run the Flask Application:
    * Start the Flask server: python app.py
    * Ensure you have configured your database connection properly. Use your PostgreSQL password in the password field of your configuration
    * Access the API at http://localhost:5000/. The API's home page provides instructions for retrieving data.

4. View and interact with the Visualizations: Open the index.html file in your web browser. Select a month from the dropdown to view sales by category.

## Technologies Used

Languages: Python, SQL, HTML, JavaScript

Libraries/Packages: Pandas, Psycopg2, SQLAlchemy, Flask, Plotly

Database: PostgreSQL

Tools: QuickDBD (for ERD design), Lucid Chart (for Block Diagram), CSV(for raw data storage and exchange)






    










