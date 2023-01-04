N,D= map(int, input().split())
counter = 0
Points = []
while counter < N:
    A, B = input().split(' ')
    Points.append([int(A), int(B)])
    counter += 1

locdrone = []
x, y = input().split(' ')
locdrone.append(int(x)),locdrone.append(int(y))


destination = []
AX, BX = input().split(' ')
destination.append(int(AX)), destination.append(int(BX))

dict = {}
import sys
lst = []

if (((locdrone[0] - destination[0]) ** 2) + ((locdrone[1] - destination[1]) ** 2))**(1 / 2)<= D:
    print("y")
    sys.exit()

for t in range(N):
    if (((Points[t][0] - locdrone[0]) ** 2) + ((Points[t][1] - locdrone[1]) ** 2))**(1 / 2)<= D:
        dict[t] = [Points[t][0], Points[t][1]]

counter = 0
similarity = dict.copy()
while len(dict) > 0:
    for f in dict:
        if (((dict[f][0] - destination[0]) ** 2) + ((dict[f][1] - destination[1]) ** 2))**(1 / 2)<= D:
            print("y")
            sys.exit()


    else:
        Test = False
        dict2 = dict.copy()
        for u in dict2:
            box = dict.pop(u)
            lst.append(box)
            for z in dict2:
                if (((dict2[z][0] - box[0]) ** 2) + ((dict2[z][1] - box[1]) ** 2))**(1 / 2)<= D:
                    if [dict2[z][0], dict2[z][1]] not in lst:
                        dict[counter] = dict2[z]
                        counter += 1

                for num in range(N):
                    if num not in similarity:
                        if (((Points[num][0] - box[0]) ** 2) + ((Points[num][1] - box[1]) ** 2))**(1 / 2)<= D:
                            if [Points[num][0], Points[num][1]] not in lst:
                                Test = True
                                save = num
                                dict[num] = [Points[num][0], Points[num][1]]

        if Test == True:
            dict2[num] = [Points[save][0], Points[save][1]]
        if dict == similarity:
            print('n')
            sys.exit()

print('n')
