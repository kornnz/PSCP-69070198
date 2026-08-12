"""Color"""
c1 = input().lower()
c2 = input().lower()

if (c1 == "red" and c2 == "yellow") or (c1 == "yellow" and c2 == "red") :
    print("Orange")
elif (c1 == "red" and c2 == "blue") or (c1 == "blue" and c2 == "red"):
    print("Violet")
elif (c1 == "yellow" and c2 == "blue") or (c1 == "blue" and c2 == "yellow"):
    print("Green")
elif c1 == c2 and c1 in ("red", "yellow", "blue"):
    print(f"{c1[0].upper()}{c1[1::]}")
else:
    print("Error")
