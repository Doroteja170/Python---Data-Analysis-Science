from prettytable import PrettyTable
x=PrettyTable()

x.add_column('Pokemon name',['Pikachu','Squirtel','Charamander'])
x.add_column('Type',['Electric','Water','Fire'])
x.align="r"
print(x)