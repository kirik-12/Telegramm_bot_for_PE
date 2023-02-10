import foto as ft
import random

que_ft = ft.all_photos
random.shuffle(que_ft)
# !!!!!!!!!!!!!!!!!!!!!!!!!!! не забудь изменить пятёрку на 15
question_foto_ans = que_ft[0:5]

lol = {
    '2':1,
    '3':1,
    '4':1,
}

print(lol.values())
print(len(lol.values()))
print('_______________')
print(list(lol.values()))
print(len(list(lol.values())))

count = 0
for i in range(len(lol.values())):
            if question_foto_ans[i][2] == list(lol.values())[i]: 
                count +=1
# print(count)
