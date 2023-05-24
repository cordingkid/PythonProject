import pymysql


conn = pymysql.connect(host='localhost', user='root', password='python',
                       port=3305, db='python', charset='utf8')
 

curs = conn.cursor()

sql = """insert into emp(e_id,e_name,sex,addr)
         values(%s,%s,%s,%s)"""
 
curs.execute(sql,('0','8','2','5'))
conn.commit()

sql2 = "select * from emp"
curs.execute(sql2)
rows = curs.fetchall()
print(rows)
    
curs.close()
conn.close()