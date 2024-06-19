l=[7,4,2,6,9,1,5]
a=l.index(9)
print(a)

# Append
l.append(10)
print(l)

# Extend
l.extend([11,12,13])
print(l)

# Insert
l.insert(2,3)
print(l)

# pop
l.pop(2)
print(l)

# remove
l.remove(7)
print(l)

# clear
l.clear()
print(l)

# reverse
l=[7,4,2,6,9,1,5]
l.reverse()
print(l)

# sort
l=[2,3,8,7,9,6,5]
l.sort()

# Count
l=[2,3,8,7,9,6,5,2,2]
print(l.count(2))