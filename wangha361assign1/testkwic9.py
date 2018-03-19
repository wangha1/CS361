#This file would test whole program!!!!!!
import kwic
document1 = "Hello world. This is a test\nhopefully it turns out okay";
document2 = "Hello there.\nHello there, buddy.\nHello and goodbye, buddy.\nHello is like buddy Goodbye!";
document3 = "Hello there. Hello there, buddy. Hello and goodbye, buddy. Hello is like buddy Goodbye!"
document4 = "This pair? is good.\n So is this pair and that pair"
document5 = "?!go!!!od morning-!"
document6 = ". A B\n. A B C\n. A B C D"
document7 = "to be or not to be"
document8 = "hello here, hello there, hello everywhere"
document9 = "a b\nb c\na c"

assert(kwic.kwic(document1,periodsToBreaks = True) == [(["a", "test", "hopefully", "it", "turns", "out", "okay", "This", "is"], 1),  (["Hello", "world."], 0),  (["hopefully", "it", "turns", "out", "okay", "This", "is", "a", "test"], 1),  (["is", "a", "test", "hopefully", "it", "turns", "out", "okay", "This"], 1),  (["it", "turns", "out", "okay", "This", "is", "a", "test", "hopefully"], 1),  (["okay", "This", "is", "a", "test", "hopefully", "it", "turns", "out"], 1),  (["out", "okay", "This", "is", "a", "test", "hopefully", "it", "turns"], 1),  (["test", "hopefully", "it", "turns", "out", "okay", "This", "is", "a"], 1),  (["This", "is", "a", "test", "hopefully", "it", "turns", "out", "okay"], 1),  (["turns", "out", "okay", "This", "is", "a", "test", "hopefully", "it"], 1),  (["world.", "Hello"], 0)])
assert(kwic.kwic(document2,periodsToBreaks = True) == kwic.kwic(document2,periodsToBreaks = True));
assert(kwic.kwic(document4,listPairs = True) == ([(['and', 'that', 'pair', 'So', 'is', 'this', 'pair'], 1),   (['good.', 'This', 'pair?', 'is'], 0),   (['is', 'good.', 'This', 'pair?'], 0),   (['is', 'this', 'pair', 'and', 'that', 'pair', 'So'], 1),   (['pair', 'and', 'that', 'pair', 'So', 'is', 'this'], 1),   (['pair', 'So', 'is', 'this', 'pair', 'and', 'that'], 1),   (['pair?', 'is', 'good.', 'This'], 0),   (['So', 'is', 'this', 'pair', 'and', 'that', 'pair'], 1),   (['that', 'pair', 'So', 'is', 'this', 'pair', 'and'], 1),   (['this', 'pair', 'and', 'that', 'pair', 'So', 'is'], 1),   (['This', 'pair?', 'is', 'good.'], 0)],  [(('is', 'pair'), 2), (('is', 'this'), 2), (('pair', 'this'), 2)]))
assert(kwic.kwic(document5,ignoreWords = ["!GoOd"]) == [(['?!go!!!od', 'morning-!'], 0), (['morning-!', '?!go!!!od'], 0)])
assert(kwic.kwic(document6,listPairs = True) == ([(['.', 'A', 'B'], 0),   (['.', 'A', 'B', 'C'], 1),   (['.', 'A', 'B', 'C', 'D'], 2),   (['A', 'B', '.'], 0),   (['A', 'B', 'C', '.'], 1),   (['A', 'B', 'C', 'D', '.'], 2),   (['B', '.', 'A'], 0),   (['B', 'C', '.', 'A'], 1),   (['B', 'C', 'D', '.', 'A'], 2),   (['C', '.', 'A', 'B'], 1),   (['C', 'D', '.', 'A', 'B'], 2),   (['D', '.', 'A', 'B', 'C'], 2)],  [(('a', 'b'), 3), (('a', 'c'), 2), (('b', 'c'), 2)]))
assert(kwic.kwic(document7,listPairs = True) == ([(['be', 'or', 'not', 'to', 'be', 'to'], 0),   (['be', 'to', 'be', 'or', 'not', 'to'], 0),(['not', 'to', 'be', 'to', 'be', 'or'], 0),   (['or', 'not', 'to', 'be', 'to', 'be'], 0),   (['to', 'be', 'or', 'not', 'to', 'be'], 0),   (['to', 'be', 'to', 'be', 'or', 'not'], 0)],  []))
assert(kwic.kwic(document8,listPairs = True) == ([(['everywhere', 'hello', 'here,', 'hello', 'there,', 'hello'], 0),   (['hello', 'everywhere', 'hello', 'here,', 'hello', 'there,'], 0),   (['hello', 'here,', 'hello', 'there,', 'hello', 'everywhere'], 0),   (['hello', 'there,', 'hello', 'everywhere', 'hello', 'here,'], 0),   (['here,', 'hello', 'there,', 'hello', 'everywhere', 'hello'], 0),   (['there,', 'hello', 'everywhere', 'hello', 'here,', 'hello'], 0)],  []))
assert(kwic.kwic(document9,listPairs = True) == ([(['a', 'b'], 0), (['a', 'c'], 2), (['b', 'a'], 0), (['b', 'c'], 1), (['c', 'a'], 2), (['c', 'b'], 1)], []))
