# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 16:49:59 2020

@author: Diana
"""
import numpy as np;

global R0
global R1
global R2
global R3

R0 = 33
R1 = 55
R2 = 97
R3 = 123

def txt_in_list():
    B = []
    f = open('111.txt')
    for line in f.readlines():
        line = line.replace("\n","").replace(",","")
        A = line.split(" ")
        B.append(A)
    return B

def output():
    PC = 0
    line_list = txt_in_list()
    for i in line_list:
        TC = 0
        PC += 1
        command = i[0]
        if command == "mov":
            TC = 1
            elem2 = i[1]
            elem2_1_1 = 0
            if elem2 == "R0":
                elem2_1_1 = int(R0)
            elif elem2 == "R1":
                elem2_1_1 = int(R1)
            elif elem2 == "R2":
                elem2_1_1 = int(R2)
            elif elem2 == "R3":
                elem2_1_1 = int(R3)
            else:
                elem2_1_1 = int(i[1])
            print("IR : ", i[0], i[1])
            elem2_1 = np.binary_repr(elem2_1_1, 12)
            print("A =  ", elem2_1)
            print("R0 = ", np.binary_repr(R0, 12))
            print("R1 = ", np.binary_repr(R1, 12))
            print("R2 = ", np.binary_repr(R2, 12))
            print("R3 = ", np.binary_repr(R3, 12))
            print("PC = ", PC)
            print("TC = ", TC)
            if int(elem2_1_1) >= 0:
                print("PS =  +")
            elif int(elem2_1_1) < 0:
                print("PS =  -")
            
        elif command == "add":
            elem3 = i[1]
            if elem3 == "R0":
                elem3 = int(R0)
            elif elem3 == "R1":
                elem3 = int(R1)
            elif elem3 == "R2":
                elem3 = int(R2)
            elif elem3 == "R3":
                elem3 = int(R3)
            else:
                elem3 = int(i[1])           
            elem3_1 = np.binary_repr(elem3, 12)
            v = np.binary_repr(bin_to_dec(elem2_1) + bin_to_dec(elem3_1), 12)
            if elem2_1_1 + elem3 < 4096:
                l = []
                l = list(str(v))
                print("IR : ", i[0], i[1])
                if len(l) > 12:
                    print("A =  ", v[1::])
                else:
                    print("A =  ", v)
                print("R0 = ", np.binary_repr(R0, 12))
                print("R1 = ", np.binary_repr(R1, 12))
                print("R2 = ", np.binary_repr(R2, 12))
                print("R3 = ", np.binary_repr(R3, 12))
                TC = 2
                print("PC = ", PC)
                print("TC = ", TC)
                if l[0] == "0":
                        print("PS =  +")
                elif l[0] == "1":
                        print("PS =  -")
            else:
                print("Введите число меньше")
        else:
            print("Таких комманд нет")  
            
def bin_to_dec(k): 
    length=len(k) 
    number_dec=0
    for i in range(0, length): 
        number_dec=number_dec+int(k[i])*(2**(length-i-1)) 
    return number_dec

output()