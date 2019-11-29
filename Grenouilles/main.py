from pyDatalog import pyDatalog

pyDatalog.clear()

pyDatalog.create_terms('croakes,eatflies,frog,chirps,sings,canary,green,jaune,P,X,Variable')

frog(P)  <= croakes(P) & eatflies(P)
canary(P) <= chirps(P) & sings(P)
green(P) <= frog(P)
jaune(P) <= canary(P)

pyDatalog.assert_fact('croakes', 'fritz')
pyDatalog.assert_fact('eatflies', 'fritz')

print(pyDatalog.ask("frog('fritz')"))
print(pyDatalog.ask("frog('totoalaplage')"))
print(pyDatalog.ask('green(X)'))
print(pyDatalog.ask('green(fritz)'))
print(pyDatalog.ask('green(xyz)'))