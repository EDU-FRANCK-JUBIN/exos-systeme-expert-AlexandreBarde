from pyDatalog import pyDatalog

pyDatalog.clear()

pyDatalog.create_terms('rectangle, isocele, equi, isoRect, P, TroiscotesPareil, angles60, DeuxcotesPareil, angleDroit, deuxAngles45, X')

equi(P) <= TroiscotesPareil(P) & angles60(P)
isocele(P) <= DeuxcotesPareil(P)
rectangle(P) <= angleDroit(P)
isoRect(P) <= angleDroit(P) & deuxAngles45(P)

pyDatalog.assert_fact('angleDroit', 'Triangle rectangle')
pyDatalog.assert_fact('angleDroit', 'Triangle rectangle isocèle')
pyDatalog.assert_fact('deuxAngles45', 'Triangle rectangle isocèle')

print(pyDatalog.ask('angleDroit(X)'))
print(pyDatalog.ask('deuxAngles45(X)'))