'''WAP which accepts marks of four subject and display total marks , percentage and grade .
# Hint : more than 70% -> distinction , more than 60%-> first, more than 40%-> pass, less
 than 40% -> fail'''
marks_of_1st_sub = int (input("Enter the marks in first subject: "))
marks_of_2nd_sub = int(input('Enter the marks in second subject:'))
marks_of_3rd_sub = int(input("Enter the marks in third subject:"))
marks_if_4th_sub = int(input("Enter the marks in fourth subject:"))
total_marks = marks_of_1st_sub +marks_of_2nd_sub + marks_of_3rd_sub +marks_if_4th_sub
percentage = ((total_marks)/400) *100
if percentage > 70:
    print("you got grade 'A' which is distinction ")
elif percentage >= 60 and percentage < 70:
    print("You got grade 'B+' which is first division")
elif percentage>=40 and percentage < 60 :
   print("You got grade 'B' which is pass")
elif percentage < 40:
    print("You are looser and failer")
