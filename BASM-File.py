#File-Mode
executingcode = True
ifexec = False
callexec = 0
looploops = 0
loopinf = False
currentline = -1
with open('basmfile.txt', 'r') as basmfile:
    lines = basmfile.readlines()
    while executingcode == True:
        try:
            result = None
            if ifexec == True:
                cmd = secondhalfcmd
                signalcmd = cmd.split()[0]
                splitcmd = cmd.split()
                ifexec = False
            elif callexec > 0:
                cmd = cmdlist[0]
                signalcmd = cmd.split()[0]
                splitcmd = cmd.split()
                del cmdlist[0]
                callexec = callexec -1
            elif looploops > 0:
                looploops = looploops - 1
                if loopinf == True:
                    looploops += 1
                cmd = loopedcmd
                signalcmd = cmd.split()[0]
                splitcmd = cmd.split()
            else:
                currentline += 1
                try:
                    cmd = lines[currentline]
                except:
                    break
                signalcmd = cmd.split()[0]
                splitcmd = cmd.split()
            if signalcmd == "ADD":
                try:
                    for i in range(len(splitcmd) - 1):
                        splitcmd[i + 1] = float(splitcmd[i + 1])
                    for i in range(len(splitcmd) - 1):
                        exec(f"result += splitcmd[i + 1]")
                except ValueError:
                    for i in range(len(splitcmd) - 1):
                        exec(f"result += {splitcmd[i + 1]}")
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
            elif signalcmd == "MUL":
                try:
                    for i in range(len(splitcmd) - 1):
                        splitcmd[i + 1] = float(splitcmd[i + 1])
                    for i in range(len(splitcmd) - 1):
                        exec(f"result *= splitcmd[i + 1]")
                except ValueError:
                    for i in range(len(splitcmd) - 1):
                        exec(f"result *= {splitcmd[i + 1]}")
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
            elif signalcmd == "EXP":
                try:
                    for i in range(len(splitcmd) - 1):
                        splitcmd[i + 1] = float(splitcmd[i + 1])
                    result = splitcmd[1] ** splitcmd[2]
                except ValueError:
                    result = {splitcmd[1]} ** {splitcmd[2]}
            elif signalcmd == "PRC":
                try:
                    for i in range(len(splitcmd) - 1):
                        splitcmd[i + 1] = float(splitcmd[i + 1])
                    result = (splitcmd[1] / 100) * splitcmd[2]
                except:
                    result = ({splitcmd[1]} / 100) * {splitcmd[2]}
            elif signalcmd == "VARSTR":
                exec(f"{splitcmd[1]} = {splitcmd[2]}")
            elif signalcmd == "VARINT":
                splitcmd[2] = int(splitcmd[2])
                exec(f"{splitcmd[1]} = {splitcmd[2]}")
            elif signalcmd == "VARFLOAT":
                splitcmd[2] = float(splitcmd[2])
                exec(f"{splitcmd[1]} = {splitcmd[2]}")
            elif signalcmd == "VARREAD":
                print(globals()[f"{splitcmd[1]}"])
            elif signalcmd == "IF":
                firsthalfcmd, secondhalfcmd = cmd.split(":", 1)
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
            elif signalcmd == "DEF":
                executedcode = cmd.split(":", 1)[1]
                globals()[f"{splitcmd[1]}"] = executedcode.split(";")
            elif signalcmd == "CALL":
                cmdlist = globals()[f"{splitcmd[1]}"]
                callexec = len(cmdlist)
            elif signalcmd == "INC":
                globals()[f"{splitcmd[1]}"] += 1
            elif signalcmd == "DEC":
                globals()[f"{splitcmd[1]}"] -= 1
            elif signalcmd == "LOOP":
                if splitcmd[1] == "INF":
                    loopinf = True
                else:
                    looploops = int(splitcmd[1])
                loopedcmd = cmd.split(":", 1)[1]
            elif signalcmd == "END":
                executingcode = False
            elif signalcmd == "JMP":
                currentline = (int(splitcmd[1]) - 2)
            elif signalcmd == "INP":
                try:
                    globals()[f"{splitcmd[2]}"] = 0
                    globals()[f"{splitcmd[2]}"] = input(f"{splitcmd[1]}")
                except:
                    globals()[f"{splitcmd[1]}"] = input()
            elif signalcmd == "VARLST":
                listvalues = splitcmd[2:]
                globals()[f"{splitcmd[1]}"] = listvalues
            try:   
                globals()[f"{splitcmd[3]}"] = result
            except:
                try:
                    print(int(result))
                except:
                        if result != None:
                            print(result)
        except Exception as code_execution_exception:
            print(f"The Program just tried to execute line {currentline + 1} of the code that raised an Error: {code_execution_exception}")
            print(f"Line that raised a problem: {lines[currentline]}")
            break
