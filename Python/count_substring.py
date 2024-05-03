def count_substring(string, sub_string):
    num_of_occurance = 0
    index = string.find(sub_string)
    while index != -1:
        num_of_occurance += 1
        # print(string, index)
        string = string[index+1:]
        index = string.find(sub_string)
    return num_of_occurance

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
