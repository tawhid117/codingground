# -*- coding: utf-8 -*-
"""
Spyder Editor

This file shows a simplified calculator created by tkinter
Last update: 04 August 2017

directory = 'E:\GoogleDrive-LenovoSSD\CodingPractice1\Python\Calculator\'

"""
status = 'no input'      # denotes the status of user activity
operator = 'undefined'   # holds the operator + - * /

import os
import tkinter as t

root = t.Tk()

lab_title = t.Label (root, text='Your input: ', justify='left', height=3, fg='red2', font=(20)).grid(row=0, column = 0)
lab_num_1 = t.Label(root, text="...", fg='gray88', font=(20)  ).grid(row = 0, column = 1)
lab_oper = t.Label(root, text='...', fg='gray88', font=(20)).grid(row=0, column=2)
lab_num_2 = t.Label(root, text='...', fg='gray88', font=(20)).grid(row=0, column=3)
lab_result_str = t.Label(root, text='The result is: ', fg='red2', font =(20) ).grid(row=1, column=0, columnspan=3)


    
def func_ip_num(digit):
    global status
    cwd = os.getcwd()
    
    if status == 'no input' or status == 'results shown':
        
        cwf = cwd + 'num_1.txt'; f = open(cwf, 'w'); f.write(' ');   f.close()  # delete data from files
#        f = open(r'E:\GoogleDrive-LenovoSSD\CodingPractice\Python\Calculator\num_1.txt', 'w'); f.write(' ');   f.close()  # delete data from files
        cwf = cwd + 'num_2.txt'; f = open(cwf, 'w'); f.write(' ');   f.close()  # delete data from files
#        f = open(r'E:\GoogleDrive-LenovoSSD\CodingPractice\Python\Calculator\num_2.txt', 'w'); f.write(' ');   f.close()   # delete data from files
        cwf = cwd + 'sym.txt'; f = open(cwf, 'w'); f.write('no-operator');   f.close()  # delete data from files
#        f = open(r'C:\Users\Tawhid\Desktop\sym.txt', 'w'); f.write('no-operator');   f.close()     # delete data from files     
        lab_num_1 = t.Label(root, text=".....................", fg='gray88', font=(20) ).grid(row = 0, column = 1)  # erase label text
        lab_num_2 = t.Label(root, text="......................", fg='gray88', font=(20) ).grid(row = 0, column = 1)  # erase label text
        lab_oper = t.Label(root, text="......................", fg='gray88', font=(20) ).grid(row = 0, column = 1)  # erase label text

        cwf = cwd + 'num_1.txt'; f = open(cwf, 'a'); f.write(digit); f.close()  # write in file
        f = open(cwf, 'r') ; x = str( f.readlines()[0]  );   f.close()   # read from file
        
        lab_num_1 = t.Label(root, text=x, fg='green4', font=(20) ).grid(row = 0, column = 1)            # update label text
        status = 'num 1 running'                                               # change status
        print ('if 1')
    
    elif status == 'num 1 running':
        cwf = cwd + 'num_1.txt'; f = open(cwf, 'a'); f.write(digit); f.close()          # write in file
        cwf = cwd + 'num_1.txt'; f = open(cwf, 'r') ; x = str( f.readlines()[0]  );   f.close()  # read from file
        lab_num_1 = t.Label(root, text="..............", fg='gray88', font=(20) ).grid(row = 0, column = 1)   # erase label text
        lab_num_1 = t.Label(root, text=x, fg='green4', font=(20) ).grid(row = 0, column = 1)                                       # update lable text
        print ('if 2')
        
    elif status == 'operator provided':
        
        cwf = cwd + 'num_2.txt'; f = open(cwf, 'a'); f.write(digit); f.close()  # write in file
        cwf = cwd + 'num_2.txt'; f = open(cwf, 'r'); x = str( f.readlines()[0] ); f.close()  # read from file
        
        lab_num_2 = t.Label(root, text="..............", fg='gray88', font=(20) ).grid(row = 0, column = 3)  # erase label text
        lab_num_2 = t.Label(root, text=x, fg='blue2', font=(20) ).grid(row = 0, column = 3)            # update label text
       
        status = 'num 2 running'                 # change status
        print ('if 3')
        
        
    elif status == 'num 2 running':
        cwf = cwd + 'num_2.txt'; f = open(cwf, 'a'); f.write(digit); f.close()                 # write in file
        cwd = cwd + 'num_2.txt'; f = open(cwf, 'r'); x = str( f.readlines()[0]  ); f.close()   # read from file
        lab_num_2 = t.Label(root, text="..............", fg='gray88', font=(20) ).grid(row = 0, column = 3)  # erase label text
        lab_num_2 = t.Label(root, text=x, fg='blue2', font=(20) ).grid(row = 0, column = 3)            # update label text
        print ('if 4') 
        
           
def func_ip_sym(op):
    global status, operator
    
    cwd = os.getcwd()
    cwf = cwd + 'sym.txt'; f = open(cwf, 'w'); f.write(op); f.close()   # write operator in file
    
    lab_oper = t.Label(root, text="..............", fg='gray88', font=(20) ).grid(row = 0, column = 2)  # erase label text
    lab_oper = t.Label(root, text = op, fg = 'black', font=(25) ).grid(row = 0, column = 2)            # update label text 

    operator = op    
    status = 'operator provided'
    print('in func_ip_sym')        

def func_show_result():
    global status, operator
    
    cwd = os.getcwd()
    x = 0; y = 0;
    cwf = cwd + 'num_1.txt'; f = open(cwf, 'r'); num_1 = f.readlines()[0]; f.close() # read num 1
    if num_1 != ' ': 
        x = int(str(num_1) ); 

    cwf = cwd + 'num_2.txt'; f = open(cwf, 'r'); num_2 = f.readlines()[0]; f.close() # read num 2
    if num_2!=' ': 
        y = int(str(num_2) );
    
    cwf = cwd + 'sym.txt'; f = open(cwf, 'r'); op = str ( f.readlines()[0]   ); f.close()       # read oper
    print('show in: ____ ')
   
    lab_result_str = t.Label(root, text='.............................................................................................................................................', fg='gray88', font =(20) ).grid(row=1, column=0, columnspan=3)

    if num_1 == ' ' or num_2 == ' ' or op == 'no-operation': result = 'illegal input'
    
    if  num_1 != ' ' and num_2 != ' ':
        if operator=='+': result = x + y 
        elif operator=='-': result = x - y
        elif operator=='*': result = x * y
        elif operator=='/': 
            if y != 0: result = x / y; 
            if y == 0: result = 'illegal iinput'
    
    
    
    lab_result_str = t.Label(root, text='The result is:        ' + str(num_1) + '   ' + op + '   ' + str(num_2) + '   =   ' + str(result), fg='khaki4', font =('comic sans ms', 13, 'italic') ).grid(row=1, column=0, columnspan=3)
    
    status = 'results shown'

def func_AC():
    global status, operator
    
    cwd = os.getcwd()
    status = 'no input'      # denotes the status of user activity
    operator = 'undefined'   # holds the operator + - * /
    
    lab_num_1 = t.Label(root, text='?', fg='red2', font=(20) ).grid(row = 0, column = 1)            # update label text for AC
    lab_num_2 = t.Label(root, text='#', fg='red2', font=(20) ).grid(row = 0, column = 3)            # update label text for AC
    lab_sym = t.Label(root, text='!', fg='black', font=(20) ).grid(row = 0, column = 2)            # update label text for AC


# buttons in row=2: 9 8 7 +    
b9 = t.Button(root, text='9', width = 7, command=(lambda: func_ip_num('9') ) ).grid(row=2, column=0)
b8 = t.Button(root, text='8', width = 7, command=(lambda: func_ip_num('8') ) ).grid(row=2, column=1)
b7 = t.Button(root, text='7', width = 7, command=(lambda: func_ip_num('7') ) ).grid(row=2, column=2)
b_plus = t.Button(root, text='+', width = 7, command=(lambda: func_ip_sym('+') ) ).grid(row=2, column=3)

# buttons in row=3: 6 5 4 -
b6 = t.Button(root, text='6', width = 7, command=(lambda: func_ip_num('6') ) ).grid(row=3, column=0)
b5 = t.Button(root, text='5', width = 7, command=(lambda: func_ip_num('5') ) ).grid(row=3, column=1)
b4 = t.Button(root, text='4', width = 7, command=(lambda: func_ip_num('4') ) ).grid(row=3, column=2)
b_min = t.Button(root, text='-', width = 7, command=(lambda: func_ip_sym('-') )).grid(row=3, column=3)

# buttons in row=4: 3 2 1 *
b3 = t.Button(root, text='3', width = 7, command=(lambda: func_ip_num('3') ) ).grid(row=4, column=0)
b2 = t.Button(root, text='2', width = 7, command=(lambda: func_ip_num('2') ) ).grid(row=4, column=1)
b1 = t.Button(root, text='1', width = 7, command=(lambda: func_ip_num('1') ) ).grid(row=4, column=2)
b_mult = t.Button(root, text='*', width = 7, command=(lambda: func_ip_sym('*') )).grid(row=4, column=3)

# buttons in row=5: AC 0 = /
b0 = t.Button(root, text='0', width = 7, command=(lambda: func_ip_num('0') ) ).grid(row=5, column=1)
b_div = t.Button(root, text='/', width = 7, command=(lambda: func_ip_sym('/') )).grid(row=5, column=3)
b_equal = t.Button(root, text='=', width = 7, command=(lambda: func_show_result() ) ).grid(row=5, column=2)
b_del = t.Button(root, text='AC', width = 7, command=(lambda: func_AC() ) ).grid(row=5, column=0)     # delete all data and clear labels


root.mainloop()
