import pymysql


conn = pymysql.connect(host='localhost', user='root', password='python',
                       port=3305, db='python', charset='utf8')
 

e_id = "5"
e_name = "5"
sex = "5"
addr = "5"

curs = conn.cursor()
sql = f"""insert into emp(e_id,e_name,sex,addr)
         values('{e_id}','{e_name}','{sex}','{addr}')"""

print("sql",sql)
 
curs.execute(sql)
conn.commit()
print("행삽입 : ",curs.rowcount)
# print(curs.row)
    
curs.close()
conn.close()