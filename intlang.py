#Made by Kamil Malicki
#All rights reserved. Copyright belongs to Kamil Malicki

import sys
import os

def interpretuj(plik):
    with open(plik, 'r') as file:
        kod = file.readlines()
    RAY = 0
    RAX = 0
    line_number = 0
    RAR = [0] * 8

    def atoi_func(reg):
     global RAX, RAY
     if reg.startswith('$'):
        reg_name = reg[1:]
        if reg_name == 'RAX':
            RAX -= 48
        elif reg_name == 'RAY':
            RAY -= 48
        else:
            if reg_name.startswith('RAR[') and reg_name.endswith(']'):
                index = int(reg_name.split('[')[1][:-1])
                if 0 <= index < 8:
                    RAR[index] -= 48
                else:
                    print("SYNTAX ERROR")
            else:
                print("SYNTAX ERROR")
     else:
        print("SYNTAX ERROR")
    
    def itoa_func(reg):
     if reg.startswith('$'):
        reg_name = reg[1:]
        if reg_name == 'RAX':
            print(chr(RAX))
        elif reg_name == 'RAY':
            print(chr(RAY))
        else:
            if reg_name.startswith('RAR[') and reg_name.endswith(']'):
                index = int(reg_name.split('[')[1][:-1])
                if 0 <= index < 8:
                    print(chr(RAR[index]))
                else:
                    print("SYNTAX ERROR")
            else:
                print("SYNTAX ERROR")
     else:
        print("SYNTAX ERROR")
    
    def print_func(*args):
        nonlocal RAX
        nonlocal RAY
        for arg in args:
            if arg == '$RAX':
                print(RAX, end=' ')
            elif arg == '$RAY':
            	print(RAY, end=' ')
            else:
                print(arg, end=' ')
        print()

    while line_number < len(kod):
        linia = kod[line_number]
        instrukcja = linia.strip().split()
        
        if instrukcja[0] == 'PRINT':
            if instrukcja[1][0] == "'" and instrukcja[-1][-1] == "'":
                print_func(' '.join(instrukcja[1:])[1:-1])
            else:
                print_func(' '.join(instrukcja[1:]))
            line_number += 1

        elif instrukcja[0] == 'SET':
            RAX = int(instrukcja[1]) if instrukcja[1].isdigit() else 0
            line_number += 1

        elif instrukcja[0] == 'INC':
            RAX = RAX + 1
            line_number += 1

        elif instrukcja[0] == 'STORE':
         index = int(instrukcja[1])
         value = int(instrukcja[2])
         if 0 <= index < 8:
          RAR[index] = value
         else:
          print("SYNTAX ERROR")
         line_number += 1

        elif instrukcja[0] == 'DATA':
           index = int(instrukcja[1])
           if 0 <= index < 8:
            print(RAR[index])
           else:
            print("SYNTAX ERROR")
           line_number += 1
           
        elif instrukcja[0] == 'DOUBLE':
            RAX = RAX * 2
            line_number += 1

        elif instrukcja[0] == 'MOV':
            if instrukcja[1] == 'Y':
             RAY = RAX
             line_number += 1
            else:
             RAX = RAY
             line_number += 1

        elif instrukcja[0] == 'ITOA':
            if len(instrukcja) == 2:
                itoa_func(instrukcja[1])
            else:
                print("SYNTAX ERROR")
            line_number += 1

        elif instrukcja[0] == 'ATOI':
            if len(instrukcja) == 2:
                atoi_func(instrukcja[1])
            else:
                print("SYNTAX ERROR")
            line_number += 1
        
        elif instrukcja[0] == 'SUM':
        	RAX = RAX + RAY
        	line_number += 1
        	

        elif instrukcja[0] == 'SUB':
        	RAX = RAX - RAY
        	line_number += 1
        
        elif instrukcja[0] == 'NINC':
            RAX = RAX - 1
            line_number += 1

        elif instrukcja[0] == 'GOTO':
            line_number = int(instrukcja[1])
            line_number += 1

        elif instrukcja[0] == 'PASS':
        	line_number += 1

        elif instrukcja[0] =='CMP':
        	warunek=int(instrukcja[1])
        	if RAX==warunek and instrukcja[2]=='GOTO':
        		line_number = int(instrukcja[3])
        	elif instrukcja[2]!='GOTO':
        		print("SYNTAX ERROR")
        	else:
        		line_number += 1

        		
        elif instrukcja[0] =='RARCMP':
        	a=int(instrukcja[1])
        	b=int(instrukcja[2])
        	if RAR[a]==RAR[b] and instrukcja[3]=='GOTO':
        		line_number = int(instrukcja[4])
        	elif instrukcja[3]!='GOTO':
        		print("SYNTAX ERROR")
        	else:
        		line_number += 1
        		
        elif instrukcja[0] == 'INPUT':
            user_input = input(">")
            RAX = int(user_input) if user_input.isdigit() else 0
            line_number += 1

        elif instrukcja[0] == 'EXIT':
        	sys.exit(0)
        
        else:
        	line_number += 1
        	
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("SYNTAX ERROR")
        print("SYNTAX = in terminal: python intlang.py <file.il> ")
        sys.exit(1)
    file_name = sys.argv[1]
    
    if not file_name.endswith('.il') or not os.path.isfile(file_name):
        print("SYNTAX ERROR")
        print("SYNTAX = in terminal: python intlang.py <file.il> ")
        sys.exit(1)
    interpretuj(sys.argv[1])
    
#PĘTLA FOR    
#PASS
#SET 1
#PASS
#PRINT $RAX
#INC
#PRINT $RAX
#PASS
#CMP 10 GOTO 11
#GOTO 3
#PASS
#PASS
#EXIT
