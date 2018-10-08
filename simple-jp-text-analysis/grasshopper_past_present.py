import MeCab, re                                                    # regex library (for finding tense)

# load MeCab and the mecab-ipadic-neologd dictionary
# https://github.com/neologd/mecab-ipadic-neologd
# mct = MeCab.Tagger("-O chasen -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd")
mct = MeCab.Tagger("-O chasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/")

gh_text = open('grasshopper.txt', 'r').read()                       # open text file and read it into gh_text

# split text into sentences on '。' character, and then replace the ending '。' on all sentences
gh_lines = gh_text.split('。')
gh_lines = [x + '。' for x in gh_lines if len(x) > 0]

past = set()                                                        # create an empty set for past-tense lines

for sentence in gh_lines:                                           # loop through sentences in gh_lines
    jparse_bug = mct.parse(sentence)
    jparse = mct.parseToNode(sentence)

    while jparse:                                                   # while there are word-tokens in a sentence
        if jparse.posid == 25:                                      # catches verb conjugations
            # in this case, past-tense conj. have 'た'
            if jparse.surface == 'た':
                past.add(sentence)                                  # if 'た' was found, add to past-tense set
        jparse = jparse.next                                        # move to the next word-token

present = set(gh_lines) - past                                      # remove lines found in past from gh_lines

print("Grasshopper and the Ant sentences in present-tense:")
[print(x) for x in present]                                         # "for every x in present, print x"
print("\nGrasshopper and the Ant sentences in past-tense:")
[print(x) for x in past]                                            # "for every x in past, print x"

new_present = []                                                    # empty list for our past-tense-to-present

# change all of the sentences in past-tense, to present-tense
for past_sentence in list(past):
    # change negative-past to negative, and postive-past to present
    now_present = re.sub('ませんでした', 'ません', past_sentence)
    now_present = re.sub('した', 'す', past_sentence)
    new_present.append(now_present)                                 # add to list of new_present sentences

print("\nGrasshopper and the Ant sentences, past-to-present:")
[print(x) for x in new_present]                                     # "for every x in new_present, print x"