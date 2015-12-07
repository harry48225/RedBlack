'''
Created on 13 Oct 2015

@author: hsbest12
'''
import time
import random

def ASCII(x):
    
    if x == 'gameover':
        
        print ' __              ___     __        ___  __  '
        print '/ _`  /\   |\/| |__     /  \ \  / |__  |__) '
        print '\__> /~~\  |  | |___    \__/  \/  |___ |  \ '
        
    if x == 'millionare':
        
        print '.88b  d88. d888888b db      db      d888888b  .d88b.  d8b   db  .d8b.  d8888b. d88888b '
        print "88 YbdP`88   `88'   88      88         88'   .8P  Y8. 888o  88 d8   8b 88  `8D 88'     "
        print '88  88  88    88    88      88         88    88    88 88V8o 88 88ooo88 88oobY  88ooooo '
        print '88  88  88    88    88      88         88    88    88 88 V8o88 88~~~88 88`8b   88~~~~~ '
        print '88  88  88   .88.   88booo. 88booo.   .88.   `8b  d8  88  V888 88   88 88 `88. 88.     '
        print 'YP  YP  YP Y888888P Y88888P Y88888P Y888888P  `Y88P   VP   V8P YP   YP 88   YD Y88888P '
    
    if x == 'bomb':
        
        print ' ____  ____  _      ____    ____  _____ _____ _     ____  _____ '
        print '/  __\/  _ \/ \__/|/  _ \  /  _ \/  __//    // \ /\/ ___\/  __/ '
        print '| | //| / \|| |\/||| | //  | | \||  \  |  __\| | |||    \|  \   '
        print '| |_\\ | \_/|| |  ||| |_\\   | |_/||  /_ | |   | \_/|\___ ||  /_  '
        print '\____/\____/\_/  \|\____/  \____/\____|\_/   \____/\____/\____\ '
                                                                
         
                   
def millionare():
    
    print 'Bonus game unlocked!'
    print
    
    ASCII('millionare')
    
    print
    
    def question(quesnum, question, ans, trueans):
        
        i = 1
         
        print 'Question ', quesnum
        print
        time.sleep(0.2)
        print question
        
        for answer in ans:
            
            time.sleep(0.1)
            print i, '', answer
            
            i += 1
            
        usrans = input(': ')
        
        print
        
        if usrans == trueans:
            time.sleep(0.2)
            print 'Correct!'
            print

            
        else:
            time.sleep(0.2)
            print 'Wrong!'
            print
            return False
            
            
    
    time.sleep(1)
            
    while True:    
    
    
        if question(1, 'What is Mr. Bhikas favourite colour?', ['Purple', 'Green', 'Red', 'Orange'], 1) == False:
            
            ASCII('gameover')
            print
            
            break
    
        if question(2, 'How many smartboards are there?', [1, 5, 100, 2], 4) == False:
            
            ASCII('gameover')
            print
            
            break    
        
        if question(3, 'Would you rather be a Blue Whale or Killer Whale?', ['Blue Whale', 'Killer Whale'], 1) == False:
            
            ASCII('gameover')
            print
            
            break
        
        time.sleep(0.5)
        
        print 'You won!'
        
        return True
        
def whackamole():
    
    print
    print 'Bonus game unlocked!'
    print 'You have tripled your original cash!'
        
    inarow = 0
    lives = 5
        
    time.sleep(1)
    print 'Welcome to Whack A Mole!'
    time.sleep(1)
    print 'You must correctly guess which hole to mole will pop up from!'
    time.sleep(2)
    print 'There are 3 holes:'
    time.sleep(1)
    print 'Hole 1'
    time.sleep(0.5)
    print 'Hole 2'
    time.sleep(0.5)
    print 'Hole 3'
    
    print 'If you get it right 3 times in a row you win!'
    
    time.sleep(4)
    
    
    while True:
        
        # Prints the Whack a Mole Logo
        print ' __          ___                _                 __  __       _      _ '
        print ' \ \        / / |              | |        /\     |  \/  |     | |    | |'
        print '  \ \  /\  / /| |__   __ _  ___| | __    /  \    | \  / | ___ | | ___| |'
        print '   \ \/  \/ / |  _ \ / _` |/ __| |/ /   / /\ \   | |\/| |/ _ \| |/ _ \ |'
        print '    \  /\  /  | | | | (_| | (__|   <   / ____ \  | |  | | (_) | |  __/_|'
        print '     \/  \/   |_| |_|\__,_|\___|_|\_\ /_/    \_\ |_|  |_|\___/|_|\___(_)'
        
        print
        
        print
        time.sleep(0.1)
        print 'You have %d Lives.' % (lives)
        print 'Your streak is %d.' % (inarow)
        
        time.sleep(0.2)
        holesel = input('Select a hole: ')
        while holesel not in [1, 2, 3]:
            print 'Incorrect input!'
            time.sleep(0.5)
            holesel = input('Select a hole: ')
            
        hole = random.randrange(1,4)
        time.sleep(0.5)
        print 'The mole appeared from hole %d!' %(hole)
        
        time.sleep(0.2)
        if hole == holesel:
            print 'Well done you selected correctly!'
            inarow += 1
            time.sleep(1)
            
        elif hole != holesel:
            print 'You got it wrong!'
            inarow = 0
            lives -= 1
            time.sleep(1)
            
        if inarow == 3:
            print
            print
            time.sleep(0.4)
            print 'You won!'
            break
        
        if lives == 0:
            print
            ASCII('gameover')
            time.sleep(0.4)
            print 'You lose!'
            break
       
def bombdefuse():
    
    print 'Bonus game unlocked!'
    print
    time.sleep(0.2)
    print 'Welcome to bomb defuse'
    time.sleep(0.2)
    print 'In this game you have to defuse a bomb'
    time.sleep(0.2)
    print 'To defuse the bomb you must cut the wires in the right order!'
    time.sleep(0.2)
    print 'The order resets every game!'
    time.sleep(3)
    correctorder = ['Red', 'Blue', 'Green']
    
    random.shuffle(correctorder)
    
    wires = ['Red', 'Green', 'Blue']
    amtofwires = []
    n = 0
    
    #print correctorder
    
    while True:
        
        amtofwires = []
        print
        ASCII('bomb')
        print
        i = 1
        
        time.sleep(0.2)
        
        
        
        for wire in wires:
            
            amtofwires.append(i)
            print i, '', wire
            i += 1
            
        wirecut = input('What wire would you like to cut: ') - 1
        while wirecut + 1 not in amtofwires:
            print 'Error!'
            wirecut = input('What wire would you like to cut: ') - 1
        
        
        time.sleep(0.2)
        if wires[wirecut] == correctorder[n]:
            
            
            print 'You cut the correct wire!'
            
        
        if n == 2:
            
            print
            time.sleep(0.5)
            print 'You won'
            time.sleep(0.2)
            return True
            break
        
        if wires[wirecut] != correctorder[n]:
            time.sleep(1)
            
            print "     _.-^^---....,,--"
            print " _--                  --_"
            print "<                        >)"
            print "|                         |"
            print " \._                   _./"
            print "    ```--. . , ; .--'''"
            print "          | |   |"
            print "       .-=||  | |=-."
            print "       `-=#$%&%$#=-'"
            print "          | ;  :|"
            print " _____.,-#%&$@%#&#~,._____"
            
            time.sleep(3)
            print 'The bomb exploded!'
            time.sleep(1)
            ASCII('gameover')
            break
            
        wires.remove(wires[wirecut])
        n += 1   
        amtofwires.remove(n)
        
        
    

#le cheeky gmae

playedwhackamole = 0



print 'Red or Black developed by: Harry Best'

#Prints a swag logo
print '  _           _              '
print ' |_)  _   _| |_) |  _.  _ |  '
print ' | \ (/_ (_| |_) | (_| (_ |< '

print
print 'Welcome to the MLG casino'
print 'You will be playing red or black today'

#Asks how much they are going to put in the machine
oldcash = input('How much money would you like to put into the machine: ')

while oldcash <= 0:
    
    print
    print 'You cant add no cash!'
    print
    oldcash = input('How much money would you like to put into the machine: ')
    
cash = oldcash
time.sleep(0.5)

print 'Thank you'

#Le game
while True:
    
    time.sleep(0.5)
    #Le casino
    
    print
    print
    print '    _          )   ___                     '
    print ' ___/__)       (__/_____)         ,        '
    print '(, /    _        /       _   _     __   ___'
    print '  /   _(/_      /       (_(_/_)__(_/ (_(_) '
    print ' (_____        (______)                    '
    print '        )                                  '
    
    
    #Tells them about the cheat codes
    print 'Hint!' 
    print 'Try using these when betting: 7355608 or 987654321123456789'
    
    #Prints Cash
    print 'Cash = %d' % (cash)
    
    #Asks what they want to bet on
    selection = input('Would you like Red(1), or Black(2): ')
    #Makes sure that selection is valid
    while selection not in [1, 2, 987654321123456789, 7355608]:
        print 'Invalid input!'
        selection = input('Would you like Red(1), or Black(2): ')
    
    if selection in [1, 2]:
        
            #Asks for bet   
        bet = input('How much would you like to bet: ')
        #Checks if they have enough money
        while bet > cash:
            print 'Insufficient funds!'
            print 'You have %d funds!' % (cash)
            bet = input('How much would you like to bet: ')
        
        while bet <= 0:
            
            print
            print 'You need to bet something!'
            print 
            print 'You have %d funds!' % (cash)
            bet = input('How much would you like to bet: ')
            
        #Chooses red or black randomly   
        redblack = random.randrange(1,3)
        
        time.sleep(0.5)
        
        #Tells user result
        if redblack == 1:
            print 'It was Red!'
            
        else:
            print 'It was Black!'
        
        print
         
        time.sleep(0.5)
         
        #Awards prizes   
        if redblack == selection:
            
            print 'You won!'
            cash += bet
        
        else:
            
            print 'You lose!'
            cash -= bet   
    
        
        #Checks if dead
        cashadd = 0
        if cash <= 0:
            
            anew = input('Would you like to add more funds? Yes(1) No(2): ')
            
            if anew == 1:
                cashadd = input('How much money would you like to add: ')
                while cashadd <= 0:
                    print 'You need to add some money!'
                    cashadd = input('How much money would you like to add: ')

    
            
                
        #Cash out?
        if cash > 0:
        
            cashout = input('Would you like to cash out, Yes(1) No(2). You have %d cash: ' % (cash))
            while cashout not in [1,2]:
                print 'Error!'
                print 'Invalid selection'
                time.sleep(0.5)
                cashout = input('Would you like to cash out, Yes(1) No(2). You have %d cash: ' % (cash))
            
            if cashout == 1:
                print
                time.sleep(0.1)
                print 'You leave with %d cash' % (cash)
                
                time.sleep(0.2)
                
                ASCII('gameover')
                time.sleep(10) 
                break
            
        if cashadd > 0:
            cash = cashadd
            oldcash = cashadd
            time.sleep(0.5)
            print 'Success!'
            print 'Your new balance is: %d' % (cash)
            
            
        if cash <= 0:
            time.sleep(0.2)
            
            ASCII('gameover')
             
            time.sleep(10)   
            break

          
        #Checks if valid 4 bonus game!
        if cash >= oldcash*3 and playedwhackamole == 0:
            
            whackamole()
            playedwhackamole = 1
              
        
    #Checks for Millionare    
    if selection == 987654321123456789:
        
        if millionare() == True:
            
            print 'Tripling your cash!'
            
            print
            
            time.sleep(3)
            
            cash += cash * 2
            
            
            print 'Complete!'
            
            print
            
            print 'Your new cash is: ', cash
        
    #Checks for Bomb Game
    if selection == 7355608:
        
        if bombdefuse() == True:
            
            print 'Tripling your cash!'
            
            print
            
            time.sleep(3)
            
            cash += cash * 2
            
            
            print 'Complete!'
            
            print
            
            print 'Your new cash is: ', cash
               
        
             
            

         
    
        
            
