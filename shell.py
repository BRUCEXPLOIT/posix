import sys
import os
import subprocess

def main():

    while True:
        sys.stdout.write("$ ")  # Correctly format the prompt without extra space
        sys.stdout.flush()     # Ensure the prompt is flushed to the output
        user_command = input()
        splitter=user_command.split(" ")#lets say the input is 'exit 4' the split function splits the sentence to words i.e splitter=['exit','4']
        if splitter[0]=="exit":
            if len(splitter)>1 and splitter[1].isdigit():#checks the number of elements in the splitter is more than 1 and check the second argument is integer value only
                sys.exit(int(splitter[1]))
        if splitter[0]=="echo":
            sys.stdout.write(" ".join(splitter[1:]) + "\n")
            continue
        if splitter[0]=="type":
            for e in splitter[1:]:
                if e == "echo":
                    print("echo is a shell builtin")
                elif e == "exit":
                    print("exit is a shell builtin")
                elif e == "type":
                    print("type is a shell builtin")

                else:
                    found = False
                    for path in os.getenv("PATH").split(":"):
                        if os.path.isdir(path):
                            for f in os.listdir(path):
                                if f == splitter[1]:
                                    print(f"{splitter[1]} is {path}/{splitter[1]}")
                                    found=True
                                    break
                        if found:
                            break
                    if not found:
                        print(f"{e}: not found")
            continue
        else:
            found=False
            for path in os.getenv("PATH").split(os.pathsep):
                if os.path.isdir(path):
                    for f in os.listdir(path):
                        if f == splitter[0]:
                            result=subprocess.run(splitter,capture_output=True,text=True)
                            print(result.stdout,end="")
                            found=True
                            break
                if found:
                    break
            if not found:
                print(f"{user_command}: command not found")








if __name__ == "__main__":
    main()
