# HTML Parser - Part 2

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  def handle_comment(self, data):
    lines = data.split("\n")
    if len(lines) > 1:
      print(">>> Multi-line Comment")
      for line in lines:
        print(line)
    else:
      print(">>> Single-line Comment")
      print(*lines)
      
  def handle_data(self, data):
    if data != '\n':
      print(">>> Data")
      print(data)


html = ""       
for i in range(int(input())):
  html += input().rstrip()
  html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
