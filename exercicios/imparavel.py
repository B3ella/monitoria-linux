import signal

def sig(*_):
    print("não :)")

signal.signal(signal.SIGINT, sig)

while True:
    continue
