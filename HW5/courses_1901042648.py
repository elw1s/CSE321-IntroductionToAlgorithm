def sortKey(obj):
    return obj[2]


def max_course(courses,n):
    attended = []
    
    courses.sort(key = sortKey)

    num_attended = 0
    attended.append(courses[0])

    for i in range(1,n):
        if courses[i][1] >= courses[num_attended][2]:
            attended.append(courses[i])
            num_attended = i

    return attended

courses = [["English",1,2],["Mathematics",3,4],["Physics",0,6],["Chemistry",5,7],["Biology",8,9],["Geography",5,9]]
n = len(courses)
print("Maximum number of courses a student can attend is",max_course(courses,n))