#any prefect solution are you know please send the mail to that message

class Solution(object):
    def prefixCount(self, words, pref):
        count = 0
        temp = None
        for i in range(len(words)):
            temp = words[i]
            if pref == temp[:len(pref)]:
                count+=1 
        return count
