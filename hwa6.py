import sqlite3
from turtle import pd

database = 'database.sqlite'

conn = sqlite3.connect(database)
print('Opened data successfully')

import pandas as pd

tables = pd.read_sql("""SELECT *
                        FROM sqlite_master
                        WHERE type='table';""", conn)

print(tables)

match_details = pd.read_sql('''SELECT  Season_id,Match_id,
                            v.Venue_name, c.City_name,
t.Team_Name AS Winner
                                FROM Match 
                                Inner Join Venue AS v ON Match.Venue_id = v.Venue_id
                                Inner Join City AS c ON v.City_id = c.City_id
                                Inner Join Team AS t ON Match.Match_Winner == t.Team_id;''', conn)


print(match_details)
