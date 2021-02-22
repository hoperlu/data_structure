class KMP:
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]
        #'ababaca'
        for i in range(1, len(pattern)):
            j = ret[i - 1] #j=目前i的前一項的ref table的值, i.e. 當j!=0, pattern[0:j]==pattern[i-j:i]
            while j > 0 and pattern[j] != pattern[i]: 
                j = ret[j - 1]
                '''
                ret[i]如果要>1，就代表前面一定要有match, 否則ret[i]只能是0 or 1 
                p[0:j+1]和p[i-j:i+1]確定不match了，所以ret[i]一定<=j，因此我們從j-1開始找，
                
                '''
            ret.append(j + 1 if pattern[j] == pattern[i] else j)#來這就代表j==0 or p[i]==p[j], j==0時ret[i]只有可能是0 or 1
        return ret                      #p[i]==p[j]也不用再找了，因為前面j個都一樣，所以ret[i]=j+1
                                        
    def search(self, T, P):
        """ 
        KMP search main algorithm: String -> String -> [Int] 
        Return all the matching position of pattern string P in T
        """
        partial, ret, j = self.partial(P), [], 0
        
        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]: j += 1
            if j == len(P): 
                ret.append(i - (j - 1))
                j = partial[j - 1]
            
        return ret

a=KMP()
print(a.partial('ababaca'))