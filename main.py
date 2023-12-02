numbers = ['1','2','3','4','5','6','7','8','9','0']
grand_total = 0

with open('day_1.txt', 'r') as file:
    string_data = file.readlines()

    for line in string_data:
        line_numbers = []

        for i in line:
            new_numbers = []
            
            if i.isdigit():
                line_numbers.append(i)

        if line_numbers:
            # number = int(''.join(line_numbers))
            number = (''.join(line_numbers))
            # print(number)
            
            if len(str(number)) < 2:
                new_numbers.append(number[0])
                
                grand_total += int(new_numbers[0])
                
            else: 
                new_numbers.append(number[0])
                new_numbers.append(number[-1])
                
                grand_total += (int(new_numbers[0]) + int(new_numbers[-1]))
                
                
    print(grand_total)
                

            