#!/bin/env python
import os
import sys
import time
from colorama import Fore
from colorama import Style

i = True

def ft_show_help():
    print("\nWelcome to the HELP DOC!\n")
    print("----------------------------------\n")
    print("This script helps you to make the start of your project faster.\n")
    print("Here the basics options :\n")
    print("- For any new project, a .gitignore file is generated.\n")

    print("- If you want to create a new C project, a src dir, a Makefile and a lib directory are automatically generated.\n")

    print("- However, for a non C project, all of this options above are not automatically generated\n")
    print("     - Just Type Y(yes) or N(No) to answer the questions.\n")
    print("     - You have to indicate the extension of your files (e.g cpp for C++, js for JavaScript, html for Html, ...)\n")
        
    print("- You can also generated a header file which will be store in includes directory.\n")

    print("- Run the script with the flag \"-gi\" , e.g \"python3 ./create_project.py -gi\" to add new files in the .gitignore file.\n")
    print("     - You have to run first the script without parameters to set a new project.\n")
    print("     - WARNING you have to indicate the right path when adding a file to .gitignore.\n")
        
    print("Enjoy !!\n")

    

def ft_creation_project(name):
    print(f"{Fore.GREEN}||||{Style.RESET_ALL}", end='')
    sys.stdout.flush()
    time.sleep(0.5)
    print(f"{Fore.GREEN}||||||||{Style.RESET_ALL}", end='')
    sys.stdout.flush()
    time.sleep(0.5)
    print(f"{Fore.GREEN}||||||||||||{Style.RESET_ALL}")
    sys.stdout.flush()
    time.sleep(0.5)
    os.system('mkdir ' + name)
    print(f"{Fore.CYAN}Creation of your project directory OK{Style.RESET_ALL}")
    os.system('touch ' + name + '/.gitignore')
    print(f"{Fore.YELLOW}Creation of .gitignore OK{Style.RESET_ALL}")

def ft_create_src(name):
    os.system('mkdir '+ name + '/src')
    print(f"{Fore.CYAN}Creation src/ OK{Style.RESET_ALL}")

def ft_create_makefile(name):
    os.system('touch ' + name + '/Makefile')
    print(f"{Fore.CYAN}Creation Makefile OK{Style.RESET_ALL}")

def ft_create_lib(name):
    os.system('mkdir ' + name + '/lib')
    print(f"{Fore.CYAN}Creation lib OK{Style.RESET_ALL}")

def ft_create_header(name):
    header = input("Do you want a header file ? Y(yes) or *(no)\n")
    if (header.upper() == 'Y'):
        name_header = input("Name of header file : ")
        os.system('mkdir ' + name + '/includes/')
        os.system('touch '+ name +'/includes/'+ name_header + '.h')
        print(f"{Fore.CYAN}Creation includes/ OK{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Creation header file OK{Style.RESET_ALL}")

def ft_create_c_project(name):
    ft_creation_project(name)
    ft_create_src(name)
    ft_create_makefile(name)
    ft_create_lib(name)
    ft_create_header(name)
    print(f"{Fore.GREEN}creation C project OK{Style.RESET_ALL}\n")

def ft_create_other_project(name):
    ft_creation_project(name)
    lang = input("Choose a valid extension : ")
    os.system('touch ' + name + '/main.'+ lang)
    src = input("Do you want a src/ directory ? Y(yes) or *(no)\n")
    if (src.upper() == 'Y'):
        ft_create_src(name)
    src = input("Do you want a Makefile ? Y(yes) or *(no)\n")
    if(src.upper() == 'Y'):
        ft_create_makefile(name)
    src = input("Do you want a lib ? Y(yes) or *(no)\n")
    if(src.upper() == 'Y'):
        ft_create_lib(name)
    ft_create_header(name)
    print(f"{Fore.GREEN}creation " + lang.upper() + " project OK\n")

def ft_set_gitignore():
    t = input(f"{Fore.RED}Warning : You have to set a project before modify .gitignore . Type QUIT to exit or * to continue{Style.RESET_ALL}\n")
    if (t.upper() == "QUIT"):
        return
    dire = input("Name of the directory : ")
    response = input("Do you really want to modify the .gitignore file ? Y(yes) or *(no)\n")
    if (response.upper() == 'Y'):
        finish = True
        while (finish):
            gi = input("What file do you want to add ? (Type QUIT to exit)\n")
            if (gi.upper() == "QUIT"):
                break
            os.system('echo \"' + gi + '\" >> ' + dire + '/.gitignore')
            print(f"{Fore.YELLOW}.gitignore has been modified{Style.RESET_ALL}\n")
    else :
        print(".gitignore not modified\n")




if (len(sys.argv) == 2):
    if (sys.argv[1] == "-gi"):
            ft_set_gitignore();
    else:
        print(f"{Fore.RED} Error ... command unknowm . Run the scritp without command or with \'-gi\' flag. {Style.RESET_ALL}\n")
elif (len(sys.argv) == 1):
    while (i):
        response = input("Do you want to generate a C project? Y/N . Type HELP for more informations or QUIT to exit\n")
        if (response.upper() == 'Y'):
            name = input("Name of the  C project :\n")
            if (len(name) <= 0):
                print(f"{Fore.RED}Please enter a name{Style.RESET_ALL}\n")
            else:
                print("Creation ... please wait\n")
                ft_create_c_project(name)
                i = False
        elif (response.upper() == 'N'):
            name = input("Name of the project :\n")
            if (len(name) <= 0):
                print(f"{Fore.RED}Please enter a name{Style.RESET_ALL}\n")
            else:
                ft_create_other_project(name)
                i = False
        elif (response.upper() == "QUIT"):
            print(f"{Fore.CYAN}See you {Style.RESET_ALL}!\n")
            break
        elif (response.upper() == "HELP"):
            ft_show_help();
        else:
            print(f"{Fore.RED}Unknow command ... please enter Y or N {Style.RESET_ALL}\n")
else :
    print(f"{Fore.RED} Error ... Run the script without command or with \'-gi\' flag. {Style.RESET_ALL}\n")

