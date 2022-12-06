from random import randint
def account_no():
    return int("3"+str(randint(10**(12-1),  (10**12)-1)))

def create_account():
    print("************************************************************************")
    a=account_no()
    b=input("Enter Name::")
    c=int(input("Enter Age::"))
    d=input("Enter Email_id:: ")
    e=input("Enter Address::")
    f=input("Enter Gender::")
    g=input("Enter Nominee::")
    h=int(input("Enter Mobile_no::"))
    i=float("Balance")
    query="INSERT INTO  data(Account_No,Name,Age,Email_id,Address,Gender,Nominee,Mobile_no) values({},'{}',{},'{}','{}','{}','{}',{},{}) ".format(a,b,c,d,e,f,g,h,i)
    cursor.execute(query)
    cnx.commit()
    print("Your Data is SUCCESSFULL inserted..............")
    return