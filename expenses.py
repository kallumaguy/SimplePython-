# expenses =[10.5,8,5,15,20,5,3]
# # sum=0
# # for x in expenses:
# #     sum=sum+x
# total=sum(expenses)
# print("You spent $",total," on lunch this week.",sep='')

#program to input expenses using for loop and display the total expenses
total = 0
expenses = []
num=int(input("Enter the number of expense:"))
for i in range(num):
    expenses.append(float(input("Enter an expense: ")))
total=sum(expenses)
print("You spent $",total,sep='')