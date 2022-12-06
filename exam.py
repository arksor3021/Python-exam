"""
小学校1年生で習う「いくつといくつ」の単元

「14 は 7 と いくつ？」みたいな
"""

import random

for  i in range(5):
  # 2から20までの乱数を出す
  num = random.randint(2,20)
  # 1からnumより1小さい数の中で乱数をだす
  x = random.randint(1, num-1 )

  print(str(num) + "は" + str(x) + "といくつにわけられますか?")
  ans = int(input())

  count = 0

  while ans != (num - x):
      print("もういちど")
      ans = int(input())
      # 間違えたら1増やす
      count+=1
  else:
    # 一回で解けたら
    if count == 0:
      print("カンペキ!\n")
    else:
      # 一度でも間違えたら
      print("せいかい!\n")


print("(* ´꒳`)ﾉよくできました♪")
    

