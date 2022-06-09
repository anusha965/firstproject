d1={}
d2={}
def anagrams(str1,str2):
        if len(str1)!=len(str2):
                return False
        else:
                num=0
                for x in str1:
                        d1[num]=x
                        num+=1
                num=0
                for x in str2:
                        d2[num]=x
                        num+=1
                a=sorted(d1.values())
                b=sorted(d2.values())
                if a==b:
                        return True
                else:
                        return False
string1=input("Enter the string")
string2=input("Enter the string to find wheather it is anagram")
print(anagrams(string1,string2))
                
