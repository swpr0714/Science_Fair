import csv
import numpy as np
file_group = ['table2001.csv', 'table2002.csv', 'table2003.csv', 'table2004.csv',
              'table2005.csv', 'table2006.csv', 'table2007.csv', 'table2008.csv',
              'table2009.csv', 'table2010.csv', 'table2011.csv', 'table2012.csv',
              'table2013.csv', 'table2014.csv', 'table2015.csv', 'table2016.csv', 
              'table2017.csv', 'table2018.csv', 'table2019.csv', 'table2020.csv']
with open('ouput.csv', 'w', newline='',encoding='utf-8') as output_file:
    writer = csv.writer(output_file)
    for file in file_group:
        list_press_str, list_press_int, all_press_min= [], [], []
        list_speed_str, list_speed_int, all_speed_max= [], [], []
        list_50kt_str, list_50kt_int, all_50kt_max= [], [], []
        list_35kt_str, list_35kt_int, all_35kt_max= [], [], [] 
        index = 2
        with open(file, newline='',encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            name = [row[5] for row in reader]
            csvfile.close
        with open(file, newline='',encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            press = [row[9] for row in reader]
            csvfile.close
        with open(file, newline='',encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            speed = [row[10] for row in reader]
            csvfile.close
        with open(file, newline='',encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            speed_50kt = [row[12] for row in reader]
            csvfile.close
        with open(file, newline='',encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            speed_35kt = [row[15] for row in reader]
            csvfile.close
        length = len(name)
        while (index<length):
            if name[index]==name[index-1]:
                list_press_str.append(press[index])
                list_speed_str.append(speed[index])
                list_50kt_str.append(speed_50kt[index])
                list_35kt_str.append(speed_35kt[index])
                index += 1
            else:
                index += 1
                for str_press in list_press_str:
                    int_press = int(str_press)
                    list_press_int.append(int_press)
                for str_speed in list_speed_str:
                    int_speed = int(str_speed)
                    list_speed_int.append(int_speed)
                for str_speed_50kt in list_50kt_str:
                    int_speed_50kt = int(str_speed_50kt)
                    list_50kt_int.append(int_speed_50kt)
                for str_speed_35kt in list_35kt_str:
                    int_speed_35kt = int(str_speed_35kt)
                    list_35kt_int.append(int_speed_35kt)
                all_press_min.append(min(list_press_int))
                all_speed_max.append(max(list_speed_int))
                all_50kt_max.append(max(list_50kt_int))
                all_35kt_max.append(max(list_35kt_int))
                list_press_str, list_press_int = [], []
                list_speed_str, list_speed_int = [], []
                list_50kt_str, list_50kt_int = [], []
                list_35kt_str, list_35kt_int = [], []
        writer.writerow([file])
        writer.writerow(all_press_min)
        writer.writerow(all_speed_max)
        writer.writerow(all_50kt_max)
        writer.writerow(all_35kt_max)
print ("DONE")