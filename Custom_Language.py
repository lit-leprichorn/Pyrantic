i=0
while True:
    file = input("File: ")
    file = file + ".pyrantic"
    with open (file,"r") as OpenFile:
        contents = OpenFile.read()
        for line in contents.split("\n"):
                i += 1
                print("run: ", i)
                parts = line.split(":",1)
                if len(parts)>1:
                    function = parts[0].strip()
                    item = parts[1].strip()
                   
                    if function == "p":
                        print(item)
                    if function == "math":
                        try:
                            math_result = eval(item)
                            print(math_result)
                        except:
                            print(item)
            
