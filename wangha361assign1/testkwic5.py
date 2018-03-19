#This file would test if the program will return error if we didn't input the valid optional arguments
import kwic
document = "test test";
assert(kwic.kwic(document,ignorewords = ["is"]) == 1)
assert(kwic.kwic(document,ignoreWords = ["is"]) != 1)
assert(kwic.kwic(document,BadArgument = 1) == 1)