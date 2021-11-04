ordinals = range(9)

for num in ordinals:
    num = num + 1
    if num == 1:
        print(f'{num}st')
    elif num == 2:
        print(f'{num}nd')
    else:
        print(f'{num}th')
