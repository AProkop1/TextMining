import re


def clean_text(input: str) -> str:
    # get emoticons
    emoticons = re.findall('[:;][^\s]+', input)
    # clean text
    no_emoticons = re.sub('[:;][^\s]+', '', input)
    no_emoticons.lower()
    no_digits = re.sub('\d', '', no_emoticons)
    no_html = re.sub('\<.{1,9}>',  ' ',    no_digits)
    no_punctuation = re.sub('[^\w\s]',  ' ',    no_html)
    no_extra_whitespaces = re.sub(' +', ' ', no_punctuation)
    # add emoticons
    for e in emoticons:
        no_extra_whitespaces += e
    return no_extra_whitespaces

