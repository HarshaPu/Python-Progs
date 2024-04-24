import webbrowser
while True:
    print("1:Whatsapp\n2:Instagram\n3:Facebook\n4:Quora\n5:Sleep")
    choice=int(input("enter your choice:"))
    if choice>0 and choice<=5:
        if choice==1:
            webbrowser.open("https://www.whatsapp.com/")
        if choice==2:
            webbrowser.open("https://www.instagram.com/")
        if choice==3:
            webbrowser.open("https://www.facebook.com/")
        if choice==4:
            webbrowser.open("https://www.quora.com/")
        if choice==5:
            break
    else:
        print("Invalid choice")