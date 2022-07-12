import random
cointoss = int(random.random()*10)
if cointoss >= 5:
    print(f"You won!! {cointoss}")
else:
    print(f"You lost!! {cointoss}")
    
