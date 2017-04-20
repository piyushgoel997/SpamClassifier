import re
import nltk.stem as stem
import VocabList


def pre_processing(text):
    """
    :param text: text to be converted to lower case
    :return: text after pre processing
    """

    # Lower Case
    text = text.lower()

    # Handle numbers
    text = re.sub('[0-9]+', 'number', text)

    # Strip of any HTML Tags
    text = re.sub('<[^<>]+>', '', text)

    # Handle URLs
    text = re.sub('(http|https)://[^\s]*', 'httpaddr', text)

    # Handle Email Address
    text = re.sub('[^\s]+@[^\s]', 'emailaddr', text)

    # Handle $ sign
    text = re.sub('[$]+', 'dollar', text)

    # remove any non alphanumeric characters
    text = re.sub('[^a-zA-Z0-9\s]+', '', text)

    # remove extra spaces
    text = re.sub('(\s)+', ' ', text, re.M | re.X)

    # Stemming, also making a list of the text
    # text = ' '.join([stem.PorterStemmer().stem(word) for word in text.split(" ")])

    str = ""
    for word in text.split(" "):
        try:
            str += stem.PorterStemmer().stem(word) + " "
        except:
            print("error")

    return str


def get_word_indices(text, vocab_list):
    """
    :param vocab_list: vocab list
    :param text: text to be processed
    :return: word_indices: indices of words chosen
    """
    word_indices = []
    i = 0
    for word in text.split(" "):
        if word in vocab_list:
            word_indices += [vocab_list[word]]
            i += 1
    return word_indices


def process(email, vocab_list):
    """
    :param vocab_list: vocab list
    :param email: content of email to be processed
    :return: indices of selective words
    """
    email = pre_processing(email)
    return get_word_indices(email, vocab_list)

# print(process(r"""Subject: english snow words
#
# jonathan david bobaljik posted a message to vol . 5-1276 of this list in which he discusses the various yup ' ik words for snow that have been contributed by anthony woodbury . for the sake of comparison he has a list of 9 or 10 english words for snow and snow-like things . i thought it would be useful to find out whether each of these english words means _ primarily _ snow or whether the snow sense is derived , figurative , or otherwise secondary . i have consulted the various editions of the oxford english dictionary . my results are as follows : a . acceptable cases : 1 . snow : a good english word with a respectable pedigree . means primarily snow . 2 . sleet : also good . by the way , is there an eskimo term corresponding to this ? 3 . slush : also good . 4 . avalanche : this word seems to have referred to snow avalanches from the beginning . 5 . blizzard : the first edition of the oed says , " a modern word . . . . as applied to a 's now-squall , ' the word became general in the american newspapers during the severe winter of 1880-81 ; but according to the _ milwaukee republican _ = ff 4 march 1881 , it had been so applied in the _ northern vindicator _ ( esthersville , iowa ) between 1860 and 1870 . it was apparently in colloquial use in the west much earlier . . . " the latest edition of the oed has a citation from 1859 . * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * b . doubtful cases : 1 . cornice : this is really an architectural term , meaning the " crown " on a building . its use to refer to a type of snow formation is merely figurative . 2 . firn : this is certainly a very rare and specialized word . the oed marks it " not naturalized " ; its synonym _ n ' ev ' e _ is marked the same way . i would accept neither . 3 . drift : with the meaning 's now-drift ' this word is attested c . 1300 , ( " this castel . . quitter es pan snau drif [ t ] . " ) but it clearly has too many other related senses , such as " off-course movement of a boat " and " gist of what someone is saying . " drift is related to " to drive " . compare bobaljik 's discussion of yup ' ik _ natquik _ 'd rifting snow ' . 4 . flurry : this word means primarily ' gust ' or 's quall ' . washington irving is cited in 1836 talking about " flurries of snow " , but there are other cases of flurries of rain , birds . conclusion : not primarily a snow word . 5 . sinkhole : bobaljik rejects _ muruaneq _ 's oft , deep snow ' , offering " sinkhole " as roughly comparable ( and presumably also unacceptable ) . = 20 " sinkhole " is not in the oed . my understanding of a sinkhole is any depression in which liquid collects , especially in the ground . i do not think it has anything to do with snow per se . * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * c . special case : 1 . frost : i have left " frost " out of the english list , since it has more to do with frozen dew and ice than with snow . i have also omitted " rime " and " hoarfrost " ( " hoar " is figurative for old age ) . accordingly , i urge that words for frost be omitted from the eskimo lists . * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * d . conclusion : my count is 5 good english words whose primary meanings are snow or forms of snow . bobaljik also allows only 5 " exclusively snow-related simple roots " in yup ' ik ( excluding " frost " as explained above ) . i am not a specialist in english etymology , but i am experienced at using the oed . is _ muruaneq _ 's oft , deep snow ' really not a purely snow word , as bobaljik says ? i would also like to know what " eskimo " languages there are other than yup ' ik for which snow-words are recorded in detail . david prager branner , yuen ren society asian l&l , do-21 , university of washington seattle , wa 98195 = 09 = 09 = 09 = 09 < charmii @ u . washington . edu >
# """, VocabList.get_vocab_list()))


