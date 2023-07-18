email=input("enter the Email")

k,j,m=0,0,0

if len(email)>=6:
    if email[0].isalpha():
        if ('@' in email ) and (email.count('@')==1):
            if (email[-4]=='.') ^ (email[-3]=='.'):
                for i in email:
                    if i==i.isspace():
                       k=1
                    elif i==i.isalpha():
                       if i==i.upper():
                          j=1
                       elif i==i.isdigit():
                           continue
                       elif i=='_' or i=='@' or i=='.':
                           continue
                       else:
                           m=1
                       
    
                if k==1 or j==1 or m==1:
                   print('wrong email 5')
                else:
                    print("Right Email")
            else:
                print("Wrong Email 4")
                print("position of '.' should be at third or fouth position from right side")
        else:
            print("wrong Email 3")
            print("count of @ is not more than 1")
    else:
        print("wrong email 2")
        print("please enter the alphabet at first place")
else:
    print("Wrong Email 1")
    print("please enter more than 6 charcter")

