import MySQLdb
import pandas as pd

mysql_cn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='root', db='db_scau')
df = pd.read_sql('select * from ios_emoji;', con=mysql_cn)
mysql_cn.close()
print(df)