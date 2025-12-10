with open('puzzleInput.txt') as f:
    input = [line.strip() for line in f]

min,max = 0, 99

def password_cracker(input: list[str]):
    cur = 50
    zero_count = 0

    for i in input:
        if i[0] == 'R':
            right = int(i[1:])
            for _ in range(right):
                cur += 1
                if cur == 100:
                    zero_count += 1
                    cur = 0
                if cur == 0:
                    zero_count += 1

        if i[0] == 'L':
            left = int(i[1:])
            for _ in range(left):
                cur -= 1
                if cur == -1:
                    zero_count += 1
                    cur = 99
                if cur == 0:
                    zero_count += 1
                    
        
    return zero_count 

print(password_cracker(input))
