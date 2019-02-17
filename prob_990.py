class Solution:#union&find
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        tmp={chr(i):chr(i) for i in range(97,124)}
        def find(x):#search for the root
            if x!=tmp[x]:#if not the root
                tmp[x]=find(tmp[x])#then recursive to the root
            return tmp[x]
        
        for it in equations:
            if it[1]=='=':
                tmp[find(it[-1])]=find(it[0])#union
        
        for it in equations:
            if it[1]=='!':
                if tmp[find(it[-1])]==find(it[0]):
                    return False
        return True
