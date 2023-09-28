def solution(s):
    cleaned_str=s.replace('-','')
    i = len(cleaned_str) - 1
    count_array = []
    previous_count = 0
    while i >= 0:
        if cleaned_str[i] == '<':
            previous_count = previous_count + 1
        count_array.insert(0, previous_count)
        i = i - 1

    final_count = 0
    for i,char in enumerate(cleaned_str):
        if char == '>':
            final_count = final_count + count_array[i]
    return final_count*2