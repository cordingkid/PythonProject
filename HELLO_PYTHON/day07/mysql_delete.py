import pymysql


conn = pymysql.connect(host='localhost', user='root', password='python',
                       port=3305, db='python', charset='utf8')
 

e_id = "3"
e_name = "6"
sex = "6"
addr = "6"

curs = conn.cursor()
sql = f"""
delete from emp
where e_id = '{e_id}'
"""

print("sql",sql)
 
curs.execute(sql)
conn.commit()
print("행삽입 : ",curs.rowcount)
# print(curs.row)
    
curs.close()
conn.close()