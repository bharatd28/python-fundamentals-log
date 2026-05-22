dict={"bharat":"diwan","Avanish":"Diwan"}
print(dict["bharat"])
# Here "bharat" is key and "diwan" is value
print(dict.get("sooraj"))
# this would return none and not an error
print(dict.keys())
print(dict.values())
for keys in dict.keys():
    print(keys,dict[keys])
    # gives all the keys 
for keys,values in dict.items():
    print(keys,values)

# Dictionary methods
manager={112:99,121:54,124:84}
junior={127:69,182:64,169:42}

junior.update(manager) # updates junior dict with managerss
print(junior)

manager.clear() # clears manager dictionary
print(manager)

junior.pop(127) # pops value 127
print(junior)

junior.popitem() # pops last item
print(junior)

del manager # deletes it

del junior[169]
print(junior) # deletes key 169 and value




