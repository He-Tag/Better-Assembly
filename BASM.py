while True:
    result = 0
    if ifexec == False:
        cmd = input("BASM>")
        signalcmd = cmd.split()[0]
        splitcmd = cmd.split()
    elif ifexec == True:
        cmd = secondhalfcmd
        signalcmd = cmd.split()[0]
        splitcmd = cmd.split()
        ifexec = False
    if signalcmd == "ADD":
        try:
            for i in range(len(splitcmd) - 1):
                splitcmd[i + 1] = float(splitcmd[i + 1])
            for i in range(len(splitcmd) - 1):
                exec(f"result += splitcmd[i + 1]")
        except ValueError:
            for i in range(len(splitcmd) - 1):
                exec(f"result += {splitcmd[i + 1]}")
        print(result)
    elif signalcmd == "SUB":
        try:
            for i in range(len(splitcmd) - 1):
                splitcmd[i + 1] = float(splitcmd[i + 1])
            result = splitcmd[1]
            for i in range(len(splitcmd) - 2):
                exec(f"result -= splitcmd[i + 2]")
        except ValueError:
            for i in range(len(splitcmd) - 2):
                exec(f"result = result + {splitcmd[i + 1]} - {splitcmd[i + 2]}")
        print(result)
    elif signalcmd == "MUL":
        try:
            for i in range(len(splitcmd) - 1):
                splitcmd[i + 1] = float(splitcmd[i + 1])
            for i in range(len(splitcmd) - 1):
                exec(f"result *= splitcmd[i + 1]")
        except ValueError:
            for i in range(len(splitcmd) - 1):
                exec(f"result *= {splitcmd[i + 1]}")
        print(result) 
    elif signalcmd == "DIV":
        try:
            for i in range(len(splitcmd) - 1):
                splitcmd[i + 1] = float(splitcmd[i + 1])
            result = splitcmd[1]
            for i in range(len(splitcmd) - 2):
                exec(f"result /= splitcmd[i + 2]")
        except ValueError:
            for i in range(len(splitcmd) - 2):
                exec(f"result = result + {splitcmd[i + 1]} / {splitcmd[i + 2]}")
        print(result)
    elif signalcmd == "EXP":
        try:
            for i in range(len(splitcmd) - 1):
                splitcmd[i + 1] = float(splitcmd[i + 1])
            result = splitcmd[1] ** splitcmd[2]
        except ValueError:
            result = {splitcmd[1]} ** {splitcmd[2]}
        print(result)
    elif signalcmd == "PRC":
        try:
            for i in range(len(splitcmd) - 1):
                splitcmd[i + 1] = float(splitcmd[i + 1])
            result = (splitcmd[1] / 100) * splitcmd[2]
        except:
            result = ({splitcmd[1]} / 100) * {splitcmd[2]}
        print(result)
    elif signalcmd == "VARSTR":
        exec(f"{splitcmd[1]} = splitcmd[2]")
    elif signalcmd == "VARINT":
        splitcmd[2] = int(splitcmd[2])
        exec(f"{splitcmd[1]} = {splitcmd[2]}")
    elif signalcmd == "VARFLOAT":
        splitcmd[2] = float(splitcmd[2])
        exec(f"{splitcmd[1]} = {splitcmd[2]}")
    elif signalcmd == "VARREAD":
        print(globals()[f"{splitcmd[1]}"])
    elif signalcmd == "IF":
        firsthalfcmd, secondhalfcmd = cmd.split(":")
        firsthalfcmd = firsthalfcmd.split()
        try:
            if firsthalfcmd[2] == "=":
                if firsthalfcmd[1] == firsthalfcmd[3]:
                    ifexec = True
            elif firsthalfcmd[2] == "!":
                if firsthalfcmd[1] != firsthalfcmd[3]:
                    ifexec = True
            elif firsthalfcmd[2] == ">":
                if firsthalfcmd[1] > firsthalfcmd[3]:
                    ifexec = True
            elif firsthalfcmd[2] == ">=":
                if firsthalfcmd[1] >= firsthalfcmd[3]:
                    ifexec = True
            elif firsthalfcmd[2] == "<":
                if firsthalfcmd[1] < firsthalfcmd[3]:
                    ifexec = True
            elif firsthalfcmd[2] == "<=":
                if firsthalfcmd[1] <= firsthalfcmd[3]:
                    ifexec = True
        except ValueError:
            if globals()[f"{firsthalfcmd[2]}"] == "=":
                if globals()[f"{firsthalfcmd[1]}"] == globals()[f"{firsthalfcmd[3]}"]:
                    ifexec = True
            elif globals()[f"{firsthalfcmd[2]}"] == "!":
                if globals()[f"{firsthalfcmd[1]}"] != globals()[f"{firsthalfcmd[3]}"]:
                    ifexec = True
            elif globals()[f"{firsthalfcmd[2]}"] == ">":
                if globals()[f"{firsthalfcmd[1]}"] > globals()[f"{firsthalfcmd[3]}"]:
                    ifexec = True
            elif globals()[f"{firsthalfcmd[2]}"] == ">=":
                if globals()[f"{firsthalfcmd[1]}"] >= globals()[f"{firsthalfcmd[3]}"]:
                    ifexec = True
            elif globals()[f"{firsthalfcmd[2]}"] == "<":
                if globals()[f"{firsthalfcmd[1]}"] < globals()[f"{firsthalfcmd[3]}"]:
                    ifexec = True
            elif globals()[f"{firsthalfcmd[2]}"] == "<=":
                if globals()[f"{firsthalfcmd[1]}"] <= globals()[f"{firsthalfcmd[3]}"]:
                    ifexec = True
