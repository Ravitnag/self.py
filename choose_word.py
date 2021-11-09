def choose_word (file_path, index):
    words_open_file = open (file_path, 'r')
    words_file = words_open_file.read().split()
    unique = []
    count = 0; 
    for word in words_file:
        if word not in unique:
         unique.append(word)
         count+=1
    return (count, words_file[(index-1) % len(words_file)]);
