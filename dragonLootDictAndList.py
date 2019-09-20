def displayInventory(inventory):
    totalInventory = 0
    for k, v in inventory.items():
        totalInventory += v
        print(str(v) + ' ' + k)
    print('You have ' + str(totalInventory) + ' total items.')

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory.keys():
            inventory[i] += 1
        elif i not in inventory.keys():
            inventory.update({i : 1})

    return inventory


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
