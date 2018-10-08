import re

def clean_text_check(text):
    """if there are no troublesome characters in the text, returns true (text is good)"""
    # \u2150—\u218F     fractions and roman numerals
    # \u2190—\u21FF     arrows (e.g. ←↑→↓↔↕)
    # \u2460-\u24FF     enclosed numbers (e.g. ②③④)
    # \u2500-\u257F     Box Drawing
    # \u25A0-\u26FF     shapes (e.g. ◉▶◩◿) and misc symbols (e.g. ♪)
    # \u3003-\u300B     〃〄々〆〇〈〉《》
    # \u300E-\u301B     『』【】〒〓〔〕〖〗〘〙〚〛
    # \u301D-\u303F     〝〞〟〠〡〢〣〤〥〦〧〨〩〪〭〮〯〫〬〰〱〲〳〴〵〶〷〸〹〺〻〼〽〾〿


    if len(text) > 4 and not re.search(r'@※＞＜ / ＝：:', text) and not re.search(r'[\u2150-\u218F\u2190-\u21FF\u2460-\u26FF\u3003-\u300B\u300E-\u301B\u301D-\u303F]', text) and not text.count('（') > 1 and not text.count('）') > 1 and not text.count('「') > 1 and not text.count('」') > 1:
        return 1    # returns true if good text
    else:
        return 0    # returns false if bad text


def no_brackets_check(text):
    """if there are no brackets or parentheses in the text, return true"""
    if not re.search(r'[】【《》「」｛｝＜＞『』（）〔〕［］]', text):
        return 1
    else:
        return 0


def punctuation(text):
    """change all irregular punctuation to japanese characters"""
    text = re.sub(r'\(', '（', text, flags=re.DOTALL)  # replace EN L paren w/JP L paren
    text = re.sub(r'\)', '）', text, flags=re.DOTALL)  # replace EN R paren w/JP R paren
    text = re.sub(r'\?', '？', text, flags=re.DOTALL)
    text = re.sub(r'!', '！', text, flags=re.DOTALL)
    text = re.sub(r'？！', '？', text, flags=re.DOTALL)
    text = re.sub(r'！？', '？', text, flags=re.DOTALL)
    return text


def remove_p_br_div(text):
    """remove br, p, and div open and close tags"""
    text = re.sub(r'<[ / ]?br[ / ]?>', '', text)       # removes <br> </br> <br/> <br /> </ br>
    text = re.sub(r'<[/]?p.*?>', '', text)             # removes <p ~> and </p>
    text = re.sub(r'<[/]?div.*?>', '', text)           # removes <div ~> and </div>
    return text
