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
    print "\n\nCHOOSE A BREED(number):\n1.ELF\n2.OGRE\n3.DWARF\n4.HUMAN\n"
    breeds = input("ENTER: ")
    print "\n\nCHOOSE A CLASS(number):\n1.MAGE\n2.THIEF\n3.WARRIOR\n4.WIZARD\n"
    classes = input("ENTER: ")
    
else:
    print "ERROR, YOU NEED TO TYPE 1, 2, 3 OR 4."
