#This file would test the periodsToBreak function.
import kwic
document1 = "Hello world. This is a test\nhopefully it turns out okay";
document2 = "Hello there.\nHello there, buddy.\nHello and goodbye, buddy.\nHello is like buddy Goodbye!";
document3 = "Hello there. Hello there, buddy. Hello and goodbye, buddy. Hello is like buddy Goodbye!"

assert(kwic.kwic(document1,periodsToBreaks = True) == [(["a", "test", "hopefully", "it", "turns", "out", "okay", "This", "is"], 1),  (["Hello", "world."], 0),  (["hopefully", "it", "turns", "out", "okay", "This", "is", "a", "test"], 1),  (["is", "a", "test", "hopefully", "it", "turns", "out", "okay", "This"], 1),  (["it", "turns", "out", "okay", "This", "is", "a", "test", "hopefully"], 1),  (["okay", "This", "is", "a", "test", "hopefully", "it", "turns", "out"], 1),  (["out", "okay", "This", "is", "a", "test", "hopefully", "it", "turns"], 1),  (["test", "hopefully", "it", "turns", "out", "okay", "This", "is", "a"], 1),  (["This", "is", "a", "test", "hopefully", "it", "turns", "out", "okay"], 1),  (["turns", "out", "okay", "This", "is", "a", "test", "hopefully", "it"], 1),  (["world.", "Hello"], 0)])
assert(kwic.kwic(document2,periodsToBreaks = True) == kwic.kwic(document2,periodsToBreaks = True));