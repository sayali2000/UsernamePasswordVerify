# 1 a. All Sentences of the poem will be printed on the same line,
#      and finally cursor will be on the new line.

"""
# move file pointer to  end of file
file=open('sarojiniPoem.txt','r')
f.seek(0,2)     # go to end of file
print(f.tell())
file.close()

# 1 b.
file=open('sarojiniPoem.txt','r')
text=file.readlines()
file.close()
         
for line in reversed(text):
    print(line)
#for line in range(len(text)-1,-1,-1):
#    print(textline])
print()


#1.c.d e
file=open('sarojiniPoem.txt','r')
text=file.readlines()
file.close()
fo=open('output.txt','w')
#fo=open('output.txt','a')
#fo.writelines(text)
lc=1
for line in (text):
    #fo.write(line+'\n')
    print(lc,line)
    lc+=1
fo.close()

# 2.
Lcount=Ecount=ccount=0
for lines in text:
    if line =='\n':
        Lcount+=1
        Ecount+=1
    else: 
        Lcount+=1
        words=line.split() #gets words from sentence
        for w in words:
            ccount+=len(w)
            print(Lcount)
            print(Ecount)
            print(ccount/(Lcount-Ecount))
            print(ccount/Lcount)
        
     
# 3 User Name and Password verification
       
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



# 4  
print(open('sarojiniPoem.txt').readlines())
 
 # 5
fname=input("Enter finename along with extention")
file=open(fname,'r')
text=file.readline()
while text:
    print(text.upper())
    text=file.readline()
file.close()

#6 
file=open('sarojiniPoem.txt','r')
fo=open('output.txt','w')
text=file.read()
for i in range(0,len(text)):
    print(text[i])
    if text[i].isupper():
        fo.write(text[i].lower())
    elif texti].islower():
        fo.write(text[i].upper())
    else:
        fo.write(text[i])
    
    
file.close()
fo.close() 


# 7 and 8
fo=open('phonebook.dat','w')
fo.write('Name'+'\t'+'Phone'+'\n')
while True:
    Name=input("enter name:")
    Phone=int(input("enter phone:"))
    fo.write(Name+'\t'+str(Phone)+'\n')
    ans=input('do u want to enter more:')
    if ans.upper()=='N':
        break
fo.close()

# 9
import os
found=0
fi=open('phonebook.dat','r')
fo=open('temp.dat','w')
text=fi.readline()
while text:
    if 'Arvind' in text:
         Phone=(input("enter new phone for Arvind:"))
         st=text.split()
         st[1]=Phone
         text=st[0]+'\t'+st[1]
         fo.write(text)
         found=1
         break
    else:
         fo.write(text)
    text=fi.readline()   
else:
    print("Error")

if(found==1):    
    pos=fi.tell()
    text=fi.read()
    fo.write(text)
fi.close()
fo.close()
os.remove('phonebook.dat')
os.rename('temp.dat','phonebook.dat')


#9
fi=open('phonebook.dat','r+')
fo=open('temp.dat','w')
text=fi.readlines()     # read a complete file 
#print(text)
found=0
for i in range(len(text)):
    twoparts=text[i].split('\t')       # lets break a line in 2 parts
   #print(twoparts,twoparts[0],twoparts[1])
    if twoparts[0]=='Arvind':
        twoparts[1]=(input("enter new phone for Arvind:"))
        found=1
    text[i]=twoparts[0]+'\t'+twoparts[1]
    print(text)    
fi.seek(0)              # bring file object to the beginning of a file
fi.writelines(text)       
    
if found==0:
    print("There is no record for Arvind")

fi.close()
fo.close()


#ADDITIONAL QUESTIONS IN fILE HANDLING
# COUNT THE NUMBER OF LINES IN A FILE & CALCULATE THE SIZE OF A FILE IN BYTES
fi=open('upper.txt','rb')
text=fi.readlines()
print(text,"Total lines in file are:",len(text))   #count no of lines
print("size of  a file:",fi.tell())   # size of file


# FIND THE NUMBER OF CHARACTERS IN A FILE, EOL CHARCATERS, NOT INCLUDING WHITESPACES,BLANK LINES
# LEADING AND TRAILING WHITESPACES USING READLINE() AND READLINES()
fi=open('upper.txt','r')
text=fi.readlines()
eolcount=len(text)     # no of lines in file =no of EOL charcaters
blankline=0
for i in text:
    if(len(i)==3):             # by default it adds 2 spaces in black line + '\n'
        blankline+=1

fi.seek(0)
text=fi.readline()
trspace=lspace=whitespace=characters=0
while text:
    #print(len(text),len(text.lstrip()),len(text)-len(text.lstrip()))  
   # print(len(text),len(text.rstrip()),len(text)-len(text.rstrip()))# default one trailing space after a word or character
    lspace+=len(text)-len(text.lstrip())
    trspace+=len(text)-len(text.rstrip())
    for i in text:
        print((i))
        if (i).isspace():
            whitespace+=1
        if (i).isalpha():
            characters+=1
    
    text=fi.readline()

print("Total EOL characters in file:",eolcount)
print("Total blank lines in file:",blankline)
print("Total WhiteSpaces in file:",whitespace-eolcount)
print("Total Trailing  spaces in file:",trspace)
print("Total leading spaces in file:",lspace)
print("Total characters in file:",characters)
fi.olose()


# IN A EXISTING TEXT FILE REPLACE ALL OCURRENCES OF 'i' WITH 'I'
fi=open('upper.txt','r')
text=fi.readlines()
for i in range(len(text)):
    text[i]=text[i].replace('i','I')
print(str(text))


# Delete 5th line of text file.
import os
fi=open('upper.txt','r')
fo=open('duplicate.txt','w+')
text=fi.readlines()
for i in range(len(text)):
    if i!=4:                 # list counting begins from 0
        fo.write(text[i])  # copy all lines except 5th into duplicate.txt
fi.close()
fo.close()
os.remove('upper.txt')
os.rename('duplicate.txt','upper.txt')
"""
#WAp to do the following:
"""1. Create file File1.txt
       Blue Sky
       Blue Ocean
       Green Grass
       Green Leaf
       Orange Sun
       Red Roses
       Red Straberry
Replace all 'Red' words with 'White'. Delete a line 'Orange Sun'.
Show file contents before and after modification """

#import os
#fo=open('duplicate.txt','w+')
fi=open('upper.txt','w+')
L=['Blue sky\n','Blue Ocean\n','Green Grass\n','Green Leaf\n','Orange Sun\n','Red Roses\n','Red Strawberry\n']

fi.writelines(L)
fi.seek(0)
text=fi.readlines()
print('Before modification File1.txt contents')     
print(text)
for i in range(len(text)):
    text[i]=text[i].replace('Red','White')  
text.remove('Orange Sun\n')  

print('After modification File1.txt contents')    
print(text)
fi.writelines(text)
fi.seek(0)
text=fi.readlines()

        
 

       

























