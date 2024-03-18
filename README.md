# Steps to operate

1. Create database in tool of choice (This used pgAdmin 4)
2. Insert data by running the table_creation.sql file
3. Make a file named 'database.ini'
   1. Input information in the form of
   2. 
        [postgresql]
        host=localhost
        database=[YOUR DATABASE NAME]
        user=[YOUR USERNAME]
        password=[YOUR PASSWORD]
4. Run main.py and follow instructions given in command line to operate script.
