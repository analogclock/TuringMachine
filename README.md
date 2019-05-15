# TuringMachine
PROJECT TITLE: Turing Machine

PURPOSE OF PROJECT: Simulate a turing machine reading an input and rejecting, looping, or halting on it, and print the string being modified as the machine reads through it

VERSION or DATE: 14 May 2019

HOW TO START THIS PROJECT: 
In the terminal, navigate to the folder containing this project. 
The text file with the machine description should be in this folder. Else, you can provide the file’s pathname as the file input. Run as python <filename>.py <file>.txt <input string>. For example:
python proj3.py 0n1n.txt 000111
  
AUTHORS: Hoffmann, Greer; Marbach, Alice

USER INSTRUCTIONS:
Give an input using valid tape symbols, but giving an invalid symbol will cause it to reject.
To represent a blank space, use '_'.

KNOWN ISSUES:
Due to indexing challenges, the machine always accepts the empty string (“” or ‘’), even if the L(M) does not have a rule for that. It also halts on all inputs

:)