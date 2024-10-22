

L=int(input("how long is the area you are putting turf in, in feet? "))
W=int(input("how wide? "))
cost=int(input("What is the ft^2 cost? "))

print("The area is", L*W,"square feet.")
print("The perimeter is", L+W+W+L, "feet around.")
print("The cost to put the turf down is", cost*L*W, "dollars.")
