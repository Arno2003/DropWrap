import psycopg2 as psg2
import pandas as pd
import os
from sqlalchemy import create_engine

class DataBaseHandler:
    
    # for creating a cursor, required for execution of commands
    def formConnection(self):
        try:
            conn = psg2.connect(
                database='dropoutdata',
                user= 'postgres',
                host='localhost',
                password='root',
                port=5432
            )
            cursor = conn.cursor()
            return conn, cursor
        
        except Exception as error:
            print("Connection not formed, some error occured")
            print("ERROR : ", error)
            
    # for executing the commands
    def executeCommand(self, command):
        try:
            dbh = DataBaseHandler()
            conn, cur = self.formConnection()
            cur.execute(command)
            res = cur.fetchall()
            conn.close()
            return res
        
        except Exception as error:
            print("An ERROR occured")
            print("ERROR : ", error) 

    # fetches data according to the condition list provided          
    def fetchData(self):      # conditions -> List of conditions for data fetching
        try:    
            dbh = DataBaseHandler()
            command = 'select * from public."combined_data2.csv"'
            res = dbh.executeCommand(command) 
            print(res)
        except Exception as error:
            print("ERROR : ", error, " Occured")
    
   
    # for inserting the data from a csv file        
    def insertData(self, filePath): # filePath -> location of the csv file to be read
        try:
            data = pd.read_csv(filePath)
            df = pd.read_csv(filePath)
            tableName = os.path.basename(filePath)
            
            # Define the table name in PostgreSQL
            table_name = tableName

            conn, cur = self.formConnection()
            
            # Create SQLAlchemy engine to connect to PostgreSQL
            engine = create_engine('postgresql://postgres:root@localhost:5432/dropoutdata')
            print(table_name)
            # Write the data to PostgreSQL
            df.to_sql(table_name, engine, if_exists='replace', index=False)
            
            # Close the connection
            conn.close()

        except FileNotFoundError:
            print("FILE NOT FOUND....")
            
if __name__ == "__main__":
    dbh = DataBaseHandler()
    dbh.fetchData()
    filePath = 'combined_data2.csv'
    dbh.insertData(filePath)