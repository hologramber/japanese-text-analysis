import MeCab
from collections import Counter                             # for counting most common elements

# load MeCab and the mecab-ipadic-neologd dictionary
# https://github.com/neologd/mecab-ipadic-neologd
# mct = MeCab.Tagger("-O chasen -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd")
mct = MeCab.Tagger("-O chasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/")

# simple recreation of previous MeCab command line tests; parse and tokenize sentence
print(mct.parse('今日はいい天気ですね。'))

gh_text = open('grasshopper.txt', 'r').read()               # open text file and read it into gh_text

# split text into sentences on '。' character, and then replace the ending '。' on all sentences
gh_lines = gh_text.split('。')
gh_lines = [x + '。' for x in gh_lines if len(x) > 0]

nouns = []                                                  # create empty lists for nouns, verbs, adjectives
verbs = []
adjectives = []

for sentence in gh_lines:                                   # loop through each sentence in gh_lines
    jparse_bug = mct.parse(sentence)
    jparse = mct.parseToNode(sentence)

    while jparse:
        mct_split = jparse.feature.split(',')               # split features up by commas
        if mct_split[0] == '名詞':
            nouns.append(jparse.surface)                    # if word is a noun, add the element to nouns
        elif mct_split[0] == '動詞':
            verbs.append(jparse.surface)                    # if word is a verb, add the element to verbs
        elif mct_split[0] == '形容詞':
            adjectives.append(jparse.surface)               # if word is an adj, add the element to adjectives
        jparse = jparse.next                                # move on to the next word-token

noun_counts = str(Counter(nouns).most_common(3))            # count the 3 most common nouns (and convert to string)
verb_counts = str(Counter(verbs).most_common(3))            # count the 3 most common verbs (and convert to string)
adjective_counts = str(Counter(adjectives).most_common(3))  # count the 3 most common adjectives (and convert to string)

print(noun_counts)                                          # print the 3 most comon nouns
print(adjective_counts)                                     # print the 3 most common adjectives
print(verb_counts)                                          # print the 3 most common verbs