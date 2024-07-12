import sys
import os
import subprocess

def executable_exist(file) -> tuple:
    PATH = os.environ["PATH"]
    paths = PATH.split(":")
    for path in paths:
        filepath = os.path.join(path,file)
        if os.path.isfile(filepath):
            return True, filepath
    else:
        return False, None

def main():
    buitin_commands = ['exit','echo', 'type','pwd','cd']
    
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        total_command = input()
        command = total_command.split()[0]
        arguments = total_command.split()[1:]
        if command == "exit":
            sys.exit()
        elif command == "echo":
            print(*arguments)
            # print(' '.join(arguments))
        elif command == "type":
            # if len(arguments) > 0:
            #     print(*(f"{arguments[i]} is a shell builtin\n" if arguments[i] in buitin_commands else f"{arguments[i]}: not found\n" for i in range(len(arguments))))
            if len(arguments) > 0:
                for i in range(len(arguments)):
                    if arguments[i] in buitin_commands:
                        print(f"{arguments[i]} is a shell builtin")
                    else:
                        exist, filepath = executable_exist(arguments[i])
                        if exist:
                            print(f"{arguments[i]} is {filepath}")
                        else:
                            print(f"{arguments[i]}: not found")
            else:
                print("",end='')
        elif command == "pwd":
            print(os.getcwd())
        elif command == "cd":
            if len(arguments)>0:
                if arguments[0].startswith("~"):
                    # home_path = os.environ.get("HOME")
                    # # full_path = os.path.join(home_path,arguments[0][1:])
                    # full_path = arguments[0].replace("~",home_path)
                    full_path = os.path.expanduser(arguments[0])
                    os.chdir(full_path)
                elif os.path.isdir(arguments[0]):
                    #os module support both absolute and relative path
                    os.chdir(arguments[0])
                else:
                    print(f"cd: {arguments[0]}: No such file or directory")
            else:
                os.chdir(os.environ.get("HOME"))
        else:
            exist, filepath = executable_exist(command)
            if exist:
                exex_command = [filepath] + arguments
                # result = subprocess.run(exex_command, stdout=subprocess.PIPE, text=True)
                # print(result.stdout)
                subprocess.run(exex_command)
            else:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
