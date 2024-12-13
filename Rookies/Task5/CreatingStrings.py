text = ''.join(sorted(input("")))

results_set = set()

def CreatString(curret_str, remaining_chars, results_set):
    if len(remaining_chars) == 0:
        results_set.add(curret_str)
        return
    
    for i in range(len(remaining_chars)):
        if i > 0 and remaining_chars[i] == remaining_chars[i - 1]:
            continue

        char = remaining_chars[i]

        new_remaining_chars = remaining_chars[0:i] + remaining_chars[i+1:]

        CreatString(curret_str + char, new_remaining_chars, results_set)
        

CreatString("", text, results_set)

results_list = sorted(results_set)

print(len(results_list))
for str in results_list:
    print(str)