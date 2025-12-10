with open('puzzleInput.txt') as f:
    input = [line.strip() for line in f]
    # input = ['L77','R33','R54','R123','L50','L50','L120']

min,max = 0, 99

def password_cracker(input: list[str]):
    cur = 50
    zero_count = 0

    for i in input:
        print('zero_count', zero_count)
        if i[0] == 'R':
            right = int(i[1:])
            print('right', right)
            cur = (cur + right) % 100
            print('right new cur', cur)
            if cur == 0:
                zero_count += 1
        if i[0] == 'L':
            left = int(i[1:])
            print('left', left)
            cur = (cur - left) % 100
            print('left new cur', cur)
            if cur == 0:
                zero_count += 1

        
    return zero_count 

print(password_cracker(input))
