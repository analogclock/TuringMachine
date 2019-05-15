#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
# Greer Hoffmann & Alice Marbach

# Read arguments from command line.
import sys
txt = open(sys.argv[1]) # Text file of the turing machine
inputStr = sys.argv[2]  # input string
# print('arg1: {}'.format(txt))
# print('arg2: {}'.format(inputStr))
print('Input String: {}'.format(inputStr))

# Turn input string into a character array
inputStrArr = list(inputStr)
# print('inputStrArr: {}'.format(inputStrArr))

# Uses readline() to read the first line containing # of states
# cast to int to create an int array from 0 to (num of states)-1 inclusive
numStates= int(txt.readline())
statesArr = [] 
k = 0
while (k<numStates):
    statesArr.insert(k,k)
    k+=1
print('States: {}'.format(statesArr))
# print(statesArr)

# create array of valid input chars
valCharsStr = txt.readline().strip()
charList = list(valCharsStr)
print("Tape Symbols: {}".format(charList))

# create array of accepting states
accStatesArr = txt.readline().split()
print("Accepting States: {}".format(accStatesArr))

# add to dictionary.
# The key is <state>.<symbol>, e.g. if I'm in state 0 and reading a 1, the key is 0.1
# Each key holds an array containing what to write to tape, direction to move, and the next state
m = 0
linesDict={}
for line in txt:
    l = line.split()
    key = '{}.{}'.format(l[0],l[1])
    linesDict[key] = [l[2],l[3],l[4]]
    # print('l: {}'.format(l))
    # print('Key: {}'.format(key))
    # linesList.insert(m,line.split())
    m+=1

# print('LinesDict: {}'.format(linesDict))
txt.close() # close text file after running

# RUNTM runs the TM.
# Takes the array representation of the input str, the dictionart
def runTM(inputArr, linesDict, accStates):
    if (inputStr == "" or inputStr == ''):
        print('Accept')
        return
    length = len(accStates)
    readInputHelper(inputArr, linesDict, 0, 0, accStates, length)

# Helper function for RUNTM
# Takes state, pos, and accStatesLen, which are constants so shouldn't be recalculated at every loop
def readInputHelper(inputArr, linesDict, state, pos, accStates, accStatesLen):
    b = 0 
    for b in range(accStatesLen): 
        s = int(state)
        accState = int(accStates[b])
        if (s == accState):
            print('Accept')
            return
        b+=1

    currChar = inputArr[pos]
    currKey = '{}.{}'.format(state,currChar)
    if not (linesDict.__contains__(currKey)): # in case invalid input char
        print('Reject')
        return

    rules = linesDict[currKey]
    # print('Rules: {}'.format(rules))
    inputArr[pos] = rules[0] 
    direction = rules[1]
    state = rules[2]
    if (direction == '<'):
        if (pos == 0):
            pos = 1
        pos -= 1
    else:
        if (pos == len(inputArr)-1):
            inputArr.append('_')
        pos+=1
    prStr = ''.join(inputArr) # makes string representation of prStrArr
    print(prStr[0:pos]+'[q{}]'.format(state)+prStr[pos+1:]) # print the str and current state    
    readInputHelper(inputArr,linesDict,state,pos,accStates, accStatesLen) # recursive call

print(inputStr)
runTM(inputStrArr, linesDict, accStatesArr)