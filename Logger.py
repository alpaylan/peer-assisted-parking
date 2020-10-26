from time import ctime, time
import os

session = 0
def startLog():
    global session

    t = str(ctime(time()))
    t = t.replace(" ", "_").replace(":", "_")

    session = t
    os.system("mkdir -p logs/" + t)

def logCritical(message):
    opt = {"type": "critical"}
    log(message, opt)

def logPrintln(message):
    logPrint(message + "\n")

def logPrint(message):
    opt = {"type": "print"}
    log(message, opt)

def logResult(message):
    opt = {"type": "result"}
    log(message, opt)

def logDebug(message):
    opt = {"type": "debug"}
    log(message, opt)

def log(message, options):
    global session
    f = open("logs/" + session + "/log_" + options["type"] + ".txt", "a")
    f.write(message)
    f.close()

def clr_log():
    global session
    os.system("rmdir -r logs/" + session)
