import re
import os

def punctuation(text):
    """change all parentheses to to japanese characters"""
    text = re.sub(r'\(', '（', text, flags=re.DOTALL)  # replace EN L paren w/JP L paren
    text = re.sub(r'\)', '）', text, flags=re.DOTALL)  # replace EN R paren w/JP R paren
    return text

article_text = []
article_folders = os.listdir('./texts/')

for folder in article_folders:
    shortpath = './texts/' + folder
    longpath = '/INSERT/FULL/PATH/HERE/texts/' + folder + '/'
    # filename = 'wikiclean' + folder + '.txt'
    for fn in os.listdir(shortpath):
        try:
            wikitext = open(os.path.join(longpath, fn), 'r').read()
        except Exception as inst:
            print(fn)
            print(type(inst))   # the exception instance
            print(inst.args)    # arguments stored in .args
            print(inst)

        wikitext = punctuation(wikitext)
        wikitext = re.sub(r'<doc.*?title=.*?:.*?>([\s\S]*?)</doc>', '', wikitext)   # (1) remove category/wikipedia/image entries
        wikitext = re.sub(r'<doc.*?>\n.*\n', '', wikitext)      # (2) remove opening doc tags and article title on following line
        wikitext = re.sub(r'<[ / ]?doc[ / ]?>', '', wikitext)   # (3) remove closing doc tags
        wikitext = re.sub(r'<[ / ]?br[ / ]?>', '', wikitext)    # (4) remove all variation of linebreaks
        wikitext = re.sub(r'[\(\uff08][^\(\uff08\)\uff09]*[\)\uff09]', '', wikitext) # (5) remove parentheticals
        wikitext = re.sub(r'<.*?>([\s\S]*?)</.*?>', '', wikitext)   # (6) remove other content between tags
        wikitext = re.sub(r'.+(?<![。！？])\n', '', wikitext)        # (7) remove all lines w/o ending punctuation

        article_text.append(wikitext)

# article_clean = open(filename, 'w')
article_clean = open('wikiclean_v2.txt', 'w')
for article in article_text:
    article_clean.write(article)
    article_clean.write("\n")
article_clean.close()