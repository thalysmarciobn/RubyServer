import datetime


def info(output):
    print(str(datetime.datetime.now().strftime("%X")) + f" [INFO] {output}")
    return


def warn(output):
    print(str(datetime.datetime.now().strftime("%X")) + f" [WARN] {output}")
    return


def alert(output):
    print(str(datetime.datetime.now().strftime("%X")) + f" [ALERT] {output}")
    return


def session(address, output):
    print(str(datetime.datetime.now().strftime("%X")) + f" [SESSION] [{address}] {output}")
    return


def packet(action, output):
    print(str(datetime.datetime.now().strftime("%X")) + f" [PACKET] [{action}] {output}")
    return
