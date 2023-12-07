# SQL Data model and qoptimization

- The aim of this project was to create a data model for Digital Bibliography and Library Project (DBLP) and query the databse.
- It is a bibligraphy database of computer science papers with over 3 million papers. In this project, we will be querying the database for information about papers,
authors, conferences, and more.

# Overview
- Extract data from the gzip files provided and replace the file path with the path from your local machine
- Create tables in your database of choice. We have used PostgreSQL for this project
- Create primary and foreign key relationship between proceedings, inproceedings, and publications tables
- Load the data using SQLAlchemy engine to PostgreSQL db
- Query the uploaded data to find interesting insights about the various publications, authors, releases and citings

## Example screenshot of inproceedings table creation and data loaded via python

![Screenshot 2023-12-07 at 12 18 01 PM](https://github.com/meetapandit/sql_optimization_project/assets/15186489/c4b3b3ac-20e1-4f4b-8bfb-bc17f494aab9)
