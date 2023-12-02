numbers = ['1','2','3','4','5','6','7','8','9','0']

with open('main.txt', 'r') as file:
    string_data = file.readlines()

    for line in string_data:
        line_numbers = []
        total = []

        for i in line:
            if i.isdigit():
                line_numbers.append(i)

        if line_numbers:
            number = int(''.join(line_numbers))
            print(number)

    