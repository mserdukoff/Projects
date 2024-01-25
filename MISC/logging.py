# program that contains code for making a log file
import datetime
import os.path

# returns boolean if file found or not
log_file = 'log.txt'
path = './log.txt'

# if file exists write to it, if it doesnt, create it
if os.path.isfile(path):
    f = open(log_file, 'a')
    now = datetime.datetime.now()
    f.write("Program Started: " + now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
    f.write("Run Status: \t")
else:
    f = open(log_file, "x")
    now = datetime.datetime.now()
    f.write("Program Started: " + now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
    f.write("Run Status:\n")

# print directly to log file with timestamp
def log(string):
    f.write("\t" + "'" + string + "'" + "   @ " + now.strftime("%Y-%m-%d %H:%M:%S") + "\n")

log("something")
