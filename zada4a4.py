"""n = int(input())
list1 = []
people=[]
history = []
OTs = []
python = []
fizi4esko = []
for i in range(n):
    new_num = int(input())
    people.append(new_num)
    if new_num <= 5:
        list1.append(new_num)
    elif 6 <= new_num and new_num <= 12:
        history.append(new_num)
    elif 13 <= new_num and new_num <= 25:
        OTs.append(new_num)
    elif 26 <= new_num and new_num <= 40:
        python.append(new_num)
    elif 40 < new_num:
        fizi4esko.append(new_num)

fiz = round(sum(list1) / sum(people) * 100, 2)
his = round(sum(history)/sum(people) * 100, 2)
ots = round(sum(OTs)/sum(people) * 100, 2)
pyt = round(sum(python)/sum(people) * 100, 2)
fizi4 = round(sum(fizi4esko)/sum(people) * 100, 2)



print(f'{fiz}%')
print(f'{his}%')
print(f'{ots}%')
print(f'{pyt}%')
print(f'{fizi4}%')"""
    

n = int(input())
people_all = 0
people_fiz = 0
people_history = 0
people_ots = 0
people_python = 0
people_fizi4esko = 0
for i in range(n):
    new_num = int(input())
    people_all += new_num
    if new_num <= 5:
        people_fiz += new_num
    elif 6 <= new_num and new_num <= 12:
        people_history += new_num
    elif 13 <= new_num and new_num <= 25:
        people_ots += new_num
    elif 26 <= new_num and new_num <= 40:
        people_python += new_num
    elif 40 < new_num:
        people_fizi4esko += new_num

print(round people_fiz/people_all*100, 2)
print(people_history/people_all*100)
print(people_ots/people_all*100)
print(people_python/people_all*100)
print(people_fizi4esko/people_all*100)