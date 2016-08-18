print "\n\n               SOULBOUND\n\n"
print "PRESS 1 TO PLAY\nPRESS 2 TO CREDITS\nPRESS 3 FOR INSTRUCTIONS\nPRESS 4 TO SAVE YOUR SETTINGS"
menu = input("\n\nENTER: ")
if menu == 1:
    print "\n\n"
elif menu == 2:
    print "\n\nCREDITS:\nEduardo Daemon Teixeira dos Santos\nMarcos Zlotnik"
elif menu == 3:
    print "\n\n"
elif menu == 4:
    print "\n\nSETTINGS\n\nObservaiton: if you want to change your class you will need to reset "
    print "the game deleting all the files created by it."
    print "\n\nCHOOSE A RACE(number):\n1.ELF\n2.ORC\n3.DWARF\n4.HUMAN\n"
    race = input("ENTER: ")
    print "\n\nCHOOSE A CLASS(number):\n1.MAGE\n2.THIEF\n3.WARRIOR\n4.WIZARD\n"
    classes = input("ENTER: ")
    PP = 0
    basic = 0
    PV = 0
    money = 20
    dictRace = {1: "ELF", 2: "ORC", 3: "DWARF", 4: "HUMAN"}
    dictClasses = {1: "MAGE", 2: "THIEF", 3: "WARRIOR", 4: "WIZARD"}
    fileClasses = open("classes.txt", "w")
    fileClasses.write(dictClasses[classes])
    fileClasses.close()
    fileMoney = open("money.txt", "w")
    fileMoney.write(str(money))
    fileMoney.close()
    fileRace = open("race.txt", "w")
    fileRace.write(dictRace[race])
    fileRace.close()
    if classes == 1:
    	player = "MAGE"
    	PP = 20
    	basic = 15
    	PV = 50
        filePP = open("PP.txt", "w")
        filePP.write(str(PP))
        filePP.close()
        fileBasic = open("basic.txt", "w")
        fileBasic.write(str(basic))
        fileBasic.close()
        filePV = open("PV.txt", "w")
        filePV.write(str(PV))
        filePV.close()
        assist = "GOLEM"
        basicAssist = 3
        PVAssist = 6
        fileAssist = open("assist.txt", "w")
        fileAssist.write(assist)
        fileAssist.close()
        fileBasicAssist = open("basicAssist.txt", "w")
        fileBasicAssist.write(str(basicAssist))
        fileBasicAssist.close()
        filePVAssist = open("PVAssist.txt", "w")
        filePVAssist.write(str(PVAssist))
        filePVAssist.close()
    elif classes == 2:
    	player = "THIEF"
    	PP = 10
    	basic = 20
    	PV = 75
        filePP = open("PP.txt", "w")
        filePP.write(str(PP))
        filePP.close()
        fileBasic = open("basic.txt", "w")
        fileBasic.write(str(basic))
        fileBasic.close()
        filePV = open("PV.txt", "w")
        filePV.write(str(PV))
        filePV.close()
        assist = "FALCON"
        basicAssist = 4
        PVAssist = 5
        fileAssist = open("assist.txt", "w")
        fileAssist.write(assist)
        fileAssist.close()
        fileBasicAssist = open("basicAssist.txt", "w")
        fileBasicAssist.write(str(basicAssist))
        fileBasicAssist.close()
        filePVAssist = open("PVAssist.txt", "w")
        filePVAssist.write(str(PVAssist))
        filePVAssist.close()
    elif classes == 3:
    	player = "WARRIOR"
    	PP = 15
    	basic = 10
    	PV = 100
        filePP = open("PP.txt", "w")
        filePP.write(str(PP))
        filePP.close()
        fileBasic = open("basic.txt", "w")
        fileBasic.write(str(basic))
        fileBasic.close()
        filePV = open("PV.txt", "w")
        filePV.write(str(PV))
        filePV.close()
        assist = "SQUIRE"
        basicAssist = 6
        PVAssist = 3
        fileAssist = open("assist.txt", "w")
        fileAssist.write(assist)
        fileAssist.close()
        fileBasicAssist = open("basicAssist.txt", "w")
        fileBasicAssist.write(str(basicAssist))
        fileBasicAssist.close()
        filePVAssist = open("PVAssist.txt", "w")
        filePVAssist.write(str(PVAssist))
        filePVAssist.close()
    elif classes == 4:
    	player = "WIZARD"
    	PP = 15
    	basic = 15
    	PV = 75
        filePP = open("PP.txt", "w")
        filePP.write(str(PP))
        filePP.close()
        fileBasic = open("basic.txt", "w")
        fileBasic.write(str(basic))
        fileBasic.close()
        filePV = open("PV.txt", "w")
        filePV.write(str(PV))
        filePV.close()
        assist = "BLACK CAT"
        basicAssist = 5
        PVAssist = 4
        fileAssist = open("assist.txt", "w")
        fileAssist.write(assist)
        fileAssist.close()
        fileBasicAssist = open("basicAssist.txt", "w")
        fileBasicAssist.write(str(basicAssist))
        fileBasicAssist.close()
        filePVAssist = open("PVAssist.txt", "w")
        filePVAssist.write(str(PVAssist))
        filePVAssist.close()
    else:
        print "ERROR, YOU NEED TO TYPE 1, 2, 3 OR 4."
    print "YOUR SETTINGS HAVE BEEN SAVED, IF YOU WANT TO PLAY THE GAME, RESTART THE PROGRAM."
else:
    print "ERROR, YOU NEED TO TYPE 1, 2, 3 OR 4."
