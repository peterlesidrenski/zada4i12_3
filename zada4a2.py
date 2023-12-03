n = int(input())
counter_0_9 = 0
counter_10_19 = 0
counter_20_29 = 0
counter_30_39 = 0
counter_40_49 = 0
counter_50_59 = 0
counter_60_69 = 0
counter_70_79 = 0
counter_80_89 = 0
counter_90_99 = 0


for i in range(n):
    new_number = int(input())
    if 0 <= new_number <=9:
        counter_0_9 += 1
    elif 10 <= new_number <= 19:
        counter_10_19 += 1
    elif 20 <= new_number <= 29:
        counter_20_29 += 1
    elif 30 <= new_number <= 39:
        counter_30_39 += 1
    elif 40 <= new_number <= 49:
        counter_40_49 += 1
    elif 50 <= new_number <= 59:
        counter_50_59 += 1
    elif 60 <= new_number <= 69:
        counter_60_69 += 1
    elif 70 <= new_number <= 79:
        counter_70_79 += 1
    elif 80 <= new_number <= 89:
        counter_80_89 += 1
    elif 90 <= new_number <= 99:
        counter_90_99 += 1

if counter_0_9 >= 1:
    print(f"Numbers of range 1-9 is/are {counter_0_9}. this is {counter_0_9/n*100}% from all numbers")
if counter_10_19 >= 1:
    print(f"Numbers of range 10-19 is/are {counter_10_19}. this is {counter_10_19/n*100}% from all numbers")
if counter_20_29 >= 1:
    print(f"Numbers of range 20-29 is/are {counter_20_29}. this is {counter_20_29/n*100}% from all numbers")
if counter_30_39 >= 1:
    print(f"Numbers of range 30-39 is/are {counter_30_39}. this is {counter_30_39/n*100}% from all numbers")
if counter_40_49 >= 1:
    print(f"Numbers of range 40-49 is/are {counter_40_49}. this is {counter_40_49/n*100}% from all numbers")
if counter_50_59 >= 1:
    print(f"Numbers of range 50-59 is/are {counter_50_59}. this is {counter_50_59/n*100}% from all numbers")
if counter_60_69 >= 1:
    print(f"Numbers of range 60-69 is/are {counter_60_69}. this is {counter_60_69/n*100}% from all numbers")
if counter_70_79 >= 1:
    print(f"Numbers of range 70-79 is/are {counter_70_79}. this is {counter_70_79/n*100}% from all numbers")
if counter_80_89 >= 1:
    print(f"Numbers of range 80-89 is/are {counter_80_89}. this is {counter_80_89/n*100}% from all numbers")
if counter_90_99 >= 1:
    print(f"Numbers of range 90-99 is/are {counter_90_99}. this is {counter_90_99/n*100}% from all numbers")




