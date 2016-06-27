#----------------------------------------------------------------------------------------
#falta definir os companheiros
#-------------------------------------------------------------------------------------------------
print "\n\n               SOULBOUND\n\n"
print "PRESS 1 TO PLAY\nPRESS 2 TO CREDITS\nPRESS 3 FOR INSTRUCTIONS\nPRESS 4 TO SAVE YOUR SETTINGS"
menu = input("\n\nENTER: ")
if menu == 1:
    print "\n\n"
elif menu == 2:
    print "\n\nCREDITS:\nEduardo Daemon Teixeira dos Santos\nMarcos Zlotnik\nRafael Utescher Stamillo"
elif menu == 3:
    print "\n\n"
elif menu == 4:
    print "\n\nSETTINGS\n\nObservaiton: if you want to change your class you will need to reset "
    print "the game deleting deleting all the files created by it."
    print "\n\nCHOOSE A RACE(number):\n1.ELF\n2.ORC\n3.DWARF\n4.HUMAN\n"
    race = input("ENTER: ")
    print "\n\nCHOOSE A CLASS(number):\n1.MAGE\n2.THIEF\n3.WARRIOR\n4.WIZARD\n"
    classes = input("ENTER: ")
    PP = 0
    basic = 0
    PV = 0
    dictRace = {1: "ELF", 2: "ORC", 3: "DWARF", 4: "HUMAN"}
    dictClasses = {1: "MAGE", 2: "THIEF", 3: "WARRIOR", 4: "WIZARD"}
    fileClasses = open("classes.txt", "w")
    fileClasses.write(dictClasses[classes])
    fileClasses.close()
    fileMoney = open("money.txt", "w")
    fileMoney.write("20")
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
        print "YOUR SETTINGS HAVE BEEN SAVED, IF YOU WANT TO PLAY THE GAME, RESTART THE PROGRAM"
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
        print "YOUR SETTINGS HAVE BEEN SAVED, IF YOU WANT TO PLAY THE GAME, RESTART THE PROGRAM"
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
        print "YOUR SETTINGS HAVE BEEN SAVED, IF YOU WANT TO PLAY THE GAME, RESTART THE PROGRAM"
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
        print "YOUR SETTINGS HAVE BEEN SAVED, IF YOU WANT TO PLAY THE GAME, RESTART THE PROGRAM"
    print "ERROR, YOU NEED TO TYPE 1, 2, 3 OR 4."
else:
    print "ERROR, YOU NEED TO TYPE 1, 2, 3 OR 4."
