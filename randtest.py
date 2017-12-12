from random import randrange
import time
import os
import sys
import random

#start = time.perf_counter()
#randomNum = randrange(0, 9223372036854775807)

#key_num32 = random.SystemRandom().randint(0, (2**31 -1))
#key_num64 = random.SystemRandom().randint(0, (2**63 -1))
#key_num128 = random.SystemRandom().randint(0, (2**127 -1))
#key_num256 = random.SystemRandom().randint(0, (2**255 -1))
#key_num512 = random.SystemRandom().randint(0, (2**511 -1))
#key_num1024 = random.SystemRandom().randint(0, (2**1023 -1))
#key_num = random.SystemRandom().randint(0, (2**4095 -1))


#print key_num.random() #produces a number between 0 and 1


#print(bin(key_num))
def num16():
    start = time.perf_counter()
    key_num16 = random.SystemRandom().randint(0, (2**15 -1))
    #print (key_num16) 
    end = time.perf_counter()
    TIMER = (end-start)*1000
    print("Time in milliseconds for 16 bit integer:\t %.12f\n" %TIMER)
    return TIMER
def num32():
    start = time.perf_counter()
    key_num32 = random.SystemRandom().randint(0, (2**31 -1))
    #print (key_num32) 
    end = time.perf_counter()
    TIMER = (end-start)*1000
    print("Time in milliseconds for 32 bit integer:\t %.12f\n" %TIMER)
    return TIMER
def num64():
    start = time.perf_counter()
    key_num64 = random.SystemRandom().randint(0, (2**63 -1))
    #print (key_num64) 
    end = time.perf_counter()
    TIMER = (end-start)*1000
    print("Time in milliseconds for 64 bit integer:\t %.12f\n" %TIMER)
    return TIMER
def num128():
    start = time.perf_counter()
    key_num128 = random.SystemRandom().randint(0, (2**127 -1))
    #print (key_num128) 
    end = time.perf_counter()
    TIMER = (end-start)*1000
    print("Time in milliseconds for 128 bit integer:\t %.12f\n" %TIMER)
    return TIMER
def num256():
    start = time.perf_counter()
    key_num256 = random.SystemRandom().randint(0, (2**255 -1))
    #print (key_num256) 
    end = time.perf_counter()
    TIMER = (end-start)*1000
    print("Time in milliseconds for 256 bit integer:\t %.12f\n" %TIMER)
    return TIMER

def main():
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    print("\n--------------------------------------------------------------------")
    for i in range(1,11):
        print("%s) " %i , end='')
        a1 = num16()
        a += a1    
    aAVG = a/10    
    print("\n--------------------------------------------------------------------")
    for i in range(1,11):
        print("%s) " %i , end='')
        b1 = num32()
        b += b1    
    bAVG = b/10 
    print("\n--------------------------------------------------------------------")
    for i in range(1,11):    
        print("%s) " %i , end='')
        c1 = num64()
        c += c1    
    cAVG = c/10 
    print("\n--------------------------------------------------------------------")
    for i in range(1,11):
        print("%s) " %i , end='')
        d1 = num128()
        d += d1    
    dAVG = d/10 

    print("\n--------------------------------------------------------------------")
    for i in range(1,11):
        print("%s) " %i , end='')
        e1 = num256()
        e += e1    
    eAVG = e/10 

    print("-----------------------------Average Times in MILLISECONDS--------------------------------")
    print("16bit number average time:\t %.12f\n" %aAVG)
    print("32bit number average time:\t %.12f\n" %bAVG)
    print("64bit number average time:\t %.12f\n" %cAVG)
    print("128bit number average time:\t %.12f\n" %dAVG)
    print("256bit number average time:\t %.12f\n" %eAVG)

main()

