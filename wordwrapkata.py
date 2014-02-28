def wrap(text, num):
  
  if len(text) <= num:
    return text
  elif text[num-1] == ' ':
    return text[:num].rstrip() + '\r\n' + wrap(text[num:], num)
  elif text[:num].find(' ') > -1:
    rightSpaceIdx = text.rfind(' ')
    return text[:rightSpaceIdx] + '\r\n' + wrap(text[rightSpaceIdx:].lstrip(' '), num)
  else:
    return text[:num] + '\r\n' + wrap(text[num:].lstrip(), num)
  

