import sys
from tkinter.font import names
import PyPDF2
import csv
sys.stdout=open('output.txt','w',encoding='utf-8')
# pdfFileObj = open('File.pdf', 'rb') 

pdfReader = PyPDF2.PdfFileReader('File.pdf') 

for j in range(1,pdfReader.getNumPages()):
    pageObj = pdfReader.getPage(j)    
    print(pageObj.extractText()) 


employee_dict=[]
new_data={}
textfile=open('output.txt','r',encoding='utf-8')
all_names=(textfile.readlines())
for i in all_names:
    if "CA." in i or "Shri" in i:
        if new_data=={}:
            pass
        else:
            employee_dict.append(new_data)
        new_data={}
        new_data['Name']=i
    if "[+91]" in i :
        if 'Phone' in new_data:
            new_data['Phone']+=i
        else:
            new_data['Phone']=i
    if "@" in i:
        if 'Email' in new_data:
            new_data['Email']+=i
        else:
            new_data['Email']=i

employee_info = ['Name', 'Phone','Email','Office Address','Residence Address']
with open('employee.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = employee_info)
    writer.writeheader()
    writer.writerows(employee_dict)