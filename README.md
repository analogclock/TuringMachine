# TuringMachine
PROJECT TITLE: Turing Machine

PURPOSE OF PROJECT: Simulate a turing machine reading an input and rejecting, looping, or halting on it, and print the string being modified as the machine reads through it

VERSION or DATE: 14 May 2019

HOW TO START THIS PROJECT: 
In the command line, navigate to the folder containing this project. 
The text file with the machine description should be in this folder. Else, you can provide the file’s pathname as the file input. Run as python [filename].py [file].txt [input string] 
For example: python proj3.py 0n1n.txt 000111
  
AUTHORS: Hoffmann, Greer; Marbach, Alice

USER INSTRUCTIONS:
Give an input using valid tape symbols, but giving an invalid symbol will cause it to reject.
To represent a blank space, use '_'.

KNOWN ISSUES:
Due to indexing challenges, the machine (proj3.py) always accepts the empty string (“” or ‘’), even if the L(M) does not have a rule for that. It also halts on all inputs

N.B.: There are two implementations of the same program (proj3.py, alt-dict.py). The difference is I use a dictionary in alt-dict.py, and a list of lists in proj3.py. They behave exactly the same and have the same known issues.
I'm keeping proj3.py here because that is the one I submitted on time. Later I want to delete it because I don't want people to see a unnecessary stupid loop in a recursive call.
