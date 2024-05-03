# The Minion Game
def minion_game(string):
  vowels = ["A","E","I","O","U"]
  scoreStuart = 0
  scoreKevin = 0

  for i in range(len(string)):
    if string[i] in vowels:
      scoreKevin += len(string) - i
    else:
      scoreStuart += len(string) - i
      
  if scoreStuart > scoreKevin:
    print("Stuart", scoreStuart)
  elif scoreStuart < scoreKevin:
    print("Kevin", scoreKevin)
  else:
    print("Draw")
    
if __name__ == '__main__':
  s = input()
  minion_game(s)
