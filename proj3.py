#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
# Greer Hoffmann & Alice Marbach

# Reads arguments from command line.
# The first arg is the text file of the turing machine,
# the second is the input string.
import sys
txt = open(sys.argv[1]) # txt file to read from
inputStr = sys.argv[2]  # input string
# print('arg1: {}'.format(txt))
# print('arg2: {}'.format(inputStr))
print('Input String: {}'.format(inputStr))

# Turn input string into a character array
inputStrArr = list(inputStr)
# print('inputStrArr: {}'.format(inputStrArr))
# print(inputStrArr)

# READING FROM TEXT FILE

# Uses readline() to read the first line containing # of states
# cast to int then create an int array from 0 to num of states
numStates= int(txt.readline())
statesArr = [] 
k = 0
while (k<numStates):
    statesArr.insert(k,k)
    k+=1
print('Num of States: {}'.format(statesArr))
# print(statesArr)

# create array of valid input chars
valCharsStr = txt.readline().strip()
charList = list(valCharsStr)
print("Tape Symbols: {}".format(charList))

# create array of accepting states
accStatesStrArr = txt.readline().split()
print("Accepting States: {}".format(accStatesStrArr))

linesList = [] # declare empty list to add lines later
m = 0
for line in txt:
    linesList.insert(m,line.split())
    m+=1

# print("linesList: {}".format(linesList))

txt.close() # close text file after running

# READINPUT
# inputs: inputArr, the arr representation of inputString
#         linesList, the list of rules for the TM
#         accStates, the list of accepting states
# outputs: 
def readInput(inputArr, linesList, accStates):
    if (inputStr == "" or inputStr == ''):
        print('Accept')
        return
    readInputHelper(len(linesList),len(inputArr),inputArr, linesList, 0, 0, accStates)

# READINPUTHELPER
# inputs: y, the length of linesList
#         z, the length of inputArr
#         inputArr, the arr representation of inputString
#         linesList, the list of rules for the TM
#         accStates, the list of accepting states
# outputs: 
# Description: prints the turing machine as it reads the input string
def readInputHelper(y,z,inputArr, linesList, state, pos, accStates):
    i = 0
    while (i<y):
#        print('i: {}'.format(i))
        # check that it contains valid chars
        if ((int(linesList[i][0]) == state) and (linesList[i][1] == inputArr[pos])):
            # update current state
            state = (int(linesList[i][4]))
            # update current symbol to prArr[i][2]
            inputArr[pos] = linesList[i][2]
            # determine which way to move
            if (linesList[i][3]=='<'):
                if (pos == 0):
                    pos = 1 # because then you'll move left
                pos-=1 # move left on the tape
            else:
                if (pos == z-1): # if pos is at end of the arr
                    inputArr.append('_') # insert a blank space at end of str
                pos+=1 # else move right on the tape
            break
        if i == y-1: # if there is no rule for it, reject
            print('Rejected')
            return
        i+=1 # else keep looking

    prStr = ''.join(inputArr) # makes string representation of prStrArr
    print(prStr[0:pos]+'[q{}]'.format(state)+prStr[pos+1:]) # print the str and current state

    # check if current state
    b = 0 
    for b in range(len(accStates)):  
        if (state == int(accStates[b])):
           print('Accept')
           break
        b+=1
    else:
        readInputHelper(y,z,inputArr,linesList,state,pos,accStates)

print(inputStr)
readInput(inputStrArr,linesList,accStatesStrArr)
    # blah blah blah