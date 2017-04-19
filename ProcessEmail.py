import re
import nltk.stem as stem


def pre_processing(text):
    """
    :param text: text to be converted to lower case
    :return: text after pre processing
    """

    # remove extra spaces
    text = re.sub('(\s)+', ' ', text, re.M | re.X)

    # Lower Case
    text = text.lower()

    # Handle numbers
    text = re.sub('[0-9]+', 'number', text)

    # Strip of any HTML Tags
    text = re.sub('<[^<>]+>', ' ', text)

    # Handle URLs
    text = re.sub('(http|https)://[^\s]', 'httplink', text)

    # Handle Email Address
    text = re.sub('[^\s]+@[^\s]', 'emailadd', text)

    # Handle $ sign
    text = re.sub('[$]+', 'dollarsign', text)

    # remove any non alphanumeric characters
    text = re.sub('[^a-zA-Z0-9\s]+', '', text)

    # Stemming, also making a list of the text
    text = ' '.join([stem.PorterStemmer().stem(word) for word in text.split(" ")])

    return text


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
            word_indices[i] = vocab_list[word]
            i += 1
    return word_indices


def processing(email, vocab_list):
    """
    :param vocab_list: vocab list
    :param email: email to be processed
    :return: indices of selective words
    """
    email = pre_processing(email)
    return get_word_indices(email, vocab_list)

print(pre_processing(r"""Subject: forensic linguistics conference international

 association of forensic linguists second international conference to be held at mary white college , university of new england armidale , new south wales , australia from 9-12 july 1995 . call for abstracts papers are called for from members of the international association of forensic linguists and others whose work involves them in any of iafl 's aims , or more broadly in any areas of language and the law . ( if you need more info about iafl 's aims contact one of the people listed towards the end of this message . ) members are keen to communicate with professionals and scholars in related disciplines who also work on aspects of language and the law . prospective paper-givers are invited to submit a half-page abstract , along with a brief biography that includes professional background and interests . deadline for submission of abstracts is february 3rd 1995 send abstracts to : diana eades , iafl conference co - ordinator , linguistics dept , university of new england , armidale nsw 2351 , australia email : deades @ metz . une . edu . au registration information registration fee : member $ a125 non - member $ a150 student $ a100 early bird discount $ a20 off if you register before april 12th 1995 . registration includes : * attendance at all sessions * abstracts booklet * morning and afternoon teas and lunches on monday tuesday and wednesday * reception on sunday evening * conference satchel * excursion to dangars falls registration below is the registration form . please do not email this form . you can print it out and send it by airmail to the address below ( or you can ask for a hardcopy by emailing diana eades ) registration form mr / mrs / ms / miss / dr / ass prof / prof ( please circle ) male / female ( please circle ) first name : surname : institution : address : suburb : state : postcode : country : email : tel : fax : accommodation please organise accommodation for me on the following nights : 8th [ ] 9th [ ] 10th [ ] 11th [ ] 12th [ ] 13th [ ] in mary white college ( $ a43 . 00 per night includes accommodation , breakfast and dinner ) off campus accommodation those staying off campus will need a vehicle to get to the conference venue . in caravan park ( accommodation only ) caravan $ a30 single $ a32 double fully self contained , heated ensuite cabin $ a44 single $ a46 double in motel ( approximate single or double accommodation only ) $ a60 per night $ a70 per night yes , i am interested in attending the pre-conference tour to dorrigo national park on sunday 9th july from 10 . 00am - 5 . 00pm at approximately $ a20 per person , and would have . . . . . . . . . . . person / s with me all registration forms must be received by 12th june 1995 ( early bird discount registration closes 12th april 1995 ) do not email this form . send it by airmail to the address below enclosed is a cheque / money order or charge my bankcard / mastercard ( delete one ) _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ expiry date : _ _ _ _ / _ _ _ _ name on card : _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ registration : $ . . . . . . . . . . . . . . . . . . . . . . accommodation : $ . . . . . . . . . . . . . . . . . . . . . . conference dinner $ . . . . . . . . . . . . . . . . . . . . . . earlybird discount : minus $ a20 ( if posting before 12th april ) total : $ please make cheques payable to university of new england . return completed registration form to : marketing executive , new england conference management , university of new england , armidale nsw 2351 we are unable to accept registration by email , send it by airmail please . further information for further information please contact the conference co-ordinator , diana eades , linguistics department , university of new england , tel : 61 67 73 3185 fax : 61 67 73 3735 email : deades @ metz . une . edu . au for administrative or accommodation enquiries , contact gabrielle aldridge at new england conference management , tel : 61 67 73 3370 fax : 61 67 71 1713 for further information about iafl and membership queries , contact diana eades ( address above ) or sue blackwell , school of english , university of birmingham , edgbaston , birmingham , b15 2tt , uk email : blackwellsa @ vms1 . bham . ac . uk or jeffrey kaplan , dept of linguistics , san diego state university , san diego , ca 92182 , usa . email : jkaplan @ sciences . sdsu . edu important dates abstracts due 3 feb notification of acceptance of abstracts 15th march earlybird registrations due 12th april registration deadline 12th june . hfraser @ metz . une . edu . au ( 129 . 180 . 4 . 1 ) helen fraser ( dr ) dept of linguistics university of new england armidale nsw 2351 australia phone 067 73 2128 / 3189 fax 067 73 3735"""))
