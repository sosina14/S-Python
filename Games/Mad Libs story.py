
print ("    ***    Complet the Mad Libs story     ***  ")
print("On a beautiful (1, adjective) day, I went to the zoo. I saw a funny (2, adjective) monkey swinging from the trees. Then, I spotted a majestic (3. adjective) lion lounging in the sun.  What a wild and (4. adjective) experience!")

words1 = input ("Insert the 1st adjective " )
words2 = input ("Insert the 2nd adjective " )
words3 = input ("Insert the 3rd adjective " )
words4 = input ("Insert the 4th adjective " )

if adjective1.lower() == "sunny":
    additional_sentence = "The sun was shining brightly, and it felt perfect outside."
elif adjective1.lower() == "rainy":
    additional_sentence = "It was drizzling a bit, but the animals seemed to enjoy it."
else:
    additional_sentence = "The weather was quite unusual, adding to the adventure."
print ("    Here is your Mad Libs story:  ")
print(f" On a beautiful {words1} day, I went to the zoo. I saw a funny {words2} monkey swinging from the trees. Then, I spotted a majestic {words3} lion lounging in the sun.  What a wild and (4. {words4} experience!{additional_sentence}")

