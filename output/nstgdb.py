import csv
import json
import sys
class Nstgdb:
  printf_func = print
  nstgdb_sql_crud_cmd = None
  nstgdb_sql_crud = None
  nstgdb_sql_from = None
  nstgdb_sql_where = None

  column_name = []
  column = []

  #Functions to decompose SQL statements
  def nstgdb_cmd_parse(self, sql_cmd):
    self.printf_func("DEBUG", self.__class__.__name__ + "."+ sys._getframe().f_code.co_name +" ->")
    self.printf_func("INFO", "Command = \"" + sql_cmd + "\"")
    
    sql_cmd_s = sql_cmd.split(" ")

    index_crud_cmd = 0
    self.nstgdb_sql_crud_cmd = self.nstgdb_crud_check(sql_cmd_s)
    index_crud = sql_cmd_s.index(self.nstgdb_sql_crud_cmd)+1
    index_from = sql_cmd_s.index("FROM")+1

    try:
      index_where = sql_cmd_s.index("WHERE")+1
    except ValueError:
      index_where = -1

    self.nstgdb_sql_crud_cmd = sql_cmd_s[index_crud_cmd]
    self.nstgdb_sql_crud = sql_cmd_s[index_crud].split(",")
    if self.nstgdb_sql_crud == ["*"]:
      self.nstgdb_sql_crud = column_name
    self.nstgdb_sql_from = sql_cmd_s[index_from]
    if index_where != -1:
      self.nstgdb_sql_where = sql_cmd_s[index_where].split("=")

    self.printf_func("DEBUG", "SRUB = \"" + self.nstgdb_sql_crud_cmd + "\", " + "SRUB_ = \"" + ",".join(self.nstgdb_sql_crud) + "\"")
    self.printf_func("DEBUG", "FROM = \"" + self.nstgdb_sql_from + "\"")
    if not(self.nstgdb_sql_where is None):
      self.printf_func("DEBUG", "WHERE = \"" + ",".join(self.nstgdb_sql_where) + "\"")

    self.printf_func("DEBUG", self.__class__.__name__ + "."+ sys._getframe().f_code.co_name +" <-")

  def nstgdb_crud_check(self, sql_cmd_s):
    self.printf_func("DEBUG", self.__class__.__name__ + "."+ sys._getframe().f_code.co_name +" ->")
    try:
      index_crud = sql_cmd_s.index("SELECT")
    except ValueError:
      index_crud = -1
    try:
      index_crud = sql_cmd_s.index("UPDATE")
    except ValueError:
      index_crud = index_crud
    self.printf_func("DEBUG", "CRUD: " + sql_cmd_s[index_crud])
    self.printf_func("DEBUG", self.__class__.__name__ + "."+ sys._getframe().f_code.co_name +" <-")
    return sql_cmd_s[index_crud]

  def nstgdb_openfile(self):
    self.printf_func("DEBUG", self.__class__.__name__ + "."+ sys._getframe().f_code.co_name +" ->")

    column_name = ""
    column = []

    with open(self.nstgdb_sql_from) as f:
      reader = csv.reader(f)
      i = 0
      for row in reader:
        if i == 0:
          column_name = row
          for j in range(len(column_name)):
            column.append([])
        else:
          for j in range(len(column_name)):
            column[j].append(row[j])
        i+=1

    self.column_name = column_name
    self.column = column

    self.printf_func("DEBUG", self.__class__.__name__ + "."+ sys._getframe().f_code.co_name +" <-")

  def nstgdb_select(self):
    self.printf_func("DEBUG", self.__class__.__name__ + "."+ sys._getframe().f_code.co_name +" ->")

    column_name = self.column_name
    column = self.column

    return_sql = dict()
    for i in range(len(column_name)):
      return_sql[column_name[i]] = column[i]
    
    if not(self.nstgdb_sql_where is None):
      index_list = self.nstgdb_where(return_sql)
      return_sql_ = dict()      
      for return_ in return_sql:
        x = []
        for index in index_list:
          x.append(return_sql[return_][index])
        return_sql[return_] = x

    for i in range(1):
      return_sql_ = dict()
      for j in self.nstgdb_sql_crud:
        return_sql_[j] = return_sql[j]
      return_sql = return_sql_
      break

    print(return_sql)

    self.printf_func("DEBUG", self.__class__.__name__ + "."+ sys._getframe().f_code.co_name +" <-")

  def nstgdb_where(self,return_sql):
    self.printf_func("DEBUG", self.__class__.__name__ + "."+ sys._getframe().f_code.co_name +" ->")

    index_list = []
    return_sql_ = dict()
    for i in range(0,len(return_sql[self.nstgdb_sql_where[0]])):
      if self.nstgdb_sql_where[1] == return_sql[self.nstgdb_sql_where[0]][i]:
        index_list.append(i)


    self.printf_func("DEBUG", self.__class__.__name__ + "."+ sys._getframe().f_code.co_name +" <-")
    return index_list


  def nstgdb_run(self, sql_cmd):
    self.printf_func("DEBUG", self.__class__.__name__ + "."+ sys._getframe().f_code.co_name +" ->")
    self.nstgdb_cmd_parse(sql_cmd)
    self.nstgdb_openfile()
    self.nstgdb_select()
    self.printf_func("DEBUG", self.__class__.__name__ + "."+ sys._getframe().f_code.co_name +" <-")

  def test(self):
    print()


  def __init__(self, printf_func = None):
    if not(printf_func is None):
      self.printf_func = printf_func
    self.printf_func("DEBUG", self.__class__.__name__ + "."+ sys._getframe().f_code.co_name +" ->")
    self.printf_func("DEBUG", self.__class__.__name__ + "."+ sys._getframe().f_code.co_name +" <-")