import nose
from ocrkata import OCRParser

def testShouldParse1():
  num = "   \n" + \
        "  |\n" + \
        "  |\n" + \
        "   "
  
  parser = OCRParser()

  assert 1==parser.parse(num), '1 did not parse'

def testShouldParse2():
  num = " _ \n" +\
        " _|\n" +\
        "|_ \n" +\
        "   "

  parser = OCRParser()
  assert 2 == parser.parse(num), "2 did not parse"

def testShouldParse3():
  num = " _ \n" +\
        " _|\n" +\
        " _|\n" +\
        "   "

  parser = OCRParser()
  print parser.parse(num)
  assert 3 == parser.parse(num), "3 did not parse"

def testShouldParse4():
  num = "   \n" +\
        "|_|\n" +\
        "  |\n" +\
        "   "

  parser = OCRParser()

  assert 4 == parser.parse(num), "4 did not parse"

def testShouldParse5():
  num = " _ \n" +\
        "|_ \n" +\
        " _|\n" +\
        "   "

  parser = OCRParser()

  print parser.parse(num)
  assert 5 == parser.parse(num), "5 did not parse"

def testShouldParse6():
  num = ' _ \n' +\
        '|_ \n' +\
        '|_|\n' +\
        '   '
  parser = OCRParser()

  print parser.parse(num)
  assert 6 == parser.parse(num), '6 did not parse'

def testShouldParse7():
  num = ' _ \n' +\
        '  |\n' +\
        '  |\n' +\
        '   '

  parser = OCRParser()
  print parser.parse(num)

  assert 7 == parser.parse(num), '7 did not parse'

def testShouldParse8():
  num = ' _ \n' +\
        '|_|\n' +\
        '|_|\n' +\
        '   '

  parser = OCRParser()
  print parser.parse(num)

  assert 8 == parser.parse(num), '8 did not parse'

def testShouldParse9():
  num = ' _ \n' +\
        '|_|\n' +\
        ' _|\n' +\
        '   '

  parser = OCRParser()
  print parser.parse(num)

  assert 9 == parser.parse(num), '9 did not parse'

def testShouldParseZeroes():

  num = ' _  _  _  _  _  _  _  _  _ \n' +\
        '| || || || || || || || || |\n' +\
        '|_||_||_||_||_||_||_||_||_|\n' +\
        '                           '

 
  parser = OCRParser()
  print parser.parseAccountNumber(num)

  assert parser.parseAccountNumber(num) == '000000000', 'zeroes failed'

