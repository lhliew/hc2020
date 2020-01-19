def word_removal(sentence1, sentence2):
    # Removes words from sentence1 which do not appear in sentence2 and adds removed words to [removed]
    # output = ((sentence1 with words removed), (words removed))
    
    sentence1_after_removals = []
    removed = []

    for word in sentence1:
        if (word in sentence2):
            sentence1_after_removals.append(word)
        else:
            removed.append(word)
    return (sentence1_after_removals, removed)

def sentence_comp(sentence1, sentence2):
    # checks words of sentence1 against sentence2 in order
    # will take in sentences after word_removal
    # output = ((number of matches), (words matched), (words not matched from sentence1))
    matches = 0
    words_matched = []
    words_not_matched = []

    for i in range(len(sentence1)):
        try:
            if (sentence1[i] == sentence2[i]):
                words_matched.append(sentence1[i])
                matches += 1
            else:
                words_not_matched.append(sentence1[i])
        except:
            pass
    return(matches, words_matched, words_not_matched)

def comparison(written, spoken):
    written = written.split()
    spoken = spoken.split()
    written_after_removals, words_not_spoken = word_removal(written, spoken)
    spoken_after_removals, extra_words = word_removal(spoken, written)
    matches, words_matched, words_not_matched = sentence_comp(written_after_removals, spoken_after_removals)
    
    match_percentage = (((matches/((len(written)+len(spoken))/2))) * 100)
    

    return match_percentage

written_orig = "hello today we are a the corn exchange in Cambridge"
spoken_orig = "hello today we are um at the um ar conn exchange Cambridge"

print(comparison(written_orig, spoken_orig))

