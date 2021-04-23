''' Given three integers , print the smallest one .Three integers should be user input'''


first_num = int(input("Enter the first number:"))
second_num = int(input("Enter the seond number:"))
third_num = int(input("Enter the third nuber:"))
if first_num < second_num < third_num:
    print(f" first_num is the smallest one")
elif second_num < first_num < third_num :
    print(f"second_num is the smallest one:")
else:
    print(f"third_num is the smallest one")