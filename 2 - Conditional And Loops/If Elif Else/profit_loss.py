# If cost price and selling price of an item is input through the keyboard, write a program to determine whether the seller has made profit or incurred loss or no profit no loss. Also determine how much profit he made or loss he incurred.

cp = int(input(("Enter Cost Price:")))
sp = int(input(("Enter Selling Price:")))

profit = sp-cp
loss = cp-sp

if sp>cp:
    print("Profit")
    print("Your Profit:", profit, "INR")
elif sp<cp:
    print("Loss")
    print("Your Loss:", loss, "INR")
else:
    print("NO LOSS, NO PROFIT")