#This file would test if the program sort string nicely without any optional argument note that we didn't add ignore case function in this version
import kwic

document1 = ". . a";
assert(kwic.kwic(document1) == [(['.', '.', 'a'], 0), (['.', 'a', '.'], 0), (['a', '.', '.'], 0)])