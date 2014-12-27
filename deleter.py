# -*- coding: utf-8 -*-

__author__ = 'dookim'
from model import *;
import  datetime
import os

last_index_file ="last_index.txt"
from_index = 0;
if os.path.exists(last_index_file):
    pid_file=open(last_index_file, "rw")
    from_index=int(pid_file.readline().strip());
else :
    pid_file=open(last_index_file, "w+")

start_date = datetime.date.today() + datetime.timedelta(-15)
start_date =  start_date.strftime("%Y:%m:%d %H-%M-%S")

query = "SELECT * FROM instances WHERE datetime <= '{datetime}' ORDER BY idinstance desc limit 1;".format(datetime = start_date)
#query = "SELECT * FROM instances WHERE idinstance = 1";
print query;

before_fetched = session.execute(query);
data = before_fetched.fetchone();
to_index = data[0];
path = "../poolfromworker/logpool/"

for i in range(from_index, to_index):
    file_path = path + i + ".txt"
    print file_path
    os.remove(file_path)


pid_file.write(str(to_index))
pid_file.close()