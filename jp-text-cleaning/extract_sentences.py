from spring_clean import punctuation, clean_text_check

sentence_collection = []            # hold the new list of sentences

def split_on_exclaim(text):
    """splits on ！"""
    lines = text.split('！')             # split line wherever ！ is found
    lines = list(filter(None, lines))
    for line in lines:
        line = line.strip()             # remove whitespace
        if not line.endswith('。') and not line.endswith('！') and not line.endswith('？'):
            line = line + '！'           # split() removes the original character
            sentence_collection.append(line)
        else:
            sentence_collection.append(line)

def split_on_question(text):
    """splits on ？ and sends lines with ！ to split_on_exclaim"""
    lines = text.split('？')
    lines = list(filter(None, lines))
    for line in lines:
        line = line.strip()
        if not line.endswith('。') and not line.endswith('！') and not line.endswith('？'):
            line = line + '？'           # split() removes the original character
            if '！' in line:
                split_on_exclaim(line)
            else:
                sentence_collection.append(line)
        else:
            sentence_collection.append(line)

def split_to_sentences(text):
    """splits on 。 and sends lines with ？ or ！ to their own split functions"""
    lines = text.split('。')
    lines = list(filter(None, lines))
    for line in lines:
        line = line.strip()
        if not line.endswith('。') and not line.endswith('！') and not line.endswith('？'):
            line = line + '。'           # split() removes the original character
            if '？' in line:
                split_on_question(line)
            elif '！' in line:
                split_on_exclaim(line)
            else:
                sentence_collection.append(line)


with open('article_clean.txt') as f:
    paragraph = f.read()

sentences_clean = open("sentences_clean.txt", "w", encoding='utf-8')

paragraph = punctuation(paragraph)      # normalize punctuation
split_to_sentences(paragraph)           # split to sentences based on punctuation

for sentence in sentence_collection:
    if sentence.count('（') != sentence.count('）') or sentence.count('「') != sentence.count('」'):
        # bracket mismatches are dismissed
        pass
    else:
        if clean_text_check(sentence):          # check for weird characters and other dealbreakers
            sentences_clean.write(sentence)     # write to file
            sentences_clean.write("\n")         # write linebreak to file

sentences_clean.close()