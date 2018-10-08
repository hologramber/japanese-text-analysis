start_at_sentence = 1000
end_at_sentence = 5000

with open('wikiclean-sentences.txt') as f:
    sentences = f.readlines()

print(len(sentences))
article_sample = open('wikiclean-sample.txt', 'w')
for sentence in sentences[start_at_sentence:end_at_sentence]:
    article_sample.write(sentence)

article_sample.close()
