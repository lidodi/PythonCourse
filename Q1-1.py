def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    l = len(word)
    if l<6:
        return False
    for i in range(0,l-5):
        window= word[i:i+6]
        flag1=window[0]==window[1]
        flag2=window[2] == window[3]
        flag3=window[4] == window[5]
        if flag1 & flag2 & flag3:
            return True
    return False

word2 = 'aabbcc67gg'
word1='aabbcc'
word='abccddee0123'
word3='llkkbmm'
word4='aaaazz'
word5='bbcCdd'
word6=''
istrifeca = trifeca(word1)