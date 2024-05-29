responses = []
while True:
    try:
        response = input("Name: ")
        responses.append(response)
    except EOFError:
        print()
        break

if len(responses) == 1:
    print("Adieu, adieu, to " + responses[0])
elif len(responses) == 2:
    print("Adieu, adieu, to " + responses[0] + " and " + responses[1])
else:
    print("Adieu, adieu, to", end = " ")
    for each in responses[0:-1]:
        print(each + ",", end = " ")
    print("and", end = " ")
    print(responses[-1])
