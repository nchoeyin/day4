def TreasureMap():
    print("Welcome to the Treasure map")
    symbol = "\U0001F600"
    x = "X"
    print('''
                11   12   13
                21   22   23
                31   32   33
          ''')
    move = int(input("Enter the position to move: "))
    def display():
         row1 = ['🏳','🏳','🏳']
         row2 = ['🏳','🏳','🏳']
         row3 = ['🏳','🏳','🏳']
         totrow = [row1, row2, row3]
         for i in range(0,3):
             print(totrow[i])
    if move == 23:
        row2[2] = symbol
        display()
    else:
        lastdigit = move%10
        firstdigit = move/10
        totrow[firstdigit][lastdigit] = x
        display()
        
TreasureMap()
