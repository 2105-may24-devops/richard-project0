import os
import sys
from pathlib import Path
from pathlib import PureWindowsPath
import datetime
from blessed import Terminal
term = Terminal()


def start():
    #give startup message and option to exit
    #if exit selected, exit program
    #if startup confirmed, run testFirstRun then return

    #establish terminal location and traits, then clear terminal window
    with term.location(0, term.height - 1):
        print(term.home + term.on_black + term.clear)

    #print program info and startup confirmation request
        print('Hawkins P0 File Backup System'+'\n')

    #test if necessary files already exist
    test=test_first_run()

    #if they exist, clear terminal and return to main
    if test == True:
        print(term.clear)
        return
    
    #if they do not exist, confirm they should be made
    else:
        print('Running this program will create folders and files'+'\n'+'in your drive if they do not already exist'+'\n')
        #accept user input        
        cont = input('Do you wish to continue? Y/N'+'\n')

        #verify input is valid, if not then request specific input
        while (cont != 'Y' and cont != 'N'):
            cont = input('Please enter either Y or N only'+'\n')

        #if startup confirmed, clear terminal window and run initialize_system(), then return to main
        if cont == 'Y':
            print(term.clear)
            initialize_system()
            return
        #if startup denied, clear terminal and exit system            
        if cont == 'N':
            input('Press any key to exit...')
            print(term.clear)
            raise SystemExit
    return
   

def test_first_run():
    #if Primary, Secondary, and Sys folders, and Global.cl and FL.sys files
    #do not exist already, return false. If they do, return true.
    '''
    p = PureWindowsPath('C:/Hawkins_P0')

    if not p:
        Path.mkdir(p)
    if not (p + "/Primary"):
        Path.mkdir(p + "/Primary")
    '''

    if not Path("Hawkins_P0").exists():
        return False
    if not Path("Hawkins_P0/Primary").exists():
        return False
    if not Path("Hawkins_P0/Secondary").exists():
        return False
    if not Path("Hawkins_P0/Sys").exists():
        return False
    if not Path("Hawkins_P0/Sys/Global.cl").exists():
        return False
    if not Path("Hawkins_P0/Sys/FL.sy").exists():
        return False

    return True
    

def initialize_system():
    #if Primary, Secondary, and Sys folders, and Global.cl and FL.sys files
    #do not exist already, create them then return
    '''
    p = PureWindowsPath('C:/Hawkins_P0')

    if not p:
        Path.mkdir(p)
    if not (p + "/Primary"):
        Path.mkdir(p + "/Primary")
    '''

    if not Path("Hawkins_P0").exists():
        Path("Hawkins_P0").mkdir()
    if not Path("Hawkins_P0/Primary").exists():
        Path("Hawkins_P0/Primary").mkdir()
    if not Path("Hawkins_P0/Secondary").exists():
        Path("Hawkins_P0/Secondary").mkdir()
    if not Path("Hawkins_P0/Sys").exists():
        Path("Hawkins_P0/Sys").mkdir()
    if not Path("Hawkins_P0/Sys/Global.cl").exists():
        with open("Hawkins_P0/Sys/Global.cl", 'w') as file:
            file.writelines("")
    if not Path("Hawkins_P0/Sys/FL.sy").exists():
        with open("Hawkins_P0/Sys/FL.sy", 'w') as file:
            file.writelines("")

    return


def mainMenu():
    #display main menu options, and allow user to select option from list

    #list possible selections in menu_items 
    menu_items = [["1- Add a file to backup"], ["2- Update all backups(in progress)"], ["3- View system changelog"],["4- View files in backup"],["5- Exit program"]]

    #set terminal parameters, clear terminl, display instructions and list options by enumerating through using for loop
    with term.location(0, term.height - 1):
        print(term.home + term.bright_blue_on_black + term.clear)
        print('Enter the number listed with the function you'+'\n'+ 'wish to perform to make your selection'+'\n')
        for (i, m) in enumerate(menu_items):
            print(term.on_black + '{t.normal}{title}'.format(t=term, title=m[0]))

    #set selection to out of bounds, while selection out of bounds/not valid request new selection
        selection=0
        print(term.bright_blue_on_black)
        while 1>selection or 5<selection:
            try:
                selection = int(input(term.red_on_black+'Please enter a number'+'\n'))
            except ValueError:
                print('Only numbers are accepted')

    #when valid selection made, clear terminal and return selection value
    print(term.white_on_black + term.clear())
    return(selection)


def actionFuncCall(act):
    
    if act == 1:
    #add file to backup    
        #accept and verify user input file path. Loop until valid file path given.
        path=Path('')
        print(term.bright_blue_on_black)
        while not path.is_file():
            try:
                path=Path(input('Please enter a valid absolute file path,'+'\n'+'or press CTRL + C to return to the main menu'+'\n'))
            except KeyboardInterrupt:
                return

        addFile(path)
        return        

    elif act == 2:
    #update files already in system
        with open('Hawkins_P0/Sys/FL.sy', 'r') as file:
            txt = file.readlines()
            for line in txt:
                path = line.rstrip()
                update_file(path)
            input('Press any key to continue...')
        return


    elif act == 3:
    #view global changelog
        view_file('Hawkins_P0/Sys/Global.cl')
        return
    
    elif act == 4:
    #view files in system
        view_file('Hawkins_P0/Sys/FL.sy')

    elif act == 5:
    #exit case
        print(term.white_on_black + term.clear)
        SystemExit
    
    else:
        return


def addFile(path):
    #add new file to backup

    #copy target of path to Primary folder as same type,
    #and to Secondary folder with .bu suffex, add entry on Global.cl

    #read given path to fp (file path) as a Path type
    fp=Path(path)
    
    #write original file path to FL.sy
    with open ("Hawkins_P0/Sys/FL.sy", 'a') as file:
        file.writelines(str(fp) + "\n")

    #read file at path into contents
    with open(path, "r") as file:
        contents = file.read()

    #truncate file path to file name and extension
    fn=fp.name

    #write contents to new file of same name and extension at C:/Hawins_P0/Primary, confirm when complete
    with open("Hawkins_P0/Primary/" + fn, 'w') as file:
        file.writelines(contents)
    print('Primary copy created'+'\n')

    #truncate file path to name only
    fs=fp.stem

    #write contents to new file of same name and different extension in C:/Hakwins_P0/Secondary, confirm when complete
    with open("Hawkins_P0/Secondary/" + fs +".bu", 'w') as file:
        file.writelines(contents)
    print('Secondary copy created'+'\n')

    #get current time, convert file path to string format, and generate entry of file creation in Global.cl
    time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open ("Hawkins_P0/Sys/Global.cl", 'a') as file:
        file.writelines(str(fp) + " added on " + time + '\n')
    input('Press any key to continue...')
    
    #clear terminal and return
    print(term.clear())
    return
    

def update_file(path):
    #update file in backup
    #copy target of path to Primary folder as same type,
    #and to Secondary folder with .bu suffex, add entry on Global.cl

    #read given path to fp (file path) as a Path type
    fp=Path(path)
    
    #read file at path into contents
    with open(fp, "r") as file:
        contents = file.read()

    #truncate file path to file name and extension
    fn=fp.name

    #write contents to new file of same name and extension at C:/Hawins_P0/Primary, confirm when complete
    with open("Hawkins_P0/Primary/" + fn, 'w') as file:
        file.writelines(contents)
    print('Primary copy created ' + str(fp) + '\n')

    #truncate file path to name only
    fs=fp.stem

    #write contents to new file of same name and different extension in C:/Hakwins_P0/Secondary, confirm when complete
    with open("Hawkins_P0/Secondary/" + fs + ".bu", 'w') as file:
        file.writelines(contents)
    print('Secondary copy created ' + str(fp) + '\n')

    #get current time, convert file path to string format, and generate entry of file creation in Global.cl
    time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open ("Hawkins_P0/Sys/Global.cl", 'a') as file:
        file.writelines(str(fp) +" updated on " +time + '\n')

    return


def view_file(path):
    #print most recent 5 lines of a file to terminal

    #get line count of file at path
    max_line = countLine(path)

    #get content from file
    content = readLines(path, max_line, (max_line-5))

    #provide output desctiption
    print(term.bright_blue_on_black+'Displaying most recent five entries', end='\n'+'\n')

    #display content by line
    print(term.white_on_black)
    print(*content, sep='\n', end='')

    #wait for user input, clear terminal, return to main menu
    input(term.bright_blue_on_black+'\n'+'Press any key to return to main menu...')
    print(term.clear())  
    return
 
 
def readLines(path, max_line = 0, min_line = 0):
    #read range of lines from file
    #input file path, minimum line and maximum line numbers to be read/returned

    #if min_line out of bounds, reset to default
    if min_line < 0 or max_line < min_line:
        min_line = 0

    #if max_line out of bounds, set to file max
    if max_line > countLine(path):
        max_line = countLine(path)

    #read lines from path to string txt,
    #slice txt to min_line and max_line,
    #return txt
    txt =""
    with open(path, 'r') as file:
        txt = file.readlines()
        txt = txt[min_line: max_line]
    return txt


def countLine(path):
    #count the number of lines in the path file
    
    with open(path, 'r') as file:
        num_lines = sum(1 for line in file)
    return num_lines


def readFolder(path):
    #scan through folder at p_path recursively, and print contents by file path

    print(term.bright_blue_on_black+'Displaying files included in backup system...')

    #get folder content
    for path,dirs,files in os.walk(path):
        for filename in files:
            print(term.white_on_black)
            print(filename, end='')
    
    #wait for user input, clear terminal, return to main menu
    input(term.bright_blue_on_black+'\n'+'Press any key to return to main menu...')
    print(term.clear())  
    return

   
