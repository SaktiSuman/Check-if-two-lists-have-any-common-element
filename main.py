def common_element(set1, set2):
    result = False
    for x in set1:
        for y in set2:
            if x == y:
                return True
    return False

list1 = [12, 34, 45, 56, 78]
list2 = [23, 34, 99, 90, 80]
print(common_element(list1, list2))