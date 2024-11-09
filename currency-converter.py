import requests
from tkinter import *   
import tkinter.ttk as ttk
import time

# Where INR is the base currency you want to use - from the api url 
url = 'https://api.exchangerate-api.com/v4/latest/INR'
urlusd= 'https://api.exchangerate-api.com/v4/latest/USD'
urleur= 'https://api.exchangerate-api.com/v4/latest/EUR'
urlgbp= 'https://api.exchangerate-api.com/v4/latest/GBP'

# Making our request - using the requests module
response = requests.get(url)
responseusd = requests.get(urlusd)
responseeur = requests.get(urleur)
responsegbp = requests.get(urlgbp)

data = response.json()
datausd= responseusd.json()
dataeur= responseeur.json()
datagbp= responsegbp.json()

#DATE and TIME
localtime=time.asctime(time.localtime(time.time()))

#Iterating through the lists to obtain the countries and its exchange rates (includes file handling)
valu=[]
rats=[]
for i in data['rates'].keys():
    valu.append(i)

for i in valu:
    rats.append(data['rates'][i])
#print("r",rats,"v",valu)
Dat_con = open('ExchangeRates.txt','w')
rec=[]

ExRA='Real Time Exchange Rates' +'\n' +'-------'+'\n'
Dat_con.write(ExRA)
for i in range(len(rats)):
    rec=valu[i] + " : " + str(rats[i]) 
    if i%2!=0:
        rec1=rec + '\n' 
        Dat_con.write(rec1)
    else:
        rec2=rec +'      '
        Dat_con.write(rec2)
Dat_con.close()

Dat_con = open('ExchangeRates.txt','r')

file = Dat_con.read()
#print(file)
#print(Dat_con)#Use this if you want to print the file in cui interface
Dat_con.close() 

#defining elements for the initial window  
def currency_converter():
    #creating instance of tkinter
    currency_converter = Tk()  
    #Set title of our window form  
    currency_converter.title("Currency Convertor")
    #Set dimension of form 
    currency_converter.geometry("475x350")
    #Centers the Window
    currency_converter.update_idletasks()
    w = currency_converter.winfo_screenwidth()
    h = currency_converter.winfo_screenheight()
    size = tuple(int(_) for _ in currency_converter.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    currency_converter.geometry("%dx%d+%d+%d" % (size + (x, y))) 

    currency_converter.rowconfigure(5, weight=1)

    currency_converter.lift()

#    currency_converter.overrideredirect(1) #Remove border
    currency_converter.configure(background='#007780')

#defining the elements for the second window which displays the exchage rates    
    def check_exchange_rates():
        window2=Tk()
        window2.title("Exchange Rates")
        window2.geometry("400x700")
        window2.configure(background="#007780")
        w2=Label(window2,text=file, bg='#007780', fg='white',font=("Times New Roman",15,'bold'))
        w2.pack(side= LEFT)
        window2.mainloop


#defining elements for graph window
    def cvb():
        UserInput = float(Currency_Input.get().replace(',', '.'))
        Currency_Output.delete(0,END)
        Currency_Output1.delete(0,END)
        Currency_Output2.delete(0,END)
        window3=Tk()
        c=Canvas(window3,width=1000,height=800,bg="black")
        c.pack()
        if box.get() == "EUR":
            c.create_line(200,600-UserInput,200,600,width=10,fill="red")
            c.create_line(250,600-UserInput*dataeur['rates']['USD'],250,600,width=10,fill="blue")
            c.create_line(300,600-UserInput*dataeur['rates']['GBP'],300,600,width=10,fill="yellow")
            c.create_line(350,600-UserInput*dataeur['rates']['INR'],350,600,width=10,fill="green")
        elif box.get() == "USD":
            c.create_line(200,600-UserInput,200,600,width=10,fill="blue")
            c.create_line(250,600-UserInput*datausd['rates']['EUR'],250,600,width=10,fill="red")
            c.create_line(300,600-UserInput*datausd['rates']['GBP'],300,600,width=10,fill="yellow")
            c.create_line(350,600-UserInput*datausd['rates']['INR'],350,600,width=10,fill="green")
        elif box.get() == "GBP":
            c.create_line(200,600-UserInput,200,600,width=10,fill="yellow")
            c.create_line(250,600-UserInput*datagbp['rates']['USD'],250,600,width=10,fill="blue")
            c.create_line(300,600-UserInput*datagbp['rates']['EUR'],300,600,width=10,fill="red")
            c.create_line(350,600-UserInput*datagbp['rates']['INR'],350,600,width=10,fill="green")
        elif box.get() == "INR":
            c.create_line(200,600-UserInput,200,600,width=10,fill="green")
            c.create_line(250,600-UserInput*data['rates']['USD'],250,600,width=10,fill="blue")
            c.create_line(300,600-UserInput*data['rates']['GBP'],300,600,width=10,fill="yellow")
            c.create_line(350,600-UserInput*data['rates']['EUR'],350,600,width=10,fill="red")
        
        window3.geometry("1000x600")



#defining the functions when the entry is given by the user
    def enter(event):
        UserInput = float(Currency_Input.get().replace(',', '.'))
        Currency_Output.delete(0,END)
        Currency_Output1.delete(0,END)
        Currency_Output2.delete(0,END)
        if box.get() == "EUR":            
            Currency_Output_Label.config(text="USD")
            Currency_Output.insert(0,UserInput*dataeur['rates']['USD'])
            Currency_Output1_Label.config(text="GBP")
            Currency_Output1.insert(0,UserInput*dataeur['rates']['GBP'])
            Currency_Output2_Label.config(text="INR")
            Currency_Output2.insert(0,UserInput*dataeur['rates']['INR'])
        elif box.get() == "USD":
            Currency_Output_Label.config(text="EUR")
            Currency_Output.insert(0,UserInput*datausd['rates']['EUR'])
            Currency_Output1_Label.config(text="GBP")
            Currency_Output1.insert(0,UserInput*datausd['rates']['GBP'])
            Currency_Output2_Label.config(text="INR")
            Currency_Output2.insert(0,UserInput*datausd['rates']['INR'])
        elif box.get() == "GBP":
            Currency_Output_Label.config(text="EUR")
            Currency_Output.insert(0,UserInput*datagbp['rates']['EUR'])
            Currency_Output1_Label.config(text="USD")
            Currency_Output1.insert(0,UserInput*datagbp['rates']['USD'])
            Currency_Output2_Label.config(text="INR")
            Currency_Output2.insert(0,UserInput*datagbp['rates']['INR'])

        elif box.get() == "INR":
            Currency_Output_Label.config(text="EUR")
            Currency_Output.insert(0,UserInput*data['rates']['EUR'])
            Currency_Output1_Label.config(text="USD")
            Currency_Output1.insert(0,UserInput*data['rates']['USD'])
            Currency_Output2_Label.config(text="GBP")
            Currency_Output2.insert(0,UserInput*data['rates']['GBP'])


#defining the quit button function
    def close_currency_converter():
        currency_converter.destroy()

#properties and dimensions of labels,buttons and combobox
    Headline_Label = Label(currency_converter, text='Currency Converter', bg='#007780', fg='white',font=("Century Gothic",16))
    Headline_Label.grid(row=0,column=0, columnspan=2, padx=5, pady=5, sticky=W)

    Box_Headline_Label = Label(currency_converter, text='Which Currency?', bg='#007780', fg='white',font=("Century Gothic",11))
    Box_Headline_Label.grid(row=1,column=0, columnspan=1, padx=5, pady=5, sticky=W)

    box_value = StringVar() 
    box = ttk.Combobox(currency_converter, textvariable=box_value, width=10)
    box['values'] = ('EUR', 'USD', 'GBP', 'INR')
    box.current(0)
    box.grid(row=1,column=1, pady=5, sticky=E)

    Currency_Input = Entry(currency_converter)
    Currency_Input.grid(row=1,column=2, padx=10, pady=5, sticky=W)

    Currency_Input.bind('<Return>',enter)

    Currency_Output_Label = Label(currency_converter, text='', bg='#007780', fg='white',font=("Century Gothic",11))
    Currency_Output_Label.grid(row=2,column=1, padx=5, pady=5, sticky=W)

    Currency_Output1_Label = Label(currency_converter, text='', bg='#007780', fg='white',font=("Century Gothic",11))
    Currency_Output1_Label.grid(row=3,column=1, padx=5, pady=5, sticky=W)   

    Currency_Output2_Label = Label(currency_converter, text='', bg='#007780', fg='white',font=("Century Gothic",11))
    Currency_Output2_Label.grid(row=4,column=1, padx=5, pady=5, sticky=W)  

    Currency_Output = Entry(currency_converter)
    Currency_Output.grid(row=2,column=2, padx=10, pady=5, sticky=W)

    Currency_Output1 = Entry(currency_converter)
    Currency_Output1.grid(row=3,column=2, padx=10, pady=5, sticky=W)

    Currency_Output2 = Entry(currency_converter)
    Currency_Output2.grid(row=4,column=2, padx=10, pady=5, sticky=W)
    
    Button(currency_converter,text="Quit",command=close_currency_converter).grid(row=6,column=0, sticky=E+S+W, pady=5, padx=5)
    Button(currency_converter,text="Check Exchange Rates",command=check_exchange_rates).grid(row=6,column=1,sticky=W+S+E,pady=5,padx=5)
    Button(currency_converter,text="graph view",command=cvb).grid(row=6,column=2, sticky=S+W+E ,pady=5, padx=5)
    

    DATE_Label = Label(currency_converter, text=localtime, bg='#007780', fg='white',font=("Century Gothic",11))
    DATE_Label.grid(row=5,column=0, columnspan=1, padx=5, pady=5, sticky=W)
    
    currency_converter.mainloop()

currency_converter()







