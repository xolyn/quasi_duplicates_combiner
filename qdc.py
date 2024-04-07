def str_sim(str1, str2):
    if str1==str2:
        return 1 
    denom=max(len(str1),len(str2))
    numer=0
    extra=0
    for i in range(denom):
        try:
            if str1[i]==str2[i]:
                numer+=1
        except:
            if extra<=2:
                numer+=0.6
            elif extra>5:
                numer+=0.3
            else:
                numer+=0.1
            extra+=1
    return numer/denom

def quasi_dup_combiner(wordlist:list[str],alpha=0.8):
    wordlistf = []
    wordlist = sorted(wordlist)
    lastword=""
    for i in range(len(wordlist)):
        if str_sim(lastword,wordlist[i])<alpha:
            wordlistf.append(wordlist[i])
        lastword=wordlist[i]
    return wordlistf