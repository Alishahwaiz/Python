#def mix_string(s1, s2):

testing chnages

s1 = input("enter first string ")
#print(s1)

s2 = input("enter first string ")
    # get first character from both string
#print(s2)
first_char = s1[0] + s2[0]

    # get middle character from both string
middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]
print(middle_char)
    # get last character from both string
last_char = s1[len(s1) - 1] + s2[len(s2) - 1]

    # add all
res = first_char + middle_char + last_char
print("Mix String is ", res)


#s1 = "America" s2 = "Japan"
#mix_string(s1, s2)