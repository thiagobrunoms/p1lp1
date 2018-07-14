#intersecao entre array

a = [1, 4, 5, 6, 7, 8, 9, 12, 13, 15, 20, 1, 3, 5, 5, 6, 8]
b = [0, 1, 5, 7, 9, 10, 12, 13, 17, 20, 21, 20, 1, 3]

intersection = []
for va in a:
    for vb in b:
        if va == vb and va not in intersection: 
            intersection.append(va)
            break

intersection.sort()
print(intersection)
