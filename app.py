import zmq
from datatime import datatime

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    message = socket.recv()

    current = time.CLOCK_REALTIME





if __name__ == "__name__":
    main()