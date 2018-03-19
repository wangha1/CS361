#This file would test the ignoreWords function, note we only accept lowercase in this version.
import kwic
document1 = "Design is hard.\nLet's just implement.";
document2 = "This is not a sentence.\nNeither is this.";
assert(kwic.kwic(document1,ignoreWords = ["is"]) == [(["Design", "is", "hard."], 0),  (["hard.", "Design", "is"], 0),  (["implement.", "Let's", "just"], 1),  (["just", "implement.", "Let's"], 1),  (["Let's", "just", "implement."], 1)])
assert(kwic.kwic(document1,ignoreWords = ["is","hard."]) == [(["Design", "is", "hard."], 0),  (["implement.", "Let's", "just"], 1),  (["just", "implement.", "Let's"], 1),  (["Let's", "just", "implement."], 1)])
assert(kwic.kwic(document2,ignoreWords = ["is."]) == [(["a", "sentence.", "This", "is", "not"], 0),  (["is", "not", "a", "sentence.", "This"], 0),  (["is", "this.", "Neither"], 1),  (["Neither", "is", "this."], 1),  (["not", "a", "sentence.", "This", "is"], 0),  (["sentence.", "This", "is", "not", "a"], 0),  (["This", "is", "not", "a", "sentence."], 0),  (["this.", "Neither", "is"], 1)])
assert(kwic.kwic(document2,ignoreWords = ["is"]) == [(["a", "sentence.", "This", "is", "not"], 0),  (["Neither", "is", "this."], 1),  (["not", "a", "sentence.", "This", "is"], 0),  (["sentence.", "This", "is", "not", "a"], 0),  (["This", "is", "not", "a", "sentence."], 0),  (["this.", "Neither", "is"], 1)])