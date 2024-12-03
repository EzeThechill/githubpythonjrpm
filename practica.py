import time



def countdown(time_sec):
    #print(f"You have {num} to save the world")
    print("WE COUNT ON YOU")

    while time_sec :
        mins, sec = divmod(time_sec,60)
        timeformat = "{:02d}:{:02d}".format(mins, sec)
        print(timeformat, end="\r")
        time.sleep(1)
        time_sec = time_sec - 1
    
print("BOOOOOOOMMMMMM!!!!!!")

num=int(input("Set your timer in sec : "))
countdown(num)