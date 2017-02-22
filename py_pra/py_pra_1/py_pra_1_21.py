# -*- coding: utf-8 -*-

# ue no cooding ha itiou kaiteoku

# Python_pra_1_21.py
# 2016.5.18
# Yusuke_Kato

# 1-100 hit number!!
# limit 5
# 999 = exit

import random   # for_random_value

def KazuGame():
    seikai = random.randint(1,100)  # create_Correct_Answer
    for i in ["1","2","3","4","5"]: # 1-5 Loop
        print("---------------")
        print(" times : " + i)  # Output_times
        print("---------------")
        input_num = input(' Input(num) > ') # Input_string
        n = int(input_num)  # int_convertion
        if n == 999:    # exit
            print(" exit")
            break
        if n == seikai: # game_clear
            print("\nWWWWWWWWWWWW")
            print(" !!Great!!")
            print("MMMMMMMMMMMM\n")
            break
        if i == "5": # 5times_notClear
            print("\n\n That's too bad............\n")
            str_seikai = str(seikai) # str_convertion
            print("\n Correct Answer : " + str_seikai + "\n") # Output_Correct_Answer
            break
        if n > seikai - 5 and n < seikai + 5: # seikai-5 < inputNumber < seikai+5
            print(" Regrettable！")
        if n > seikai:
            print(" n > seikai")
        if n < seikai:
            print(" n < seikai")

if __name__ == "__main__":

    KazuGame()
    print("\n END \n")
            
    
    
