import numpy as np
import pandas as pd
import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
print('Opened data successfully')

tables = pd.read_sql("""SELECT *
                 FROM SQLite_master
                    WHERE type='table';""", conn)

print(tables)

Joined_city = pd.read_sql("""SELECT c.Country_id, c.Country_Name, ci.City_Name
                        FROM Country c
                        INNER JOIN City ci
                        ON c.Country_id = ci.Country_id;""", conn)

print(Joined_city)

Joined_left = pd.read_sql("""SELECT *
                          FROM player
                          LEFT JOIN season
                          ON player.player_id = season.MAN_of_the_series;""", conn)

print(Joined_left) 

Joined_cross = pd.read_sql("""SELECT c.Country_id, c.Country_Name, ci.City_Name
                        FROM Country c
                        CROSS JOIN City ci;""", conn)

print(Joined_cross)

union = pd.read_sql("""SELECT player_name
                        FROM player
                        UNION
                        SELECT Team_name
                        FROM team;""", conn)

print(union)