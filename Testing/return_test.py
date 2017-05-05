import return_data as gs

player = input('Enter name: ').upper()

a = gs.get_data(player)
print(a)
for z in a:
    print('Saved games where name = ' + z[1])
    print('ID' + ' ' + "Winnings")
    print(str(z[0]) + ' ' + str(z[2]))