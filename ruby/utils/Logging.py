import datetime


def info(output):
    print(str(datetime.datetime.now().strftime("%X")) + " [INFO] " + output)
    return


def warn(output):
    print(str(datetime.datetime.now().strftime("%X")) + " [WARN] " + output)
    return


def alert(output):
    print(str(datetime.datetime.now().strftime("%X")) + " [ALERT] " + output)
    return


def session(address, output):
    print(str(datetime.datetime.now().strftime("%X")) + " [SESSION] [" + address + "] " + output)
    return


def packet(action, output):
    print(str(datetime.datetime.now().strftime("%X")) + " [PACKET] [" + action + "] " + output)
    return
