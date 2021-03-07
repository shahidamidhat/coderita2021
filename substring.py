#Given a string S. The task is to count the number of substrings which contains equal number of lowercase and uppercase letters.
def countSubstring(self, S): 
        #code here
        count=0
        for i in range(len(S)):
            c=0;
            for j in range(i,len(S)):
                if(ord(S[j])>=ord("a"))and(ord(S[j])<=ord("z")):
                    c+=1
                else:
                    c-=1
                if c==0:
                    count+=1
        return count
