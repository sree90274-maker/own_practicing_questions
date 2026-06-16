numbers=[10,4,6,7,8,16,15]
largest=numbers[0] 
for i in numbers:
	if i>largest:
		largest=i
print(largest)
print("______________________________")
#In a shopping application, how would you calculate the total cost of 5 items priced at ₹200 each?
items=5
price=200
total=items*200
print(total)
print("______________________________")
#find square of a number
num=16
square=num**num
print(square)
print("_____________________________")
num=int(input("Enter a number:"))
if num%2==0:
	print("it is a even:")
else:
	print("not a even:")
print("___________________________")
num_of_items=10
each_item_cost=150
total_amt=10*150
print(total_amt)
print("__________________________________")
#How do comparison operators help in login validation?
student_name="durga"
roll_no=101
student_name=input("enter a student_name:")
student_id=int(input("enter a student_id:"))
if student_name==student_name and student_id==roll_no:
	print("login_sucessful:")
else:
	print("student is invalid:")
print("____________________________")
#Write a condition to check whether a student passed if marks are greater than or equal to 35.
student_name="durga"
student_class="10th"
telugu=90
hindi=80
english=70
maths=35
soc=90
sci=50
if telugu>=35 and hindi>=35 and english>=35 and maths>=35 and soc>=35 and sci>=35:
	print("student pass:")
else:
	print("fail:")
print("____________________________")











