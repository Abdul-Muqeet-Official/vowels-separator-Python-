statement=input("enter the statment :")
vowel="aeiou"
l1=""
l2=""
for i in statement:
	if i in vowel:
		l1=l1+i
	else:
		l2=l2+i
print('Vowel :',l1)
print('Rest of the Statement :', l2)
