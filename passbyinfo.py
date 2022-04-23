try:
    from os import system as cmd
    import random
    from time import sleep as sp

    print("""   
 ██████╗ ██╗  ██╗██████╗ ██╗  ██╗██████╗ 
██╔═████╗╚██╗██╔╝██╔══██╗██║  ██║██╔══██╗
██║██╔██║ ╚███╔╝ ██████╔╝███████║██║  ██║
████╔╝██║ ██╔██╗ ██╔══██╗╚════██║██║  ██║
╚██████╔╝██╔╝ ██╗██████╔╝     ██║██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚═╝╚═════╝ 
coding by @i0xb4d , @21o1""")
    print("Password list by informations")
    print("Starting...\n")
    path = input("Enter the output file name[without .txt]:\n>")
    filea = open(path+".txt", 'w')
    cnt =int(input("Enter the count[must be integer]:\n>"))








    lene = input("Enter the length of the password -how much info is in each password-? (if you didn't understand click enter for the default (4 info) or write 999 for more help )\n>")
    if lene == "999":
        print("""
---------------------------------------------------------------
That's number is the count of information in each password:
if you set it to 3 and you put 3 info
1-2000
2-Mohammed
3-R
the output file will include 2 info in each password:
the list:

moahmmed2000
R2000
Rmohammed


$two info in each password
---------------------------------------------------------------
        """)
        lene = input("Enter the length of the password -how much info is in each password-? (if you didn't understand click enter for the default (4 info))\n>")
    elif lene == '':
        lene = 4

    info1 = input("Birthday?(Write no to skip)\n>")
    info2 = input("Name?(Write no to skip)\n>")
    info3 = input("Love?(Write no to skip)\n>")

    infomx = [info1,info2,info3]
    if info1  == "no":
        infomx.pop(0)
    elif info2  == "no":
        infomx.pop(1)
    elif info3  == "no":
        infomx.pop(2)
    addinfo = input("another info?(yes/no)\n>")
    while addinfo == "yes":
        newinfo = input("what else?\n>")
        infomx.append(newinfo)
        addinfo = input("another info?(yes/no)\n>")
        infomxl2 = len(infomx)
        if addinfo == "no":
            infomx.pop(infomxl2 - 1)
    check = input("Check your input and if no typing error write yes except write no?\n>")
    if check == "yes":
        for i in range(cnt):
            infomxl = len(infomx)
            result = ''
            for e in range(int(lene)):
                result += infomx[random.randint(0,infomxl -1)]
                
            filea.write(result+"\n")
    else:
        print("start again...")
        sp(1)
        try:
            cmd("cls")
            cmd("python passbyinfo.py")
        except:
            cmd("clear")
            cmd("python passbyinfo.py")
except KeyboardInterrupt:
    print("\nhave a nice day , exiting...")
    sp(1)
except FileNotFoundError:
    print("please check the path and try again...")
    sp(1)
except ValueError:
    print("bad type of data please follow the rules (numbers for integer and letter for strings)")
    sp(1)
except ModuleNotFoundError:
    print("we cant find the module which we need\nand to install it:")
    print("""
windows:
1-run cmd as adminstrator
2-write 'pip install random'
3-enter!

Linux:
1-sudo pip install random
2-enter!
    """)
    