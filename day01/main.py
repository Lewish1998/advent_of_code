with open('puzzleInput.txt') as f:
    input = [line.strip() for line in f]
    # input = ['R29', 'L3', 'L46', 'L25', 'L38']#, 'R43', 'L20', 'R9', 'L6', 'L47']
    # 50 > 79 < 3 76 < 46 30 < 25 5 < 38 67 > 43 10 < 20 90 > 9 99 < 6 93 < 47 46
# The dial starts by pointing at 50.
# ['R29', 'L3', 'L46', 'L25', 'L38', 'R43', 'L20', 'R9', 'L6', 'L47']


min,max = 0, 99


def password_cracker(input: list[str]):
    cur = 50
    temp_list: list[int] = [cur]
    zero_count = 0
    step = 0
    loop = True

    # print('CUR START', cur)
    for i in input:
        step += 1
        print(step)
        # print(cur)
        if i[0] == 'R':
            rup = int(i[1:]) # 79
            if cur + rup > 99:
                loop = True
                while loop:
                    # print('FIRST rup', rup)
                    rup -= cur # THAT'S WHAT IT SHOULD END ON
                    # print('SECOND rup', rup)
                    cur = 0
                    cur += rup # < so that's correct 
                    # print('CUR RUP', cur)
                    if cur + rup <= 99:
                        loop = False
                        break
            else:
                cur += rup
            # print('CUR RUP', cur)
            

        elif i[0] == 'L':
            ldn = int(i[1:])
            if cur - ldn < 0:
                loop = True
                while loop:
                    # print('FIRST ldn', ldn)
                    ldn -= cur # THAT'S WHAT IT SHOULD END ON
                    # print('SECOND ldn', ldn)
                    cur = 100 if cur - ldn != 0 else 0
                    cur -= ldn # < so that's correct 
                    # print('CUR LDN', cur)
                    if cur - ldn >= 0:
                        loop = False
                        break
            else:
                cur -= ldn
            # print('CUR LDN', cur)

        
        if cur == 0:
            zero_count += 1
    # print('end cur', cur)
    return zero_count 


print(password_cracker(input))
