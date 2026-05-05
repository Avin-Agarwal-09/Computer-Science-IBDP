Colour = str(input("What colour is your favourite colour? "))
Number = int(input("Whats your lucky number? "))
if Colour == "green":
    if Number > 4 and Number < 7:
        print("in", Number, "years, you'll buy a ", Colour, "bicycle")
    else:
       print("I suppose you wanted a", Colour, "ball", Number, "years ago")
