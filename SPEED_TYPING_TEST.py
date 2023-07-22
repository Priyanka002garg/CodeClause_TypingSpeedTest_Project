from time import *
import random as r

#determine error in typing


def mistake(m_par,m_user):
    error= 0
    for i in range(len(m_par)):
        try:
            if m_par[i] != m_user[i]:
                error = error + 1
        except :
            error = error + 1
    return error

# calculate speed of typing

def speed_timing(start_time,end_time,userinput):
    time_delay = end_time - start_time
    time_RoundOff = round(time_delay,2)
    speed = len(userinput)/ time_RoundOff
    return round(speed)


string_list = ["CodeClause has industry-specific software expertise in Technology, Financial, Healthcare, Media, Manufacturing, and many other sectors. "
        "The company specializes in offering Data & Analytics, Automation AI, IoT Services, Web Designing, Web Application Development, and many more." ]


test = r.choice(string_list)
print("                                        ************ WELCOME TO SPEED TYPING TEST *************")
print()
print()
print(test)
print()
print()
time_1 = time()

# type the string

string_input = input("Enter the string: ")
time_2 = time()

# printing speed and error result

print('Typing Speed : ',speed_timing(time_1,time_2,string_input) ,"word/sec")
print('Error in typing:  ',mistake(test,string_input))


