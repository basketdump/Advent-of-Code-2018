class Claim:
    def __init__(self, claim):
        tmp = self.parseClaim(claim)
        self.id = tmp[0]
        self.x = tmp[1] - 1
        self.y = tmp[2] - 1
        self.width = tmp[3]
        self.height = tmp[4]


    def parseClaim(self, claim):
        result = []
        tmp = ''

        for ch in claim:
            if '0' <= ch <= '9':
                tmp += ch
            elif tmp != '':
                result.append(int(tmp))
                tmp = ''
        
        result.append(tmp)
        return result
