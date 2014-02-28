import nose
import wordwrapkata

def testShouldSplit():
  result = wordwrapkata.wrap("abc", 2)

  assert "ab\r\nc" == result, "did not split correctly"

def testShouldSplitTwice():
  result = wordwrapkata.wrap("abcde", 2)
  print result
  assert "ab\r\ncd\r\ne" == result, "Should Split Twice failed"

def testShouldNotWrapSmallLine():
  result = wordwrapkata.wrap("abc", 10)

  assert "abc" == result, "Wrapped when it shouldn't"

def testSplitOneWordManyTimes():
  result = wordwrapkata.wrap("abcdefghij", 3)

  assert "abc\r\ndef\r\nghi\r\nj" == result, "one word wrapped many times failed"

def testSplitTwoWords():
  result = wordwrapkata.wrap("word word", 5)

  assert "word\r\nword" == result, "Split Two Words Failed"

def testWrapAfterWordBoundary():
  result = wordwrapkata.wrap("word word", 6)
  print result
  assert "word\r\nword" == result, "Wrap after word boundary failed"

def testWrapWellBeforeWordBoundary():
  result = wordwrapkata.wrap("word word", 3)

  print result
  assert "wor\r\nd\r\nwor\r\nd" == result, "Wrap well before word boundary failed"

def testWrapWithTrimmedSpaceAfterWordBoundary():
  result = wordwrapkata.wrap("word word", 4)

  print result
  print len(result)
  assert "word\r\nword" == result, "Wrap with trimmed space failed"
