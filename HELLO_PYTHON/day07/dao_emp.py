import pymysql

class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',
                       port=3305, db='python', charset='utf8')
        
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)

    def selectList(self):
        sql = """
        select 
            e_id,
            e_name,
            sex,
            addr 
        from emp"""
        self.curs.execute(sql)
        
        list = self.curs.fetchall()
        return list
    
    def selectOne(self,e_id):
        sql = f"""
        select 
            e_id,
            e_name,
            sex,
            addr 
        from emp 
        where e_id = {e_id}
        """
        self.curs.execute(sql)
        
        one = self.curs.fetchone()
        return one
    
    def insert(self,e_id,e_name,sex,addr):
        sql = f"""
        insert into 
            emp(
                e_id,
                e_name,
                sex,
                addr)  
            values(
                {e_id},
                {e_name},
                {sex},
                {addr})
        """
        self.curs.execute(sql)
        self.conn.commit()
        return self.curs.rowcount
    
    def update(self, e_id, e_name, sex, addr):
        sql = f"""
        update emp
        set
            e_name = {e_name},
            sex = {sex},
            addr = {addr}
        where e_id = {e_id}
        """
        self.curs.execute(sql)
        self.conn.commit()
        return self.curs.rowcount
    
    def delete(self,e_id):
        sql = f"""
        delete from emp
        where e_id = {e_id}
        """
        self.curs.execute(sql)
        self.conn.commit()
        return self.curs.rowcount
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
# ======================================================================
        # main에서 되는지 안되는지 검사 하기
# ======================================================================
if __name__ == '__main__':
    de = DaoEmp()
    list = de.selectList()
    print("list",list)
    
    one = de.selectOne("1")
    print(one)
    print(de.insert("6", "6", "6", "6"))
    print(de.update("5", "7", "7", "7"))
    print(de.delete("4"))
