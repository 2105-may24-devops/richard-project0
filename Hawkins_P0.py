import sysP0 as sysP0

#Written by Richard Hawkins, May 29, 2021
#Creative consultant Christian English

def main(act=0):
    #run program start/setup actions
    sysP0.start()
    
    #begin main action loop, while action selection valid, loop and return to main menu. 
    #when exit selection made, exit program
    while act != 5:
        act = sysP0.mainMenu()
        sysP0.actionFuncCall(act)
        
main()
