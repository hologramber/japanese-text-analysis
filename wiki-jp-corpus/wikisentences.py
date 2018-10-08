import re

keeplines = []

with open('wikiclean.txt') as f:
    wikitext = f.readlines()

article_dismiss = open('wikiclean-dismissed.txt', 'w')
article_sentences = open('wikiclean-sentences.txt', 'w')

text = ''

for line in wikitext:
    line = line.strip()
    if len(line) > 2 and not line.endswith('、') and '。' in line:
        text = line.split('。')
        text = list(filter(None, text))
        for sentence in text:
            sentence = sentence.strip()
            if (re.search('[,「」（）［］《》＜＞{}@&＆#＃※=＝+＋/／；;：:…]', sentence) # dismiss brackets, etc
                    or re.search('[a-zA-Z]', sentence)      # dismiss for any latin alphabet characters
                    or re.search('[\u2150-\u218F\u2190-\u21FF\u2460-\u26FF]', sentence) # shapes, icons, etc
                    or re.search('[\u3003-\u300B\u300E-\u301B\u301D-\u303F]', sentence) # shapes, icons, etc
                    or re.search('、{2,}', sentence)     # dismiss if more than 2 、in a row
                    or re.search('、。', sentence)        # dismiss if the pattern 、。 is found
                    or sentence.count('・') > 2          # dismiss if there are more than 2 dots
                    or sentence.endswith('、')           # dismiss if the line ends with 、
                    or len(sentence) > 150              # dismiss if the line is more than 150 chars
                    or len(sentence) < 3                # dismiss if the line is less than 3 chars
                    or not re.search('[\u3040-\u309F]+$', sentence)):   # dismiss if the line doesn't end w/kana
                article_dismiss.write(sentence)
                article_dismiss.write("\n")
            else:
                sentence = sentence + '。'
                sentence = sentence.replace(" ", "")
                article_sentences.write(sentence)
                article_sentences.write("\n")

article_dismiss.close()
article_sentences.close()
