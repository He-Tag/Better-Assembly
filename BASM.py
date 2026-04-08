while True:
    result = 0
    cmd = input("BASM>")
    signalcmd = cmd.split()[0]
    splitcmd = cmd.split()
    if signalcmd == "ADD":
        for i in range(len(splitcmd) - 1):
            splitcmd[i + 1] = float(splitcmd[i + 1])
        for i in range(len(splitcmd) - 1):
            exec(f"result += splitcmd[i + 1]")
        print(result)
    elif signalcmd == "SUB":
        for i in range(len(splitcmd) - 1):
            splitcmd[i + 1] = float(splitcmd[i + 1])
        result = splitcmd[1]
        for i in range(len(splitcmd) - 2):
            exec(f"result -= splitcmd[i + 2]")
        print(result)
    elif signalcmd == "MUL":
        for i in range(len(splitcmd) - 1):
            splitcmd[i + 1] = float(splitcmd[i + 1])
        for i in range(len(splitcmd) - 1):
            exec(f"result *= splitcmd[i + 1]")
        print(result) 
    elif signalcmd == "DIV":
        for i in range(len(splitcmd) - 1):
            splitcmd[i + 1] = float(splitcmd[i + 1])
        result = splitcmd[1]
        for i in range(len(splitcmd) - 2):
            exec(f"result /= splitcmd[i + 2]")
        print(result)
    elif signalcmd == "EXP":
        for i in range(len(splitcmd) - 1):
            splitcmd[i + 1] = float(splitcmd[i + 1])
        result = splitcmd[1] ** splitcmd[2]
        print(result)
    elif signalcmd == "PRC":
        for i in range(len(splitcmd) - 1):
            splitcmd[i + 1] = float(splitcmd[i + 1])
        result = (splitcmd[1] / 100) * splitcmd[2]
        print(result)
    elif signalcmd == "VARSTR":
        exec(f"{splitcmd[1]} = splitcmd[2]")
    elif signalcmd == "VARINT":
        splitcmd[2] = int(splitcmd[2])
        exec(f"{splitcmd[1]} = {splitcmd[2]}")
    elif signalcmd == "VARREAD":
        print(globals()[f"{splitcmd[1]}"])
