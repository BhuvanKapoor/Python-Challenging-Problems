# %%
'''
A primary school has students with roll numbers 1 to 60 and also has seats with numbers 1 to 60 printed on them. Normally each student sits in the seat as per roll number. One day the students sit differently as the teacher told them so. It is possible some students did not change position. Or some set of students form friend circles and change the seats only among themselves.
Your input is the list of numbers from 1 to 60 rearranged as per the new seating. The 4th number of the list should be interpreted as the roll number of students in seat number 4. (To make it convenient for Python, create seat number 0 and and assume teacher takes that seat always).
Your job is identiying the friends circle in the new rearrangment. An example friend circle could be [1, 7, 2, 24, 8]. This means these students changed seats among themselves as below:
1 → 7 → 2 → 24 → 8 → 1
A student refusing to move would make (theoretically) a friend circle of length 1. Two students making mutual exchange will be a friend circle of length 2. etc
Your problem is, given an input list which is a rearrangment of 1 to 60 to print all the friend circles for that rearrangement.
'''

def find_friend_circles(seating_arrangement):
    n = len(seating_arrangement)
    visited = [False] * n
    friend_circles = []

    for i in range(n):
        if not visited[i]:
            friend_circle = []
            current_student = i
            while not visited[current_student]:
                visited[current_student] = True
                friend_circle.append(seating_arrangement[current_student])
                current_student = seating_arrangement[current_student] - 1 

            if len(friend_circle) > 1:
                friend_circles.append(friend_circle)

    return friend_circles
    
seating_arrangement = [4, 1, 7, 2, 24, 8, 6, 5, 3, 10, 9, 11, 12, 15, 14, 13, 17, 16, 18, 19, 22, 21, 20, 23, 25, 28, 27, 26, 29, 30, 33, 32, 31, 34, 35, 36, 39, 38, 37, 40, 42, 41, 44, 43, 45, 46, 47, 50, 49, 48, 53, 52, 51, 54, 55, 56, 57, 58, 59, 60]
friend_circles = find_friend_circles(seating_arrangement)

for i, circle in enumerate(friend_circles):
    print(f"Friend Circle {i + 1}: {circle}")