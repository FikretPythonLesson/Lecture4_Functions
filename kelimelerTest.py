# -*- coding: utf-8 -*-

import kelimeler

name = raw_input("What is your name ?")
lastName = kelimeler.getLastWord(name)
firstName = kelimeler.getFirstWord(name)

print "Hello Mr. ", lastName
print "Hi ", firstName, " how are you doing?"

