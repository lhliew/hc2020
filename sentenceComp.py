written_orig = "hello today we are a the corn exchange in Cambridge"
spoken_orig = "hello today we are um at the um ar conn exchange Cambridge"

written_orig = written_orig.split()
spoken_orig = spoken_orig.split()

written_after_removals = []
spoken_after_removals = []

print ("Written: ", written_orig)
print ("Spoken: ", spoken_orig)


pos_in_spoken = []
words_not_recognised = []
words_extra = []


for word in written_orig:
    if (word in spoken_orig):
        written_after_removals.append(word)
    else:
        words_not_recognised.append(word)

for word in spoken_orig:
    if (word in written_orig):
        spoken_after_removals.append(word)
    else:
        words_extra.append(word)


print(" ")
print ("Written: ", written_after_removals)
print ("Spoken: ", spoken_after_removals)

print(" ")
print(words_not_recognised)
print(words_extra)

written_orig = written_after_removals
spoken_orig = spoken_after_removals

matches = 0
for i in range(len(written_orig)):
    if (written_orig[i] == spoken_orig[i]):
        matches += 1
        print("Match: ", written_orig[i])
    else:
        print("--> No match: ", written_orig[i], " : ", spoken_orig[i])

match_percentage = ((matches/((len(written_orig)+len(spoken_orig)/2))) * 100)

print('Percentage match: %d%%' % (match_percentage))