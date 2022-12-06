#Program for the Banking System
import mysql.connector
from functions import *
cnx=mysql.connector.connect(user='root',password='sweethome',host='127.0.0.1',database='vishal')
if cnx.is_connected()==False:
    print("unable to connect database")
cursor=cnx.cursor()
#function to create an account number

#function for creating account

#function for Depositing 
def deposit():
    acc=int(input("Enter your Account number:: "))
    q=float(input("Enter the Amount::"))
    query='update   data set  Balance={}  where  Account_no={}'.format(q,acc)
    cursor.execute(query)
    cnx.commit()
    print("\n\t\t\t\tDeposited SUCCESSFULLY.....")
    return
'''
#function for  withdrawl
def withdrawl():
    acc=int(input("Enter  your Account_no::"))
    wit=int(input("Enter the amount of money::"))
    
    print("The money you have WITHDRAWL  is,")
    return'''
#function for searching account 
def searching():
    account_no=int(input("Enter you account number ::"))
    query='SELECT * FROM data where Account_no={}'.format(account_no)
    cursor.execute(query)
    result=cursor.fetchall()
    print("____________________________________________________")
    print("\t\t\t\t\tACCOUNT DETAILS")
    for row in result:
        print('Account_no::',row[0])
        print('Name::',row[1])
        print('Age::',row[2])
        print('Email_id::',row[3])
        print('Address::',row[4])
        print('Gender::',row[5])
        print('Nominee::',row[6])
        print('Mobile_no',row[7])
        print('Balance',row[8])
        return
#function for Outstanding Details 
'''def outstanding():

'''

def main():
#MENU of the Program
  i=1
  while(i==1):
        print("\t\t\t\t**************************MENU*********************** ")
        print("1. CREATE  new account")
        print("2. DEPOSIT")
        print("3. WITHDRAWL")
        print("4. SEARCH  Details ")
        print("5. DISPLAY balance outstanding")
        print("6. EXIT..")
        ch=int(input("Enter your choise[1,2,3,4,5,6]::"))
        if ch==1:
            create_account()
            break
        elif ch==2:
            deposit()
            break
        elif ch==3:
            withdrawl()
            break
        elif ch==4:
            searching()
            break
        elif ch==5:
            outstanding()
            break
        elif ch==6:
            break
        else:
            print("\n Incorrect option ,Please try again............")
main()
'''
char=input("DO you want to run the Program again [Y/N]")
if (char==Y or y):
    main()'''
print("***********************************END OF PROGRAM**************************************")