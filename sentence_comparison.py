import string


def preprocessing(sentence):
    # removes apostrophies and fullstops and makes all lower case
    sentence = sentence.replace("'", "")
    sentence = sentence.replace(",", "")
    sentence = sentence.replace("-", " ")
    sentence = sentence.replace(".", "").lower()

    return sentence

def word_removal(sentence1, sentence2):
    # Removes words from sentence1 which do not appear in sentence2 and adds removed words to [removed]
    # output = ((sentence1 with words removed), (words removed))
    # print("WORD REMOVAL: from ", sentence1)
    sentence1_after_removals = []
    removed = []

    for word in sentence1:
        if (word in sentence2):
            sentence1_after_removals.append(word)
            # print("not removed :", word)
        else:
            removed.append(word)
            # print("removed ", word)
    return (sentence1_after_removals, removed)

def sentence_comp(sentence1, sentence2):
    # checks words of sentence1 against sentence2 in order
    # will take in sentences after word_removal
    # output = ((number of matches), (words matched), (words not matched from sentence1))
    matches = 0
    words_matched = []
    words_not_matched = []
    offset = 0

    for i in range(len(sentence1)):
        try:
            if (sentence1[i] == sentence2[i+offset]):
                words_matched.append(sentence1[i])
                matches += 1
                # print("m : ", i)
            elif (sentence1[i] == sentence2[i+offset-1]):
                words_matched.append(sentence1[i])
                matches += 1
                offset -=1
                # print("m-1 : ", i)
            elif (sentence1[i] == sentence2[i+offset-2]):
                words_matched.append(sentence1[i])
                matches += 1
                offset -=2
                # print("m-2 : ", i)
            elif (sentence1[i] == sentence2[i+offset-3]):
                words_matched.append(sentence1[i])
                matches += 1
                offset -=3
                # print("m-3 : ", i)
            elif (sentence1[i] == sentence2[i+offset+1]):
                words_matched.append(sentence1[i])
                matches += 1
                offset +=1
                # print("m+1 : ", i)
            elif (sentence1[i] == sentence2[i+offset+2]):
                words_matched.append(sentence1[i])
                matches += 1
                offset +=2
                # print("m+2 : ", i)
            elif (sentence1[i] == sentence2[i+offset+3]):
                words_matched.append(sentence1[i])
                matches += 1
                offset +=3
                # print("m+3 : ", i)
            else:
                words_not_matched.append(sentence1[i])
                print(words_not_matched)
                # print("not_matched : ", i)
        except:
            # print("passed :", i)
            pass
        # print(offset)
    return(matches, words_matched, words_not_matched)

def comparison(written, spoken):
    written = preprocessing(written).split()
    spoken = preprocessing(spoken).split()
    written_after_removals, words_not_spoken = word_removal(written, spoken)
    spoken_after_removals, extra_words = word_removal(spoken, written)
    matches, words_matched, words_not_matched = sentence_comp(written_after_removals, spoken_after_removals)

    match_percentage = (((matches/((len(written)+len(spoken))/2))) * 100)

    # print("written:   ", written)
    # print("spoken:   ", spoken)
    # print("written_after_removals:   ", written_after_removals)
    # print("spoken_after_removals:   ", spoken_after_removals)
    # print("matches:   ", matches)
    # print("words_matched:   ", words_matched)
    # print("words_not_spoken:   ", words_not_spoken)
    # print("words_not_matched:   ", words_not_matched)


    return (match_percentage, words_matched)

# written_og = "hello today we are a the corn exchange in Cambridge"
# spoken_og = "hello today we are um at the um ar conn exchange Cambridge"

# written_og = "Parts of Australia's east coast have been hit by heavy rain and thunderstorms, dousing some bushfires but also bringing the threat of flooding. Some, such as this thirsty koala, have been making the most of the wet conditions."
# spoken_og = "Australia east Coast have been hit by heavy rain and thunderstorms losing some bushfires by also bringing the Threat of flooding have been making the most of these conditions"

# print(comparison(written_og, spoken_og))
