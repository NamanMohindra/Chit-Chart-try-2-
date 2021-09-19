import nltk

#nltk.download('stopwords') # for the stopwords
#nltk.download('punkt') # for the stemmers I think
import regex
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from time import time
from collections import deque

class Token_List:
    def __init__(self):
        self.right = None
        self.left = None
        self.length = 0

    def __str__(self):
        ret = ""
        start = self.left
        while start != None:
            ret += start.user + str(start.words) + " | "
            start = start.prev
        return ret

    def append(self, token):
        if self.length > 0:
            self.right.prev = token
            token.next = self.right
            self.right = token
        else:
            self.right = token
            self.left = token
            self.length += 1

    def popleft(self):
        ret = None
        if self.length > 1:
            ret = self.left
            self.left.prev.next = None
            self.left = self.left.prev
            self.length -= 1
            return ret
        elif self.length == 1:
            ret = self.left
            self.left = None
            self.right = None
            self.length -= 1
            return ret
        else:
            return None

    def remove_ref(self, token):
        if token.next != None:
            token.next.prev = token.prev
        else:
            self.left = token.prev
        if token.prev != None:
            token.prev.next = token.next
        else:
            self.right = token.next
        token.next = None
        token.prev = None
        self.length -= 1

class Token:
    def __init__(self, wordList, user, next=None, prev=None):
        self.words = wordList
        self.tstamp = time()
        self.user = user
        self.next, self.prev = next, prev

class Chat_processor:
    def __init__(self, maxToken=10, manageDuplicateUsers=False, manageDuplicateWords=True):
        self.stop_words = set(stopwords.words('english'))
        more_stop = {',', '.', '!', '?', '(', ')', ':', ';', '~', '@', '*', '%', '$', '#', '+', '-'}
        self.stop_words = self.stop_words.union(more_stop)
        self.fdist = FreqDist()
        self.stemmer = SnowballStemmer("english")
        self.tokens = Token_List()
        self.maxToken = maxToken
        self.timestamp10 = time()
        self.count12 = [0.0]*12
        self.currCount = 0.0
        self._manageDuplicateUsers = manageDuplicateUsers
        self._manageDuplicateWords = manageDuplicateWords
        if self._manageDuplicateUsers:
            self.users = {}
        """
        for word in AI_tokens:
            fdist[word.lower()] += 1
        fdist.most_common(10)
        """

    def strip_stopwords(self, inStr, lowercase=True, stemmer=False):
        """
        Tokenizes the inStr, strips all stopwords, makes all words into lowercase if specified,
        and stemms all words if specified. Returns a list of words after the stripping process
        """
        tokens = word_tokenize(inStr)
        filtered_tokens = []
        for w in tokens:
            if w not in self.stop_words:
                filtered_tokens.append(w)
        if lowercase:
            for i in range(len(filtered_tokens)):
                filtered_tokens[i] = filtered_tokens[i].lower()
        if stemmer:
            for i in range(len(filtered_tokens)):
                filtered_tokens[i] = self.stemmer.stem(filtered_tokens[i])
        if self._manageDuplicateWords:
            s = set()
            for word in filtered_tokens:
                s.add(word)
            filtered_tokens = []
            for word in s:
                filtered_tokens.append(word)
        return filtered_tokens

    def update_counter(self):
        timepassed = time() - self.timestamp10
        if timepassed < 10:
            self.currCount += 1
            self.count12[11] = float(self.currCount) + float(self.count12[10])*(10-timepassed)/10.0
        else:
            shift = int(timepassed//10)
            self.timestamp10 += 10.0 * shift
            self.count12[11] = self.currCount
            for i in range(12):
                if i - shift >= 0:
                    self.count12[i - shift] = self.count12[i]
            for i in range(shift):
                self.count12[11-i] = 0.0
            self.currCount = 1
            self.count12[11] = self.currCount + self.count12[10]*(10-max(timepassed, 10))/10.0

    def process_string(self, inStr, user):
        '''
        inStr - the message
        user - username
        '''
        self.update_counter()
        words = self.strip_stopwords(inStr)
        token = Token(words, user)
        if self._manageDuplicateUsers:
            if user not in self.users.keys():
                self.tokens.append(token)
                self.users[user] = token
                for word in words:
                    self.fdist[word] += 1
            else:
                old_token = self.users[user]
                self.tokens.remove_ref(old_token)
                for word in old_token.words:
                    self.fdist[word] -= 1
                for word in words:
                    self.fdist[word] += 1
                self.users[user] = token
                self.tokens.append(token)
        else:
            self.tokens.append(token)
            for word in words:
                self.fdist[word] += 1
        if self.tokens.length > self.maxToken:
            removed = self.tokens.popleft()
            for word in removed.words:
                self.fdist[word] -= 1

    def getCommon(self, mostCommon=6):
        '''
        Return the list of most commong tupples

        '''
        return self.fdist.most_common(mostCommon)

    def get_CPM(self):
        ret = [0]*12
        for i in range(12):
            ret[i] = self.count12[i]*6//1
        return ret

    def command(self, num):
        """
        num == 0 will cause a reset
        """
        if num == 0:
            if self._manageDuplicateUsers:
                self.users = {}
            self.fdist = FreqDist()
            self.tokens = Token_List()

class Tester:
    def __init__(self):
        self.chat_processor = Chat_processor(maxToken=5, manageDuplicateUsers=False, manageDuplicateWords=False)
        self.ex0 = total[0]

    def test(self):
        dic = self.chat_processor.fdist
        for lst in small:
            self.chat_processor.process_string(lst[0], lst[1])
            for key in dic:
                print(key, dic[key])
            print(self.chat_processor.tokens.length)
            print(self.chat_processor.tokens)
            print(self.chat_processor.getCommon(5))
            print('\n\n')

def main():
    #    tester = Tester()
    #    tester.test()
    #    print(tester.chat_processor.fdist.keys())
    pass

if __name__ == "__main__":
    main()
