import csv
import json
import sys

sql_cmd = sys.argv[1].split(" ")

index_select = sql_cmd.index("SELECT")+1
index_from = sql_cmd.index("FROM")+1

try:
  index_where = sql_cmd.index("WHERE")+1
except ValueError:
  index_where = -1

#print("SELECT=\t"+sql_cmd[index_select])
#print("FROM=\t"+sql_cmd[index_from])
#print("WHERE=\t"+sql_cmd[index_where])

select_ = sql_cmd[index_select].split(",")
from_ = sql_cmd[index_from]
where_ = sql_cmd[index_where].split("=")

column_name = []
column = []

with open(from_) as f:
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

if select_ == ["*"]:
  select_ = column_name

return_sql = dict()

#print(column_name)
#print(select_)

for i in select_:
  column_index = column_name.index(i)  
  return_sql[column_name[column_index]] = column[column_index]

if index_where != -1:
  index_list = []
  return_sql_ = dict()
for i in range(0,len(return_sql[where_[0]])):
    if where_[1] == return_sql[where_[0]][i]:
      index_list.append(i)

for return_ in return_sql:
    #print(return_sql[return_])
    x = []
    for index in index_list:
      #print(return_sql[return_])
      #print(index)
      x.append(return_sql[return_][index])
    return_sql[return_] = x

print(return_sql)