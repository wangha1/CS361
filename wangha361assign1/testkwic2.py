#This file will test if we can rotate string correctly, the input should be sorted because we don't have a sort function right now

import kwic

document1 = "a\na b";
assert(kwic.kwic(document1) == [(["a"],0),(["a","b"],1),(["b","a"],1)] or kwic.kwic(document1) == [(["a"],0),(["b","a"],1),(["a","b"],1)]);
