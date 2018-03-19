#This file would test the ignoreWords function, and we will ignore case
import kwic
document1 = "Design is hard.\nLet's just implement.";

assert(kwic.kwic(document1,ignoreWords = ["is"]) == kwic.kwic(document1,ignoreWords = ["IS"]))
assert(kwic.kwic(document1,ignoreWords = ["is","hard."]) == kwic.kwic(document1,ignoreWords = ["Is","hard."]))
assert(kwic.kwic(document1,ignoreWords = ["is","hard."]) == kwic.kwic(document1,ignoreWords = ["Is","HArd."]))
assert(kwic.kwic(document1,ignoreWords = ["is","hard."]) == kwic.kwic(document1,ignoreWords = ["is","haRd."]))
