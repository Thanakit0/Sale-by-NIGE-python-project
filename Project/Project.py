from tkinter import *
import pandas as pd
import xlsxwriter

global US
US = pd.read_excel('User.xlsx')

def cal_all(Price_Cals):

    global Per_int
    global discount

    if Price_Cals < 5000:
        price_int = int(Price_Cals//1000)
        Per = [0,0.1,0.2,0.3,0.4]       
        discount = Price_Cals * Per[price_int]
        Per_int = ('{:.0f}%'.format(Per[price_int]*100))
    else:
        discount = Price_Cals * 0.5
        Per_int = '50%'
    return discount,Per_int

def pay_():
    
    global total_pay

    En_pay_store2 = float(En_pay_store.get())
    
    total_pay = En_pay_store2 - pay
    Label(finish,text = 'Change of money = '+str(total_pay),fg ="#F0FFFF",bg="#6A5ACD",font='Segoe 10 bold').grid(columnspan=2,row=10)
   
lst_Product_lists=''
lst_Prices=''
list_num =[]

def finish():

    global total_pay
    global En_pay
    global En_pay_store
    global pay
    global lst_Product_lists
    global lst_Prices
    global Payment
    global finish
   
    try:
        
        Price_Cal = sum(lst_Price)* NB 
        finish = Toplevel(p_user)
        
        finish.title('Check')
        finish.minsize(250,280)
        finish.config(bg='#8470FF')
        Product_number = len(lst_Product_list)*NB
        discounts,per = cal_all(Price_Cal) 
        pay = Price_Cal - discount 
        lst_num = NB * 1
           
        for i in lst_Product_list:
            lst_Product_lists+=('{}\n'.format(i))
        for s in lst_Price:
            lst_Prices+=('{}*{} THB\n'.format(lst_num,s))
  
        Label(finish,text = 'Username : ' + Username,fg ="#F0FFFF",bg="#8470FF",font='Segoe 10 bold').grid(columnspan=2,row=0) 
        Label(finish,text = lst_Product_lists,fg ="#F0FFFF",bg="#8470FF",font='Segoe 10 bold').grid(column=0,columnspan=2,row=1) 
        Label(finish,text = str(lst_Prices),fg ="#F0FFFF",bg="#8470FF",font='Segoe 10 bold').grid(column=1,row=1,columnspan=2)  
        Label(finish,text = 'Total product : ' +str(Product_number),fg ="#F0FFFF",bg="#8470FF",font='Segoe 10 bold').grid(columnspan=2,row=2)  
        Label(finish,text = 'Total price : ' +str(Price_Cal),fg ="#F0FFFF",bg="#8470FF",font='Segoe 10 bold').grid(columnspan=2,row=3)  
        Label(finish,text = 'Discount : ' +Per_int,fg ="#F0FFFF",bg="#8470FF",font='Segoe 10 bold').grid(columnspan=2,row=4)
        Label(finish,text = 'Discount price : ' +str(discount),fg ="#F0FFFF",bg="#8470FF",font='Segoe 10 bold').grid(columnspan=2,row=5) 
        Label(finish,text = 'Amount to pay : ' +str(pay),fg ="#F0FFFF",bg="#8470FF",font='Segoe 10 bold').grid(columnspan=2,row=6)  

        En_pay_store = IntVar()

        Label(finish,text = '** Specify your amount to pay **',fg ="#FF6699",bg="#8470FF",font='Segoe 10 bold').grid(columnspan=2,row=7)
        En_pay = Entry(finish,textvariable = En_pay_store,fg='#CC99FF').grid(columnspan=2,row=8)
        Button(finish,text ='Agree',command = pay_,bg='#FF3399',fg='#F0FFFF',width=10).grid(row=9,columnspan=2,pady=10)
        process1.destroy()
               
    except Exception:
        Excep()
 
def notstock():
    
    not_stock = Toplevel(p_user)
    not_stock.title('Out of stock')
    not_stock.minsize(200,150)
    not_stock.config(bg='#F5F5F5')

    Label(not_stock,text = 'We not found product / Out of product',font='Tahoma 16',bg='#F5F5F5',fg = '#990000').grid(pady = 10,sticky =(),row = 0 ,padx = 150)
    Button(not_stock,text ='Accept',command = not_stock.destroy,bg='#D3D3D3',fg='#FF0000',width=5).grid()
       
lst_Price = []
lst_Product_list = []

def ADD(): 

    global lst1
    global PD
    global lst1
    global Price_store2
    global Product_lsit_store2
    global NB

    try:
        
        PD = int(pd_code.get())
        NB = int(nb.get())

        PL = pd.read_excel('Product_list.xlsx')    
        P_code = PL['Product code'].values.tolist()
   
        if PD in P_code :
        
            Price_store = PL.loc[PL["Product code"] == PD, ["Price"]].values.tolist()
            Price_store2 = Price_store[0][0]            
            lst_Price.append(Price_store2)
        
            Product_lsit_store = PL.loc[PL["Product code"] == PD, ["Product list"]].values.tolist()
            Product_lsit_store2 = Product_lsit_store[0][0] 
            lst_Product_list.append(Product_lsit_store2)

            Stock = PL.loc[PL["Product code"] == PD, ["Stock"]].values.tolist()
            Stock2 = Stock[0][0] 
            Stock2 = int(Stock2)
            Stock_ok = Stock2 - NB       
  
            if Stock_ok > 0 and NB != 0:
                            
                    stock_data2 = pd.read_excel(r'Product_list.xlsx')
                    stock_data2.loc[stock_data2["Product code"] == PD, ["Stock"]] = Stock_ok 
                    writer = pd.ExcelWriter('Product_list.xlsx', engine='xlsxwriter')  
                    stock_data2.to_excel(writer, index=False)  
                    writer.save()                 
            else:
                notstock()      
        else:       
            notstock()
    except Exception:
        
        Excep()

def Excep():
    Exception_ADD = Toplevel(p_user)
    Exception_ADD.title('Please Enter data')
    Exception_ADD.minsize(200,150)
    Exception_ADD.config(bg='#F5F5F5')
    Label(Exception_ADD,text="Please Enter data",font='Tahoma 16',bg='#F5F5F5',fg = '#990000').grid(pady = 10,sticky =(),row = 0 ,padx = 150)
    Button(Exception_ADD,text="OK",command = Exception_ADD.destroy,bg='#D3D3D3',fg='#FF0000',width=5).grid()


def process_1 (): 

    global process1
    global pd_code
    global nb
    global En_Product
    global En_nb
    global PL
       
    process1 = Toplevel(p_user)
    process1.minsize(500,320)
    process1.config(bg='#8DEEEE')

    pd_code = StringVar()
    nb = StringVar()
    
    process1.title('Sale by NIGE')

    Label(process1,text='Sale by NIGE',fg ="#FFFAFA",bg="#528B8B",font='Segoe 18 bold').grid(pady = 10,sticky =(),row = 1,padx = 10,column=1)
    Label(process1,text='Enter your product code',fg ="#001100",bg="#79CDCD",font='Tahoma 10').grid(pady = 10,row = 2 ,padx = 10,column=0)
    En_Product = Entry(process1,textvariable = pd_code,bg="#CCFFFF").grid(pady = 10,sticky =(),row = 2 ,padx = 10,column=1)
    Label(process1,text='Number of you buy the product',fg ="#001100",bg="#79CDCD",font='Tahoma 10').grid(pady = 10,row = 3 ,padx = 10,column=0)
    En_nb = Entry(process1,textvariable = nb,bg="#CCFFFF").grid(pady = 10,sticky =(),row = 3 ,padx = 10,column=1)

    Button(process1,text='Add product',command = ADD,fg ="#FFFAFA",bg="#0000DD",width=10).grid(pady = 10,row = 4,column=0)
    Button(process1,text='Finish',command = finish,fg ="#FFFAFA",bg="#009900",width=10).grid(pady = 10,row = 4,column=1)
   
    login_screen.destroy()
    screen1.destroy()   
    
def Login_success():
    global screen1
    screen1 = Toplevel(p_user)
    screen1.title('Login Success')
    screen1.minsize(200,150)
    screen1.config(bg='#F5F5F5')
    Label(screen1,text="Login Success",font='Tahoma 16',bg='#F5F5F5',fg='#008800').grid(pady = 10,sticky =(),row = 0 ,padx = 150)
    Button(screen1,text="OK",command = process_1,bg='#D3D3D3',fg='#008800',width=5).grid()
    
def Wrong_password():
    global screen2
    screen2 = Toplevel(p_user)
    screen2.title('Password Error')
    screen2.minsize(200,150)
    screen2.config(bg='#F5F5F5')
    Label(screen2,text="Password Error",font='Tahoma 16',bg='#F5F5F5',fg = '#990000').grid(pady = 10,sticky =(),row = 0 ,padx = 150)
    Button(screen2,text="OK",command = screen2.destroy,bg='#D3D3D3',fg='#FF0000',width=5).grid()
    
def User_not_found():
    global screen3
    screen3 = Toplevel(p_user)
    screen3.title('User not found')
    screen3.minsize(200,150)
    screen3.config(bg='#F5F5F5')
    Label(screen3,text="User not found",font='Tahoma 16',bg='#F5F5F5',fg = '#990000').grid(pady = 10,sticky =(),row = 0 ,padx = 150)
    Button(screen3,text="OK",command = screen3.destroy,bg='#D3D3D3',fg='#FF0000',width=5).grid()

    
def login_verify(): 

    global Username
    Username = username1.get()
    Password = password1.get()
   
    input_user2.delete(0, END)  
    input_pass2.delete(0, END)

    US = pd.read_excel('User.xlsx')
    id = US['Username'].values.tolist()
    if Username in id:

        verify = US.loc[US["Username"] == Username, ["Password"]].values.tolist()
        v = verify[0][0]
        
        if Password == v:
            Login_success()
        else:
            Wrong_password()
    else:
        User_not_found()
    
def login(): 
    
    global login_screen
    global username1
    global password1
    global input_pass2
    global input_user2
       
    print('-- Process login --')
    login_screen = Toplevel(p_user)
    login_screen.title('Login')
    login_screen.minsize(400,280)
    login_screen.config(bg='#FAFAD2')

    username1 = StringVar()
    password1 = StringVar()

    Label(login_screen,text='  Please enter username  ',font='Segoe 16 bold',bg = '#F4A460').grid(row=0,column=1,columnspan=2,pady = 20)                                
    Label(login_screen,text='Username',bg='#FAFAD2',font='Segoe 10 bold').grid(column=0,row = 1,pady=5)
    
    input_user2 = Entry(login_screen,textvariable = username1 )
    input_user2.grid(column=1,row = 1,pady=10)
    input_user2.focus()
    
    Label(login_screen,text='Password',bg='#FAFAD2',font='Segoe 10 bold').grid(column=0,row = 2,pady=5)
    
    input_pass2 = Entry(login_screen,show="*",textvariable = password1 )
    input_pass2.grid(column=1,row = 2,pady=10)
    
    Button(login_screen,text = 'Login',width = 10,command = login_verify,bg='#008800',fg='white').grid(pady=10,row=3,column=1)

def No_pass():
    no_pass = Toplevel(p_user)
    no_pass.title('Please Enter your password')
    no_pass.minsize(200,150)
    no_pass.config(bg='#F5F5F5')
    Label(no_pass,text="Please Enter your password",font='Tahoma 16',bg='#F5F5F5',fg = '#990000').grid(pady = 10,sticky =(),row = 0 ,padx = 150)
    Button(no_pass,text="OK",command = no_pass.destroy,bg='#D3D3D3',fg='#FF0000',width=5).grid()

def confirm_pass ():
    confirm_pass = Toplevel(p_user)
    confirm_pass.title('Password do not match')
    confirm_pass.minsize(200,150)
    confirm_pass.config(bg='#F5F5F5')
    Label(confirm_pass,text="Password do not match",font='Tahoma 16',bg='#F5F5F5',fg = '#990000').grid(pady = 10,sticky =(),row = 0 ,padx = 150)
    Button(confirm_pass,text="OK",command = confirm_pass.destroy,bg='#D3D3D3',fg='#FF0000',width=5).grid()
    
def data_user():
        
    global Username2
    global Password2
    global lst_data_user
    global US

    US = pd.read_excel('User.xlsx')
                                            
    Username2 = username2.get()
    Password2 = password2.get()
    Password3 = password3.get()
    
    id = US['Username'].values.tolist() 
            
    if Username2  in id:  
        
        Have_account = Tk() 
        Have_account.title('Unable to create an account')
        Have_account.minsize(200,150)
        Have_account.config(bg='#F5F5F5')
        
        Label(Have_account,text = 'This username is already taken',font='Tahoma 16',bg='#F5F5F5').grid(pady = 10,sticky =(),row = 0 ,padx = 150)   
        Button(Have_account,text='OK' , command = Have_account.destroy,width=5,bg='#D3D3D3',fg='#FF0000').grid()
        
        Label(register_screen,text = 'Registration Error',bg='#FAFAD2',fg='#FF0000').grid()

    else:

        if Password2 == '' :
            No_pass()
        else:
            if Password2 == Password3 :
        
                id_data = pd.DataFrame({'Username': [Username2]}) 
                frame = [US, id_data] 
                result = pd.concat(frame) 
  
                writer = pd.ExcelWriter('User.xlsx', engine='xlsxwriter') 
                result.to_excel(writer, sheet_name='Sheet1', index=False) 
                writer.save()

                password = pd.read_excel(r'User.xlsx')
                password.loc[password["Username"] == Username2, ["Password"]] = Password2  
                writer = pd.ExcelWriter('User.xlsx', engine='xlsxwriter')  
                password.to_excel(writer, index=False)  
                writer.save()
        
                Label(register_screen,text = 'Registration Success',bg='#FAFAD2',fg='#FF0000').grid()

            else:
                confirm_pass()      
  
    input_user.delete(0,END)
    input_pass.delete(0,END)
    input_pass_2.delete(0,END)
    
def register():
    
    global register_screen
    global username2
    global password2
    global password3
    global input_pass
    global input_pass_2
    global input_user
       
    print('-- Process register --')
    register_screen = Toplevel(p_user) 
    register_screen.title('Register')
    register_screen.minsize(400,280)
    register_screen.config(bg='#FAFAD2')
    
    username2 = StringVar()
    password2 = StringVar()
    password3 = StringVar()
    
    Label(register_screen,text='Please create a username account',font='Tahoma 16 bold',bg = '#FFE4B5').grid(row=0,column=0,columnspan=2,padx=30,pady=20)
    
    Label(register_screen,text='Username',bg='#FFE4B5').grid(pady = 10,sticky =(),row = 1 ,column=0)
    
    input_user = Entry(register_screen,textvariable = username2 ,bg='#FDF5E6')
    input_user.grid(row=1,column=1)
      
    Label(register_screen,text='Password',bg='#FFE4B5').grid(pady = 4 ,sticky=(),row = 2,column=0)
    input_pass = Entry(register_screen,show="*",textvariable = password2,bg='#FDF5E6' )
    input_pass.grid(row=2,column=1)
    
    Label(register_screen,text='Confirm password',bg='#FFE4B5').grid(pady = 6 ,sticky=(),row = 3,column=0)
    input_pass_2 = Entry(register_screen,show="*",textvariable = password3,bg='#FDF5E6')
    input_pass_2.grid(row=3,column=1)
    
    Button(register_screen,text = 'Register',command = data_user ,width = 10,bg='#EECBAD',fg='#007700').grid(pady = 20 ,sticky=(),row = 10)

def Not_member():
    
    global process1
    global pd_code
    global nb
    global En_Product
    global En_nb
    global PL
    global Username
    
    Username = 'Not a member'
    Not_member = Toplevel(p_user)
    Not_member.minsize(800,300)
    Not_member.title('Sale by NIGE')
    Not_member.config(bg='#FFE4E1')
      
    pd_code = StringVar()
    nb = StringVar()
    
    Label(Not_member,text='Sale by NIGE',fg ="blue violet",bg="#CDB7B5", font='Segoe 22 bold').grid(pady = 10,row = 1,column=2)
    Label(Not_member,text='Enter your product code',fg ="blue violet",bg="#EED5D2", font='Segoe 16 bold').grid(pady = 10,sticky =(),row = 2 ,column=2)
                                                                                
    En_Product = Entry(Not_member,textvariable = pd_code,width = 40,bg="#FFF0F5",fg='#9900FF').grid(pady = 10,row = 3 ,column=2)
    Label(Not_member,text='Number of you buy the product', font='Segoe 16 bold',bg="#EED5D2",fg='#9900FF').grid(pady = 10,row = 4 ,column=2)
    En_nb = Entry(Not_member,textvariable = nb,width = 40,bg="#FFF0F5",fg='#9900FF').grid(pady = 10,row = 5 ,column=2)

    Button(Not_member,text='Add product',command = ADD,bg='#990099',fg='white', font='Segoe 12 bold',width = 10,height= 1).grid(pady = 10,row = 8,column=1,padx=100)
    Button(Not_member,text='Finish',command = finish,bg='#9900CC',fg='white', font='Segoe 12 bold',width = 10,height= 1).grid(pady = 10,row = 8,column=3,padx=100)
    
def main_user():
    
    global p_user
       
    p_user = Tk()
    p_user.title('Sale by NIGE')
    p_user.minsize(400,380)
    p_user.config(bg='#FFEFD5')

    lb = Label(p_user,text=('--- Welcome to my store ---'), font='Segoe 28 bold',
               bg = "#CD853F",fg ="white").grid(padx=10,row=0,column=1,pady=40)
    lb =Label(p_user,text='** Please Login **',
              font="Segoe 20 bold",bg='#FFEFD5').grid(padx=10,row=1,column=1,pady=10)
    
    bt = Button(p_user,text = 'Login',command = login ,width = 20,height= 2,
                bg='#F4A460',fg='#000011',font="Segoe 12 ").grid(padx=30,row=2,column=0,pady=20)
    
    bt = Button(p_user,text = 'Register',
                command = register ,width = 20,height= 2,
                bg='#FFCC99',fg='#000011',font="Segoe 12 ").grid(row=2,column=1,pady=20)
    
    bt = Button(p_user,text = 'Not a member',
                command = Not_member ,width = 20,height=2,
                bg='#8B8989',fg='#000011',font="Segoe 12 ").grid(padx=30,row=2,column=2,pady=20)
    
    p_user.mainloop()
    
main_user()
