import mysql.connector


class AccionesBd:
    def __init__(self, host, user, psw, db):
        self.cnn = mysql.connector.connect(host=host, user=user, 
        passwd=psw, database=db)
        self.__table = ""
        self.__columns = []
        self.__condition = ""
        self.__values = []
    
    #Conexion con la Base de datos
    def __search_all_of_a_table(self, table):
        try:
            cur = self.cnn.cursor()
            cur.execute("SELECT * FROM {}".format(table))
            data = cur.fetchall()
            cur.close()
        except:
            data = False  
        return data 
    
    def __search_all_by_condition(self, table,condition):
        try:
            cur = self.cnn.cursor()
            cur.execute("SELECT * FROM {} WHERE {}".format(table,condition))
            datos = cur.fetchone()
            cur.close() 
        except:
            return False   
        return datos
    
    def __search_by_columns(self,columns,table):
        try:
            cur = self.cnn.cursor()
            cur.execute("SELECT {} FROM {}".format(columns,table))
            data = cur.fetchall()
            cur.close() 
        except:
            return False
        return data
    
    def __search_by_columns_and_condition(self,columns,table,condition):
        try:
            cur = self.cnn.cursor()
            cur.execute("SELECT {} FROM {} WHERE {}".format(columns,table,condition))
            data = cur.fetchall()
            cur.close() 
        except:
            return False
        return data
    
    def __insert(self,table,columns,values):
        try:
            cur = self.cnn.cursor()
            cur.execute("Insert into {} {} VALUES {}".format(table,columns,values))
            n=cur.rowcount
            self.cnn.commit()    
            cur.close()
        except:
            return False
        return n  
    
    def __delete_by_condition(self,table,condition):
        try:
            cur = self.cnn.cursor()
            cur.execute("DELETE FROM {} WHERE {}".format(table,condition))
            n=cur.rowcount
            self.cnn.commit()    
            cur.close()
        except:
            return False
        return n  
    
    def __update_row(self,table,values,condition):
        cur = self.cnn.cursor()
        cur.execute("UPDATE {} SET {} WHERE {}".format(table,values,condition))
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n  
        
    
    #Setters
    def set_table(self,table):
        self.__table = table
    
    def set_columns(self,*columns):
        for col in columns:
            self.__columns.append(col)
    
    def set_condition(self,condition):
        self.__condition = condition
    
    def set_values(self,*values):
        for val in values:
            self.__values.append(val)      
    
    
    #Getters
    def get_table(self):
        return self.__table
          
    def get_columns(self):
        return self.__columns
    
    def get_specific_columns(self,*places):
        columns_return = []
        for place in places:
            try:
                columns_selected = self.__columns[place]
                columns_return.append(columns_selected)
            except:
                pass
        return columns_return
    
    def get_condition(self):
        return self.__condition
    
    def get_values(self,*place):
        if place:
            for i in place:
                return self.__values[i]
        else:
            return self.__values
    
    
    #Methods
    def __columns_to_string(self):
        to_string = self.__columns
        string_val = ""
        for string in to_string:
            string_val += string+","
        string_val = string_val[:-1]
        return string_val
    
    def __values_to_tuple_string(self):
        return str(tuple(self.get_values()))
    
    def __columns_to_insert(self):
        columns = self.__columns_to_string()
        columns = f"({columns})"
        return columns
    
    def __remove_columns(self,*columns):
        remove_list = []
        for col in columns:
            ref=self.__columns[col]
            remove_list.append(ref)
        for remove in remove_list:
            self.__columns.remove(remove)
        return True
    
    def __set_to_update(self):
        values = self.__values
        columns = self.__columns
        set_update=""
        if len(values) == len(columns):
            length = len(values)
            for i in range(length):
                set_update +=columns[i]+"="
                if type(values[i])== str:
                    set_update += "'"+values[i]+"',"
                else:
                    set_update += str(values[i])+","
            set_update = set_update[:-1]
            return set_update
        else:
            return False
    
    #Actions
    def select_all(self):
        data = self.__search_all_of_a_table(self.__table)
        if data:
            return data
        else:
            return False
    
    def select_all_by_condition(self):
        data = self.__search_all_by_condition(self.__table,self.__condition)
        if data:
            return data
        else:
            return False
        
    def select_by_columns(self):
        columns = self.__columns_to_string()
        data = self.__search_by_columns(columns,self.__table)
        if data:
            return data
        else:
            return False
    
    def select_by_columns_and_conditions(self):
        columns = self.__columns_to_string()
        data = self.__search_by_columns_and_condition(columns,self.__table,self.__condition)
        if data:
            return data
        else:
            return False
        
    def insert_value(self):
        columns = self.__columns_to_insert()
        values = self.__values_to_tuple_string()
        data = self.__insert(self.__table,columns,values)
        if data:
            return data
        else:
            return False
    
    def delete_value(self):
        data = self.__delete_by_condition(self.__table,self.__condition)
        if data:
            return data
        else:
            return False
    
    def update_values(self):
        values=self.__set_to_update()
        data = self.__update_row(self.__table,values,self.__condition)
        if data:
            return data
        else:
            return False
    
   
