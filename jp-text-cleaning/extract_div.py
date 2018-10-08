from bs4 import BeautifulSoup
import re

with open('article.html') as f:
    text = f.read()                             # read in the article.html file
soup = BeautifulSoup(text, 'html.parser')       # run text through BeautifulSoup

# .decompose() removes tags specified and the text between them
# .unwrap() also removes the tags, but leaves the text inside untouched
for h2 in soup("h2"):               # remove <h2></h2> tags and everything between them
    h2.decompose()
for rt in soup("rt"):               # <rt></rt> tags & text are furigana readings; remove these
    rt.decompose()
for ruby in soup("ruby"):           # remove <ruby></ruby> tags, but leave the text inside
    ruby.unwrap()

article = soup.find(id="newsarticle")           # the text I want is within the div w/id "newsarticle"
article = str(article).splitlines()             # convert to string
text = ''
for line in article:
    line = line.strip()                         # remove excess whitespace
    text = text + line                          # recombine text after removing whitespace

text = re.sub(r'<.*?>', '', text)                       # removes ALL HTML tags+attributes
# article = re.sub(r'<[ / ]?br[ / ]?>', '', article)    # removes <br> </br> <br/> <br /> </ br>
# article = re.sub(r'<[/]?p.*?>', '', article)          # removes <p ~> and </p>
# article = re.sub(r'<[/]?div.*?>', '', article)        # removes <div ~> and </div>

article_clean = open('article_clean.txt', 'w')
article_clean.write(text)
article_clean.close()
