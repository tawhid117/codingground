'''
(02:10:48.00) 27.06.14;02.10.50;Irrad.=     0; W/qm;
(02:10:58.00) 27.06.14;02.11.00;Irrad.=   861; W/qm;
(02:11:08.00) 27.06.14;02.11.10;Irrad.=   983; W/qm;
'''

text_file = open("a.txt", "r"); words = text_file.read().split(); print words; li_rad = []; li_day = []; li_month = []; li_year = [];

for i in words:
    if i.endswith(";"):
        digit = i[:-1]
        if digit.isdigit():
            print digit
            
for i in words:
    if i.endswith("="):
        day=i[0:2]; li_day.append(day);
        month=i[3:5]; li_month.append(month);
        year=i[6:8]; li_year.append(year);
        
print "day: ", li_day, " month: ", li_month, " year: ", li_year

from datetime import datetime
print datetime.strptime('2012-02-10' , '%Y-%m-%d')
