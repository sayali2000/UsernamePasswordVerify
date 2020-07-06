#  User Name and Password verification in File
       
def verify(uid):
    while True: 
        pas=input('Enter password:')
        if(len(pas)>=8):
            if('@' in pas or '%' in pas or '$' in pas):
                d=[0,1,2,3,4,5,6,7,8,9]
                count=0
                for i in d:
                    if str(i) in pas:
                        count+=1
                else:
                    if(count>0):
                        print('Valid password')
                        file=open('Security.txt','a')
                        file.write(uid+'\t'+pas+'\n')
                        file.close()
                        return(1)
            else:
                pass
        else:
            print('Password must be 8 characters long, at least one digit,and a special character(@or % or$)')
            print('Enter again')
        
       

        
file=open('Security.txt','r')
d=file.readlines()
L=data=[]
for i in d:
    L=i.split()
    data.append(L[0])
    print(L,data)
file.close()


uidvalid=True
while True:
    uid=input('Enter username:')
    if uid not in data:
        verify(uid)            
        break  
  
    print("user name already exist, please enter it again")

print('successfully appened uid and pass')  