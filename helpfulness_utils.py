def read_glove_vectors(glove_file_name):
    with open(glove_file_name, 'r') as f:
        words = set()
        word_to_vector_map = {}
        for line in f:
            line = line.strip().split()
            current_word = line[0]
            words.add(current_word)
            word_to_vector_map[current_word] = np.array(line[1:], dtype=np.float64)
        
        i = 1
        words_to_index = {}
        index_to_words = {}
        for word in sorted(words):
            words_to_index[word] = i
            index_to_words[i] = word
            i = i + 1
    return words_to_index, index_to_words, word_to_vector_map

