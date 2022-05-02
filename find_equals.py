def find_equals(num_list = [1,2,3,4,5,6,7,8,9], exp_list = ["+", "-", ""], target = 100):
    return_list = []
    #numbers
    num_list = num_list
    #expressions
    exp = exp_list
    #bits
    if len(num_list) <= 1: #Requires at least 2 numbers in list
        if len(num_list) == 0:
            return return_list
        if (num_list[0] == target):
            return_list.append(f"{num_list[0]}")
            return return_list
        else:
            return return_list
    else:
        bits = [0] * (len(num_list)-1)
    #total of equals
    #total = 0

    for x in range(len(exp) ** len(bits)):
        #Test Print
        test_string = ""
        for z in range(len(bits)):
            test_string += str(num_list[z])
            if bits[z] <= len(exp) - 1:
                test_string += str(exp[bits[z]])
        test_string += str(num_list[len(bits)])
        if eval(f"{test_string} == {target}"):
            #total += 1
            return_list.append(test_string)
            #print(f"{test_string} == {target}")
        #Bit Counter
        bits[0] += 1
        for y in range(len(bits) - 1):
            if bits[y] >= len(exp):
                bits[y] = 0
                bits[y + 1] += 1
    #print(f"Total {target}'s found: {total}")
    return return_list
#print(find_equals([1,2,3,4,5], ["+"], 15))
#print(find_equals([1], [], 1))
print(find_equals())
