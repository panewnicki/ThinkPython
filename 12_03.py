def most_frequent(text):
    
    my_dict = {}
    my_list = []
    
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            if letter not in my_dict:
                my_dict[letter] = 1
            else:
                my_dict[letter] += 1

    for key, value in my_dict.items():
        my_list.append((value, key))

    my_list.sort(reverse = True)
  
    for number, letter in my_list:
        print(letter)

# code version for calculation the percentage of the letter:
    
def most_frequent_percentage(text):
    
    my_dict = {}
    my_list = []
    
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            if letter not in my_dict:
                my_dict[letter] = 1
            else:
                my_dict[letter] += 1

    for key, value in my_dict.items():
         my_list.append((value, key))

    my_list.sort(reverse = True)

    my_sum = 0
    for number, letter in  my_list:
        my_sum += number
    
    for number, letter in  my_list:
        if len(text) <= 20:
            print(letter,'is {:05.2f}% of'.format((number/my_sum)*100), text)
        else:
            print(letter,'is {:05.2f}% of'.format((number/my_sum)*100), text[:20],'...')