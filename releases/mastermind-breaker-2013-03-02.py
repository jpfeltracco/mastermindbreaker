import random
#!/usr/bin/python



import itertools
from itertools import repeat

while 1 == 1:

    try:

        print "                  _                      _           _ "
        print "  /\/\   __ _ ___| |_ ___ _ __ _ __ ___ (_)_ __   __| |"
        print " /    \ / _` / __| __/ _ \ '__| '_ ` _ \| | '_ \ / _` |"
        print "/ /\/\ \ (_| \__ \ ||  __/ |  | | | | | | | | | | (_| |"
        print "\/    \/\__,_|___/\__\___|_|  |_| |_| |_|_|_| |_|\__,_|"


        def evaluate(suggestion, comparelist):
                        takensu = []
                        takenso = []
                        
                        rcrp = 0
                        for i in range(5):
                                if suggestion[i] == comparelist[i]:
                                        rcrp += 1
                                        takensu.append(i)
                                        takenso.append(i)


                        rcwp = 0
                        for i in range(5):
                                        for j in range(0,5):
                                                if i not in takensu and j not in takenso:
                                                        if suggestion[i] == comparelist[j]:
                                                                rcwp += 1
                                                                takensu.append(i)
                                                                takenso.append(j)
                        return [rcrp, rcwp]


        def breaker(Tries, score, history, actualnum):
            compare = []
            suggestion = []
            ible = score[0] + score[1]
            subtries = 0
            if Tries == 1:
                suggestion = [0, 0, 0, 0, 0]
            if Tries == 2:
                actualnum = list(repeat(0,ible))	
                suggestion = actualnum + list(repeat(1,5-ible))
                while evaluate(suggestion, history[0])[0] != hisscore[0][0]:
                    random.shuffle(suggestion, random.random)
                    subtries = subtries + 1
                    if subtries > 100000:
                        suggestion = 42
                        print " "
                        print "ERROR"
                        break
                    
                    
            if Tries == 3:
                actualnum = actualnum + list(repeat(1,ible-len(actualnum)))
                suggestion = actualnum + list(repeat(2,5-ible))
                while (evaluate(suggestion, history[0])[0] != hisscore[0][0]
                       or evaluate(suggestion, history[1])[0] != hisscore[1][0]):
                    random.shuffle(suggestion, random.random)
                    subtries = subtries + 1
                    if subtries > 100000:
                        suggestion = 42
                        print " "
                        print "ERROR"
                        break

            if Tries == 4:
                actualnum = actualnum + list(repeat(2,ible-len(actualnum)))
                suggestion = actualnum + list(repeat(3,5-ible))
                while (evaluate(suggestion, history[0])[0] != hisscore[0][0]
                       or evaluate(suggestion, history[1])[0] != hisscore[1][0]
                       or evaluate(suggestion, history[2])[0] != hisscore[2][0]):
                    random.shuffle(suggestion, random.random)
                    subtries = subtries + 1
                    if subtries > 100000:
                        suggestion = 42
                        print " "
                        print "ERROR"
                        break

            if Tries == 5:
                actualnum = actualnum + list(repeat(3,ible-len(actualnum)))
                suggestion = actualnum + list(repeat(4,5-ible))
                while (evaluate(suggestion, history[0])[0] != hisscore[0][0]
                       or evaluate(suggestion, history[1])[0] != hisscore[1][0]
                       or evaluate(suggestion, history[2])[0] != hisscore[2][0]
                       or evaluate(suggestion, history[3])[0] != hisscore[3][0]):
                    random.shuffle(suggestion, random.random)
                    subtries = subtries + 1
                    if subtries > 100000:
                        suggestion = 42
                        print " "
                        print "ERROR"
                        break

            if Tries == 6:
                actualnum = actualnum + list(repeat(4,ible-len(actualnum)))
                suggestion = actualnum + list(repeat(5,5-ible))
                while (evaluate(suggestion, history[0])[0] != hisscore[0][0]
                       or evaluate(suggestion, history[1])[0] != hisscore[1][0]
                       or evaluate(suggestion, history[2])[0] != hisscore[2][0]
                       or evaluate(suggestion, history[3])[0] != hisscore[3][0]
                       or evaluate(suggestion, history[4])[0] != hisscore[4][0]):
                    random.shuffle(suggestion, random.random)
                    subtries = subtries + 1
                    if subtries > 100000:
                        suggestion = 42
                        print " "
                        print "ERROR"
                        break

            if Tries == 7:
                actualnum = actualnum + list(repeat(5,ible-len(actualnum)))
                suggestion = actualnum + list(repeat(6,5-ible))
                while (evaluate(suggestion, history[0])[0] != hisscore[0][0]
                       or evaluate(suggestion, history[1])[0] != hisscore[1][0]
                       or evaluate(suggestion, history[2])[0] != hisscore[2][0]
                       or evaluate(suggestion, history[3])[0] != hisscore[3][0]
                       or evaluate(suggestion, history[4])[0] != hisscore[4][0]
                       or evaluate(suggestion, history[5])[0] != hisscore[5][0]):
                    random.shuffle(suggestion, random.random)
                    subtries = subtries + 1
                    if subtries > 100000:
                        suggestion = 42
                        print " "
                        print "ERROR"
                        break

            if Tries == 8:
                actualnum = actualnum + list(repeat(6,ible-len(actualnum)))
                suggestion = actualnum + list(repeat(7,5-ible))
                while (evaluate(suggestion, history[0])[0] != hisscore[0][0]
                       or evaluate(suggestion, history[1])[0] != hisscore[1][0]
                       or evaluate(suggestion, history[2])[0] != hisscore[2][0]
                       or evaluate(suggestion, history[3])[0] != hisscore[3][0]
                       or evaluate(suggestion, history[4])[0] != hisscore[4][0]
                       or evaluate(suggestion, history[5])[0] != hisscore[5][0]
                       or evaluate(suggestion, history[6])[0] != hisscore[6][0]):
                    random.shuffle(suggestion, random.random)
                    subtries = subtries + 1
                    if subtries > 100000:
                        suggestion = 42
                        print " "
                        print "ERROR"
                        break

            if Tries == 9:
                actualnum = actualnum + list(repeat(7,ible-len(actualnum)))
                suggestion = actualnum + list(repeat(8,5-ible))
                while (evaluate(suggestion, history[0])[0] != hisscore[0][0]
                       or evaluate(suggestion, history[1])[0] != hisscore[1][0]
                       or evaluate(suggestion, history[2])[0] != hisscore[2][0]
                       or evaluate(suggestion, history[3])[0] != hisscore[3][0]
                       or evaluate(suggestion, history[4])[0] != hisscore[4][0]
                       or evaluate(suggestion, history[5])[0] != hisscore[5][0]
                       or evaluate(suggestion, history[6])[0] != hisscore[6][0]
                       or evaluate(suggestion, history[7])[0] != hisscore[7][0]):
                    random.shuffle(suggestion, random.random)
                    subtries = subtries + 1
                    if subtries > 100000:
                        suggestion = 42
                        print " "
                        print "ERROR"
                        break

            if Tries == 10:
                actualnum = actualnum + list(repeat(8,ible-len(actualnum)))
                suggestion = actualnum + list(repeat(9,5-ible))
                while (evaluate(suggestion, history[0])[0] != hisscore[0][0]
                       or evaluate(suggestion, history[1])[0] != hisscore[1][0]
                       or evaluate(suggestion, history[2])[0] != hisscore[2][0]
                       or evaluate(suggestion, history[3])[0] != hisscore[3][0]
                       or evaluate(suggestion, history[4])[0] != hisscore[4][0]
                       or evaluate(suggestion, history[5])[0] != hisscore[5][0]
                       or evaluate(suggestion, history[6])[0] != hisscore[6][0]
                       or evaluate(suggestion, history[7])[0] != hisscore[7][0]
                       or evaluate(suggestion, history[8])[0] != hisscore[8][0]):
                    random.shuffle(suggestion, random.random)
                    subtries = subtries + 1
                    if subtries > 100000:
                        suggestion = 42
                        print " "
                        print "ERROR"
                        break

            if Tries == 11:
                actualnum = actualnum +list(repeat(9,ible-len(actualnum)))
                suggestion = actualnum + list(repeat(10,5-ible))
                while (evaluate(suggestion, history[0])[0] != hisscore[0][0]
                       or evaluate(suggestion, history[1])[0] != hisscore[1][0]
                       or evaluate(suggestion, history[2])[0] != hisscore[2][0]
                       or evaluate(suggestion, history[3])[0] != hisscore[3][0]
                       or evaluate(suggestion, history[4])[0] != hisscore[4][0]
                       or evaluate(suggestion, history[5])[0] != hisscore[5][0]
                       or evaluate(suggestion, history[6])[0] != hisscore[6][0]
                       or evaluate(suggestion, history[7])[0] != hisscore[7][0]
                       or evaluate(suggestion, history[8])[0] != hisscore[8][0]
                       or evaluate(suggestion, history[9])[0] != hisscore[9][0]):
                    random.shuffle(suggestion, random.random)
                    subtries = subtries + 1
                    if subtries > 100000:
                        suggestion = 42
                        print " "
                        print "ERROR"
                        break
            if Tries == 12:
                actualnum = actualnum +list(repeat(10,ible-len(actualnum)))
                suggestion = actualnum + list(repeat(11,5-ible))
                while (evaluate(suggestion, history[0])[0] != hisscore[0][0]
                       or evaluate(suggestion, history[1])[0] != hisscore[1][0]
                       or evaluate(suggestion, history[2])[0] != hisscore[2][0]
                       or evaluate(suggestion, history[3])[0] != hisscore[3][0]
                       or evaluate(suggestion, history[4])[0] != hisscore[4][0]
                       or evaluate(suggestion, history[5])[0] != hisscore[5][0]
                       or evaluate(suggestion, history[6])[0] != hisscore[6][0]
                       or evaluate(suggestion, history[7])[0] != hisscore[7][0]
                       or evaluate(suggestion, history[8])[0] != hisscore[8][0]
                       or evaluate(suggestion, history[9])[0] != hisscore[9][0]
                       or evaluate(suggestion, history[10])[0] != hisscore[10][0]):
                    random.shuffle(suggestion, random.random)
                    subtries = subtries + 1
                    if subtries > 100000:
                        suggestion = 42
                        print " "
                        print "ERROR"
                        break
            return suggestion, actualnum



        Tries = 0
        score = [0,0]
        history = []
        hisscore = []
        actualnum = []
        colors = ["Wh","Pi","Or","Ye","Gr","Bu","Pu","Bk"]
        random.shuffle(colors)

        print "Enter 'go' to begin cracking, 'help' for help,"
        print "'colors' for color list, or 'quit' to quit."
        print " "
        command = raw_input("Command: ")
        print " "
        command = command.lower()
        if command == "go":
            while score != [5,0]:
                Tries = Tries + 1
                atry = breaker(Tries, score, history, actualnum)
                if atry[0] == 42:
                    break
                history.append(atry[0])
                actualnum = atry[1]
                lengthatry = len(atry[0])
                if lengthatry > 5:
                    print " "
                    print "ERROR"
                    break
                    
                convertedlist = []
                for i in atry[0]:
                    convertedlist.append(colors[i])
	
                if Tries < 10:
                    print Tries,". "," ",','.join(convertedlist)
                if Tries > 9:
                    print Tries,"."," ",','.join(convertedlist)
                try:
                    score = tuple(int(x.strip()) for x in raw_input("Score: ").split(','))
                except:
                    print " "
                    print "ERROR"
                    break
                hisscore.append(score)
                if score[0] == 5:
                    print " "
                    print "Cracked!"
                    break
                if score[0] > 5 or score[1] > 5:
                    print " "
                    print "ERROR"
                    break
        if command == "help":
            print "Enter the number of red pins, a comma, followed by"
            print "the number of white pins. Then hit enter."
            print " "
            print "Red pins are correct color and correct position"
            print " "
            print "White pins are correct color but incorrect position"
        if command == "colors":
            print "Wh,Pi,Or,Ye,Gr,Bu,Pu,Bk"
            print "Wh = white, Pi = pink, Or = orange, Ye = yellow,"
            print "Gr = green, Bu = blue, Pu = pink, Bk = black"
        if command == "quit":
            break


    except:
        print " "
        print "ERROR"
        
    print " "
    endvar = raw_input("Restart? [Y/N]: ")
    endvar = endvar.lower()
    if endvar == "n":
        break
