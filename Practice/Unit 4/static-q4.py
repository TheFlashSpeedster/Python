n = int(input())

list1 = []

for i in range(n):
    data = input().split()
    list1.append(data)

def highest_mark(list1):
    max_mark = max(int(i[1]) for i in list1)
    print(max_mark) # max mark

    top_students = [i[0] for i in list1 if int(i[1]) == max_mark]
    return(top_students) # students with max mark
    
# Students With Max Marks
print(highest_mark(list1))