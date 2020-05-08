def prt1():
  print("I'm NiceBoy!")

def prt2():
  print("I'm Goodboy!")

# 단위 실행(독립적으로 파일 실행)
# 위에 만든 함수가 잘돌아가는지 아 파일안에서만 실행해봄
if __name__ == "__main__":
  print("This is", dir())
  prt1()
  prt2()