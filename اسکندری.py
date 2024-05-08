def remove_all(xyz, value):
    while(value in xyz):
        index= xyz.index (value)
        xyz.pop(index)
        if(index< len(xyz)):
            xyz.insert(index,None)
xyz=[17.5,'220',34.354,4,13,9,13,"bahar",8,9,13]
remove_all(xyz,13)
print(xyz)
