with open("quotes.txt", "r",encoding = "utf-8") as f:
    for line in f:
        print(line)
a = input("Хто написав?")
with open("quotes.txt", "a",encoding = "utf-8") as f:
    f.write("\n "+a+" \n")
while 1:
    b = input("Напиши цитату:")
    if b == "stop":
        break
    else:
        q = input("цитата"):
        with open("quotes.txt", "a", encoding = "utf-8") with f:
        
        
        f.write("\n "+a+"\n")
