import argparse
import csv
import os
import sqlite3


db_name = 'database.db'
db_path = f'{os.getcwd()}\\{db_name}'

# Delete DB if exist
if os.path.exists(db_path):
    os.remove(db_path)
    print(f'\nThe "{db_name}" database was recreated.\n')

# Create connection to db
db_conn = sqlite3.connect(db_name)

# Create cursor
handle = db_conn.cursor()

# Create DB schema
with db_conn:
    handle.executescript("""
        PRAGMA foreign_keys = ON;
        
        CREATE TABLE Projects(
            Name TEXT PRIMARY KEY,
            Description TEXT,
            Deadline INTEGER NOT NULL);
    
        CREATE TABLE Tasks(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Priority INTEGER NOT NULL,
            Details TEXT NULL,
            Status TEXT NOT NULL,
            Deadline INTEGER NOT NULL,
            Completed INTEGER NOT NULL,
            Project TEXT NOT NULL,
            FOREIGN KEY(Project) REFERENCES Projects(Name));
        """)

# Convert Tasks data from CSV format to list of tuples [(),]
with open('Tasks.csv', 'r') as f:
    f_csv = csv.DictReader(f, delimiter='|')
    tasks_data = [(line['Priority'], line['Details'], line['Status'], line['Deadline'],
                   line['Completed'], line['Project']) for line in f_csv]


# Convert Projects data from CSV format to list of tuples [(),]
with open('Projects.csv', 'r') as f:
    f_csv = csv.DictReader(f, delimiter='|')
    projects_data = [(line['Name'], line['Description'], line['Deadline']) for line in f_csv]

# Populate Projects table
with db_conn:
    for line in projects_data:
        handle.execute("""INSERT INTO Projects (Name, Description, Deadline) 
                          VALUES (?, ?, ?);""", line)

# Populate Tasks table
with db_conn:
    for line in tasks_data:
        handle.execute("""INSERT INTO Tasks (Priority, Details, Status, Deadline, Completed, Project) 
                          VALUES (?, ?, ?, ?, ?, ?);""", line)

parser = argparse.ArgumentParser(description='Provide name of project after -w')
parser.add_argument('-w', '--where', nargs='+', type=str, help='Enter project name', required=True)
args = parser.parse_args()

with db_conn:
    handle.execute("SELECT "
                    "Id, Priority, Details, Status, date(Deadline, 'unixepoch') AS Deadline, Completed, Project "
                    "FROM Tasks "
                    f"WHERE Project = '{' '.join(args.where)}'")
    result_set = handle.fetchall()
    if len(result_set) != 0:
        print('(Id, Priority, Details, Status, Deadline, Completed, Project)')
        for line in result_set:
            print(line)
    else:
        print(f"Tasks for '{' '.join(args.where)}' project were not found. Please check entered project name.")
db_conn.close()

# Example:   python retriever_sqlite3.py -w Magna Malesuada