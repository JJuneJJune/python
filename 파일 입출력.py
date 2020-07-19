myFile = open("word.hwp", "w")
while True:
    msg = input("기록할 문장을 입력하세요: ")
    if msg == "" :
        break
    else:
        myFile.write(msg + "\n")
myFile.close()
