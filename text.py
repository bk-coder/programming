a = int(input())
x = a
rev = 0
while(x > 0):
	last = x % 10
	rev = rev*10 + last
	x = x//10
 
if(rev == a):
	print("Palindrome")
else:
	print("Not a palindrome")