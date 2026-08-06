valist = []
import random
i=0
total=0

from lang_xtras import allowed, resp

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
                    #print(function)
                    #print({repr(function)})
                    if function == "p":
                        print(item)
                    elif function == "math":
                        if not all(chars in allowed for chars in item):# checks if every character is isnide of allowed list
                            print("fuck. not again. ")
                            print(item, " ", random.choice(resp))
                            continue
                        try:
                            math_result = eval(item)
                            print(math_result)
                        except:
                            print(item)
                            
                    elif function == "d":
                        with open(file,"w") as destroy:
                            for line in file:
                                total += 1
                                for _ in range(total):
                                    destroy.write(f"{total}\n Where did it go?")
                    elif function == "val":
                        print("val is running bro") # WHY ARE YOU NOT RUNNING?????,nvm fixed
                        valist.extend(item.split(' '))
                        #print(valist)
                    
                    
                    
                    
                    
                    
