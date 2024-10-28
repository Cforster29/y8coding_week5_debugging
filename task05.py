print("Where were you born? ")
var = input()
print("Where do you live now? ")
var = input()
print("So, aside from", var, "and", var, "Is there anywhere else you've lived?")


### What was wrong ?
### DISCUSS HERE:
### This is a logical error, and there are two problems with this. 1. The code is trying to use 'var = input' as a way to make the user input their answer to the question, but because 'var' has no relation to the line above it, in the ending line it prints nothing. 2. IF 'var = input()' were to work, this would still not print the correct text due to the fact that the same variable ('var') is used twice.
### Was this a... syntax, logical or runtime error?