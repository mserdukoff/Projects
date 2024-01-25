import math
import datetime

time_arr = (
            (1,"una"),
            (2,"due"),
            (3,"tre"),
            (4,"quattro"),
            (5,"cinque"),
            (6,"sei"),
            (7,"sette"),
            (8,"otto"),
            (9,"nove"),
            (10,"dieci"),
            (11,"ondici"),
            (12,"dodici")
                            )


usr = input("Enter a time to translate into Italian. (Enter 0 to quit)\n")

while usr != '0':
    if usr == '0':
        break
    else:
        time = datetime.datetime.strptime(usr, "%H:%M")
    if time.hour < 12:
        if time.minute == 0:
            print("Sono le " + time_arr[time.hour - 1][1] + " in punto.")
        elif time.minute == 5:
            print("Sono le " + time_arr[time.hour - 1][1] + " e cinque.")
        elif time.minute == 10:
            print("Sono le " + time_arr[time.hour - 1][1] + " e dieci.")
        elif time.minute == 15:
            print("Sono le " + time_arr[time.hour - 1][1] + " e un quarto.")
        elif time.minute == 20:
            print("Sono le " + time_arr[time.hour - 1][1] + " e venti.")
        elif time.minute == 25:
            print("Sono le " + time_arr[time.hour - 1][1] + " e venticinque.")
        elif time.minute == 30:
            print("Sono le " + time_arr[time.hour - 1][1] + " e mezza.")
        elif time.minute == 35:
            print("Sono le " + time_arr[time.hour - 1][1] + " e trentacinque.")
        elif time.minute == 40:
            print("Sono le " + time_arr[time.hour][1] + " meno venti.")
        elif time.minute == 45:
            print("Sono le " + time_arr[time.hour][1] + " meno un quarto.")
        elif time.minute == 50:
            print("Sono le " + time_arr[time.hour][1] + " meno dieci.")
        elif time.minute == 55:
            print("Sono le " + time_arr[time.hour+1][1] + " meno cinque.")
    else:
        if time.minute == 0:
            print("Sono le " + time_arr[time.hour - 1][1] + " in punto.")
        elif time.minute == 5:
            print("Sono le " + time_arr[time.hour - 1][1] + " e cinque.")
        elif time.minute == 10:
            print("Sono le " + time_arr[time.hour - 1][1] + " e dieci.")
        elif time.minute == 15:
            print("Sono le " + time_arr[time.hour - 1][1] + " e un quarto.")
        elif time.minute == 20:
            print("Sono le " + time_arr[time.hour - 1][1] + " e venti.")
        elif time.minute == 25:
            print("Sono le " + time_arr[time.hour - 1][1] + " e venticinque.")
        elif time.minute == 30:
            print("Sono le " + time_arr[time.hour - 1][1] + " e mezza.")
        elif time.minute == 35:
            print("Sono le " + time_arr[time.hour - 1][1] + " e trentacinque.")
        elif time.minute == 40:
            print("Sono le " + time_arr[time.hour - 1][1] + " e quaranta.")
        elif time.minute == 45:
            print("Sono le " + time_arr[time.hour - 1][1] + " e quarantacinque.")
        elif time.minute == 50:
            print("Sono le " + time_arr[time.hour - 1][1] + " e cinquanta.")
        elif time.minute == 55:
            print("Sono le " + time_arr[time.hour - 1][1] + " e cinquantacinque.")

    usr = input("\nEnter another or 0 to quit.\n")