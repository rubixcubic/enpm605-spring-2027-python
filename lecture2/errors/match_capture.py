STOP = "stop"
command = "forward"

match command:
    case STOP:
        print("Stopping")
    case _:
        print("Another command")
