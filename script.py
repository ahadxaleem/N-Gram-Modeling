import os
import re

#returns tokenized strings
def tokenize(f):
    x=f.read()
    tokens=re.split(r"[\.\n\?\!]\s+",x)
    return tokens

#returns N-grams
def Ngram(n,sent):
    n_grams={}
    x=sent.split(" ")
    #storing N-grams in a dictionary
    for i in range(len(x)):
        temp=[]
        j=0
        while j<n and i-j>=0:
            if(j>1):
                temp[1]=x[i-j]+" "+temp[1]
                j+=1
            elif(j>0):
                temp.append(x[i-j]+" "+temp[0])
                j+=1
            else:
                temp.append(x[i-j])
                j+=1
            
        n_grams[i]=temp
    return n_grams

#calculating sentence probability
def sentenceProb(sent):
    #to keep track of no. of occurence of unique words
    word_count={}
    #total no of words
    no_of_words=0
    bigrams=Ngram(2,sent)
    #traversing directories and files
    parentdir="E:\myfiles"
    for i in range(10):
        folname="fol"+str(i)
        folpath = os.path.join(parentdir, folname)
        for j in range(50):
            subfilename="file"+str(j)+".txt"
            filepath = os.path.join(folpath, subfilename)
            subf=open(filepath,"r", encoding='utf-8')
            temp=subf.read()
            file_words=temp.split(" ")
            #calculating count of words
            for k in file_words:
                if k not in word_count.keys():
                    word_count[k]=1
                    no_of_words+=1
                else:
                    word_count[k]+=1
                    no_of_words+=1
            #calculating biagram count
            for m in range(1,len(bigrams)):
                bigram_count=re.findall( bigrams[m][1], temp)
                if bigrams[m][1] not in word_count.keys():
                    word_count[bigrams[m][1]]=len(bigram_count)
                else:
                    word_count[bigrams[m][1]]+=len(bigram_count)
                
    # print(word_count)
    probability=1
    # print(bigrams)
    if bigrams[0][0] in word_count.keys():
        probability=word_count[bigrams[0][0]]/no_of_words
    else:
        probability=0
    for l in range(1,len(bigrams)):
        temp1=bigrams[l][1].split(" ")
        probability*=(word_count[bigrams[l][1]]/word_count[temp1[0]])
    return probability

#calculating probabilty using laplace smoothing
def smoothSentenceProb(sent):
    #to keep track of no. of occurence of unique words
    word_count={}
    #to keep track of no. of occurence of bigram strings
    bigram_freq={}
    #total no of words
    no_of_words=0
    bigrams=Ngram(2,sent)
    #traversing directories and files
    parentdir="E:\myfiles"
    for i in range(10):
        folname="fol"+str(i)
        folpath = os.path.join(parentdir, folname)
        for j in range(50):
            subfilename="file"+str(j)+".txt"
            filepath = os.path.join(folpath, subfilename)
            subf=open(filepath,"r", encoding='utf-8')
            temp=subf.read()
            file_words=temp.split(" ")
            #calculating count of words
            for k in file_words:
                if k not in word_count.keys():
                    word_count[k]=1
                    no_of_words+=1
                else:
                    word_count[k]+=1
                    no_of_words+=1
            #calculating biagram count
            for m in range(1,len(bigrams)):
                bigram_count=re.findall( bigrams[m][1], temp)
                if bigrams[m][1] not in bigram_freq.keys():
                    bigram_freq[bigrams[m][1]]=len(bigram_count)
                else:
                    bigram_freq[bigrams[m][1]]+=len(bigram_count)
                
    # print(word_count)
    probability=1
    # print(bigrams)
    if bigrams[0][0] in word_count.keys():
        probability=word_count[bigrams[0][0]]/no_of_words
    else:
        probability=0
    for l in range(1,len(bigrams)):
        temp1=bigrams[l][1].split(" ")
        probability*=((bigram_freq[bigrams[l][1]]+1)/(word_count[temp1[0]]+len(word_count)))
    return probability

def perplexity(sent):
    x=sent.split(" ")
    temp=1/len(x)
    prob=1/sentenceProb(sent)
    perplexity=pow(prob,temp)
    return perplexity

s="Traditionally, faith, in addition to reason, has been considered a source of religious beliefs"
# print(Ngram(3,s))
print(sentenceProb(s))
print(smoothSentenceProb(s))
print(perplexity(s))


