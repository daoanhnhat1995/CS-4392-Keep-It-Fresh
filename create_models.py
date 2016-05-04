import pandas as pd
from pandas.io import sql
from db.models import db_connect

conn = db_connect().raw_connection()
data = sql.read_sql("SELECT restaurant_id  from violations",conn)
print(data)
conn.close()


