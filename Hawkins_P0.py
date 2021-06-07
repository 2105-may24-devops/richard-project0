#!/usr/bin/env python3

import sysP0 as sysP0
from pathlib import Path
import sys, datetime


#Written by Richard Hawkins, May 29, 2021
#Creative consultant Christian English

def main(act = 0):
    #run program start/setup actions
    sysP0.start()
    
    #begin main action loop, while action selection valid, loop and return to main menu. 
    #when exit selection made, exit program
    while act != 5:

            act = sysP0.mainMenu()
            sysP0.actionFuncCall(act)


if __name__ == "__main__":

    action = ''
    path = ''

    if len(sys.argv) >= 2:
        action = sys.argv[1]
    if len(sys.argv) >= 3:
        path = sys.argv[2]



    if sysP0.test_first_run() == True:    
        #get current time, and generate entry of runtime in Global.cl
        time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open ("Hawkins_P0/Sys/Global.cl", 'a') as file:
            file.writelines('Program start at ' + time + '\n')
        
    if action == '-add':
        if sysP0.test_first_run() == False:
            print('Please run the full backup program to initialize necessary files.', file = sys.stderr)
            exit (1)
        path=Path(path)
        if not path.is_file(): 
            print('File must exist to be added to backup', file = sys.stderr)
            exit (1)   
        else:
            sysP0.addFile(path)

    elif action == '-update':
        if sysP0.test_first_run() == False:
            print('Please run the full backup program to initialize necessary files.', file = sys.stderr)
            exit (1)
        with open('Hawkins_P0/Sys/FL.sy', 'r') as file:
            txt = file.readlines()
            for line in txt:
                path = line.rstrip()
                sysP0.update_file(path)

    else:
        main()

