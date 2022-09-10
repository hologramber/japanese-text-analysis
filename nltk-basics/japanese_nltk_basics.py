import nltk
from nltk.corpus import jeita
from nltk.corpus import knbc

print("file identifiers in the jeita and knbc corpuses:")
print(jeita.fileids())
print(knbc.fileids())

print("first ten words in the JEITA corpus:")
print(jeita.words()[0:10])

print("first ten words with their part-of-speech tags in the JEITA corpus:")
print(jeita.tagged_words()[0:10])

print("functions available in the JEITA corpus:")
print(dir(jeita))

print("avg word length, avg sentence length, and lexical diversity for each fileid in JEITA:")
for fileid in jeita.fileids():
    num_chars = len(jeita.raw(fileid))
    num_words = len(jeita.words(fileid))
    num_sents = len(jeita.sents(fileid))
    num_vocab = len(set(w.lower() for w in jeita.words(fileid)))
    print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)

# load single fileid from the jeita corpus
jsingle_t = nltk.Text(jeita.words('a0010.chasen'))
print("total number of words/symbols/tokens: " + str(len(jsingle_t)))
print("unique words/symbols/tokens: " + str(len(set(jsingle_t))))
print("occurrences of 見る with context:")
print(jsingle_t.concordance("見る"))         #  every occurrence of a given word, together with some context
print("number of times 夜 appears: " + str(jsingle_t.count("夜")))

# display the location of a word in the text: this positional information can be displayed using a dispersion plot
# each stripe represents an instance of a word, and each row represents the entire text
jsingle_t.dispersion_plot(["見る", "地", "時間", "今", "高い"])

# the frequency distribution tells us the frequency of each vocabulary item in the text
fdist_j = nltk.FreqDist(jsingle_t)
print("50 most common words in a0010.chasen:")
print(fdist_j.most_common(50))

# for each word w in the vocabulary jsingle_t_set, check whether len(w) is greater than or equal to 3
jsingle_t_set = set(jsingle_t)
long_words = [w for w in jsingle_t_set if len(w) >= 3]
print("words in a0010.chasen with 3 or more characters:")
print(sorted(long_words))

# for each word w in jsingle_t, check if length is >= 3, and if it occurs >= 3 times in the text
print("words in a0010.chasen with 3 or more characters, that appear 3 or more times:")
print(sorted(w for w in set(jsingle_t) if len(w) >= 3 and fdist_j[w] >= 3))
print("words in a0010.chasen ending in しい:")
print(sorted(w for w in set(jsingle_t) if w.endswith('しい')))
print("words in a0010.chasen starting with 見:")
print(sorted(w for w in set(jsingle_t) if w.startswith('見')))
print("words in a0010.chasen which contain 山:")
print(sorted(w for w in set(jsingle_t) if '山' in w))
print("words in a0010.chasen which contain 上 or 下:")
print(sorted(w for w in set(jsingle_t) if '上' in w or '下' in w))

# create NLTK texts for each corpus in full
jfull_t = nltk.Text(jeita.words())
kfull_t = nltk.Text(knbc.words())

# the frequency distribution tells us the frequency of each vocabulary item in the text
fdist_jfull = nltk.FreqDist(jfull_t)
print("50 most common words in the full JEITA corpus:")
print(fdist_jfull.most_common(50))
fdist_kfull = nltk.FreqDist(kfull_t)
print("50 most common words in the full KNB corpus:")
print(fdist_kfull.most_common(50))

# a collocation is a sequence of words that occur together unusually often
print("collocations (words that occur together unusually often) in the JEITA corpus:")
print(jfull_t.collocations())
print("collocations (words that occur together unusually often) in the KNB corpus:")
print(kfull_t.collocations())

print("sentences w/context where token '人' appears in JEITA corpus:")
print(jfull_t.concordance("人"))
print("sentences w/context where token '人' appears in KNB corpus:")
print(kfull_t.concordance("人"))

print("words that appear in the same context (same words on either side) as '人' in JEITA:")
print(jfull_t.similar("人"))
print("words that appear in the same context (same words on either side) as '人' in KNB:")
print(kfull_t.similar("人"))
