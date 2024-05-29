words = input("Check word if it's a palindrome - ").strip().replace(" ", "").lower()
print(words)
print(words[::-1])
if words == words[::-1]:
    print("Yes, it is")
else:
    print("No, it isn't")