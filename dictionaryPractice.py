# write a function named displayInventory() that would take any possible inventory
# and display it like the following:

# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12 }

def displayInventory(inventory):
    totalInventory = 0
    for k, v in stuff.items():
        totalInventory += v
        print(str(v) + ' ' + k)
    print('You have ' + str(totalInventory) + ' total items.')
    
displayInventory(stuff)
        
