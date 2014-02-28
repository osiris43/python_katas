class OCRParser(object):
  def parse(self, num):
    lines = num.split('\n')
   
    if lines[0] == '   ' and lines[1] == '|_|': 
      return 4
    elif lines[1] == '|_|' and lines[2] == '|_|':
      return 8
    elif lines[1] == '|_|':
      return 9
    elif lines[2] == '|_|' and lines[1] == '|_ ':
      return 6
    elif lines[2] == '|_|':
      return 0
    elif lines[0] == '   ':
      return 1
    elif lines[0] == ' _ ' and lines[1] == '|_ ':
      return 5
    elif lines[1] == ' _|' and lines[2] == '|_ ':
      return 2
    elif lines[2] == ' _|':
      return 3
    elif lines[0] == ' _ ':
      return 7

  def parseAccountNumber(self, num):
    lines = num.split('\n')
    
    acctNum = ''
    endings = [x for x in range(1, 28) if x % 3 == 0]
    for ending in endings:
      a = lines[0][ending-3:ending] + '\n'
      a += lines[1][ending-3:ending] + '\n'
      a += lines[2][ending-3:ending] + '\n'
      acctNum += str(self.parse(a))

    return acctNum
    
