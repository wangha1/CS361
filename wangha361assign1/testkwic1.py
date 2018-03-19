#this file will test if we can split string properly, without taking any optional argument, and the input string will be already sorted and only contain one word because we didn't add sort function or rotate function in this version

import kwic

document1 = "a";
document2 = "a\nb";

assert(kwic.kwic(document1) == [(["a"],0)]);
assert(kwic.kwic(document2) == [(["a"],0),(["b"],1)]);
