#!/usr/bin/env python
# coding: utf-8

from tkinter import *
import math,random,os
from tkinter import messagebox

#initializing all variables
#creating frames, labels, buttons and enytries
class Bill_App:
    
    def __init__(self,root):                          # Constructor for the initiation of the Object of the Class.
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing App")
        bg_color="#bcbcbc"
        title=Label(self.root,text="BROGRAMMERS SUPER MART",bd=6,relief=GROOVE,bg=bg_color,fg="black",font=("times new roman",26,"bold"),pady=2).pack(fill=X)
        #relief means the border designs...
        
        # ************Variables***************
        # *********Cosmetics***********
        
        self.bath=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.hair_gel=IntVar()
        self.hair_shampoo=IntVar()
        self.body_lotion=IntVar()
        
        # *********Groceries***********
        
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.pulses=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        
        # *********Drinks***********
        
        self.roohAfza=IntVar()
        self.milkShake=IntVar()
        self.rasna=IntVar()
        self.coke=IntVar()
        self.maaza=IntVar()
        self.lemonades=IntVar()
        
         # *********Total Price and Tax Variables***********
        
        self.m1=StringVar()
        self.m2=StringVar()
        self.m3=StringVar()
        
        self.c1=StringVar()
        self.c2=StringVar()
        self.c3=StringVar()
        
        #************Customer Variables****************
        
        self.cname=StringVar()
        self.cphone=StringVar()
        x=random.randint(1000,99999)
        self.cbill=StringVar()
        self.cbill.set(str(x))
        self.search_bill=StringVar()
        
        # Now, we need to assign these varibales to each and every textfield specified respectively.
        
        # **********Customer Detail Frame************
        F1=LabelFrame(self.root,text="Customer Details",font=("times new roman",15,"bold"),fg="red",bg=bg_color,bd=5,relief=GROOVE)
        F1.place(x=0,y=60,relwidth=1)
        
        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="black",font=("times new roman",16,"bold")).grid(row=0,column=0,padx=15,pady=6)
        cname_txt=Entry(F1,width=15,bd=3,relief=SUNKEN,textvariable=self.cname,font=("arial",16)).grid(row=0,column=1,padx=15,pady=6)
        
        cphone_lbl=Label(F1,text="Phone Number",bg=bg_color,fg="black",font=("times new roman",16,"bold")).grid(row=0,column=2,padx=15,pady=6)
        cphone_txt=Entry(F1,width=15,bd=3,relief=SUNKEN,textvariable=self.cphone,font=("arial",16)).grid(row=0,column=3,padx=15,pady=6)
        
        cbill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="black",font=("times new roman",16,"bold")).grid(row=0,column=4,padx=15,pady=6)
        cbill_txt=Entry(F1,width=15,bd=3,relief=SUNKEN,textvariable=self.search_bill,font=("arial",16)).grid(row=0,column=5,padx=15,pady=6)
        
        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=4,font=("arial",12,"bold")).grid(row=0,column=6,padx=15,pady=6)
        
        #***********Cosmetics Frame************
        F2=LabelFrame(self.root,text="Cosmetics",font=("times new roman",15,"bold"),fg="red",bg=bg_color,bd=5,relief=GROOVE)
        F2.place(x=2,y=140,width=320,height=330)
        
        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=0,column=0,padx=10,pady=5,sticky="w")
        bath_txt=Entry(F2,width=12,textvariable=self.bath,font=("times new roman",16),bd=3,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)
        
        face_cream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=1,column=0,padx=10,pady=5,sticky="w")
        face_cream_txt=Entry(F2,width=12,textvariable=self.face_cream,font=("times new roman",16),bd=3,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=5)
        
        face_wash_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=2,column=0,padx=10,pady=5,sticky="w")
        face_wash_txt=Entry(F2,width=12,textvariable=self.face_wash,font=("times new roman",16),bd=3,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=5)
        
        hair_shampoo_lbl=Label(F2,text="Hair Shampoo",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=3,column=0,padx=10,pady=5,sticky="w")
        hair_shampoo_txt=Entry(F2,width=12,textvariable=self.hair_shampoo,font=("times new roman",16),bd=3,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=5)
        
        hair_gel_lbl=Label(F2,text="Hair Gel",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=4,column=0,padx=10,pady=5,sticky="w")
        hair_gel_txt=Entry(F2,width=12,textvariable=self.hair_gel,font=("times new roman",16),bd=3,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=5)
        
        body_lotion_lbl=Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=5,column=0,padx=10,pady=5,sticky="w")
        body_lotion_txt=Entry(F2,width=12,textvariable=self.body_lotion,font=("times new roman",16),bd=3,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=5)
        
        #***********Grocery Frame************
        F3=LabelFrame(self.root,text="Groceries",font=("times new roman",15,"bold"),fg="red",bg=bg_color,bd=5,relief=GROOVE)
        F3.place(x=330,y=140,width=305,height=330)
        
        rice_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=0,column=0,padx=10,pady=5,sticky="w")
        rice_txt=Entry(F3,width=12,textvariable=self.rice,font=("times new roman",16),bd=3,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)
        
        food_oil_lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=1,column=0,padx=10,pady=5,sticky="w")
        food_oil_txt=Entry(F3,width=12,textvariable=self.food_oil,font=("times new roman",16),bd=3,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=5)
        
        pulses_lbl=Label(F3,text="Pulses",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=2,column=0,padx=10,pady=5,sticky="w")
        pulses_txt=Entry(F3,width=12,textvariable=self.pulses,font=("times new roman",16),bd=3,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=5)
        
        wheat_lbl=Label(F3,text="Wheat Flour",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=3,column=0,padx=10,pady=5,sticky="w")
        wheat_txt=Entry(F3,width=12,textvariable=self.wheat,font=("times new roman",16),bd=3,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=5)
        
        sugar_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=4,column=0,padx=10,pady=5,sticky="w")
        sugar_txt=Entry(F3,width=12,textvariable=self.sugar,font=("times new roman",16),bd=3,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=5)
        
        tea_lbl=Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=5,column=0,padx=10,pady=5,sticky="w")
        tea_txt=Entry(F3,width=12,textvariable=self.tea,font=("times new roman",16),bd=3,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=5)
        
         #***********Cold Drinks Frame************
        F4=LabelFrame(self.root,text="Drinks",font=("times new roman",15,"bold"),fg="red",bg=bg_color,bd=5,relief=GROOVE)
        F4.place(x=640,y=140,width=330,height=330)
        
        roohAfza_lbl=Label(F4,text="RoohAfza",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=0,column=0,padx=10,pady=5,sticky="w")
        roohAfza_txt=Entry(F4,width=12,textvariable=self.roohAfza,font=("times new roman",16),bd=3,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)
        
        milkShake_lbl=Label(F4,text="Milk Shake",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=1,column=0,padx=10,pady=5,sticky="w")
        milkShake_txt=Entry(F4,width=12,textvariable=self.milkShake,font=("times new roman",16),bd=3,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=5)
        
        rasna_lbl=Label(F4,text="Rasna",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=2,column=0,padx=10,pady=5,sticky="w")
        rasna_txt=Entry(F4,width=12,textvariable=self.rasna,font=("times new roman",16),bd=3,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=5)
        
        coke_lbl=Label(F4,text="Coke/Coke diet",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=3,column=0,padx=10,pady=5,sticky="w")
        coke_txt=Entry(F4,width=12,textvariable=self.coke,font=("times new roman",16),bd=3,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=5)
        
        maaza_lbl=Label(F4,text="Maaza",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=4,column=0,padx=10,pady=5,sticky="w")
        maaza_txt=Entry(F4,width=12,textvariable=self.maaza,font=("times new roman",16),bd=3,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=5)
        
        lemonades_lbl=Label(F4,text="Lemonades",font=("times new roman",16,"bold"),bg=bg_color,fg="darkblue").grid(row=5,column=0,padx=10,pady=5,sticky="w")
        lemonades_txt=Entry(F4,width=12,textvariable=self.lemonades,font=("times new roman",16),bd=3,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=5)

        #************Bill Frame**********
        F5=Frame(self.root,bd=5,relief=GROOVE)
        F5.place(x=975,y=140,width=375,height=330)
        bill_title=Label(F5,text="Bill Area",font="Arial 15",bd=5,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scroll_y.set) #self isile lagaya hai taaki isko mai globally access kr saku.
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview) #It is used to configure the scrollBar with the textarea specified.
        self.textarea.pack(fill=BOTH,expand=1)
        
        #***********Button(Bill Menu) Frame*********
        F6=LabelFrame(self.root,text="Bill Menu",font=("times new roman",15,"bold"),fg="dark red",bg=bg_color,bd=5,relief=GROOVE)
        F6.place(x=0,y=470,relwidth=1,height=235)
        m1_lbl=Label(F6,text="Total Cosmetics Bill(Rs.)",bg=bg_color,fg="black",font=("times new roman",16,"bold")).grid(row=0,column=0,padx=20,pady=10,sticky="w")
        m1_txt=Entry(F6,width=15,textvariable=self.m1,font="arial 15",bd=3,relief=SUNKEN).grid(row=0,column=1,padx=20,pady=10)
        
        m2_lbl=Label(F6,text="Total Groceries Bill(Rs.)",bg=bg_color,fg="black",font=("times new roman",16,"bold")).grid(row=1,column=0,padx=20,pady=10,sticky="w")
        m2_txt=Entry(F6,width=15,textvariable=self.m2,font="arial 15",bd=3,relief=SUNKEN).grid(row=1,column=1,padx=20,pady=10)
        
        m3_lbl=Label(F6,text="Total Drinks Bill(Rs.)",bg=bg_color,fg="black",font=("times new roman",16,"bold")).grid(row=2,column=0,padx=20,pady=10,sticky="w")
        m3_txt=Entry(F6,width=15,textvariable=self.m3,font="arial 15",bd=3,relief=SUNKEN).grid(row=2,column=1,padx=20,pady=10)
        
        c1_lbl=Label(F6,text="Cosmetics Tax",bg=bg_color,fg="black",font=("times new roman",16,"bold")).grid(row=0,column=2,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F6,width=15,textvariable=self.c1,font="arial 15",bd=3,relief=SUNKEN).grid(row=0,column=3,padx=20,pady=10)
        
        c2_lbl=Label(F6,text="Groceries Tax",bg=bg_color,fg="black",font=("times new roman",16,"bold")).grid(row=1,column=2,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F6,width=15,textvariable=self.c2,font="arial 15",bd=3,relief=SUNKEN).grid(row=1,column=3,padx=20,pady=10)
        
        c3_lbl=Label(F6,text="Drinks Tax",bg=bg_color,fg="black",font=("times new roman",16,"bold")).grid(row=2,column=2,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F6,width=15,textvariable=self.c3,font="arial 15",bd=3,relief=SUNKEN).grid(row=2,column=3,padx=20,pady=10)
        
        btn_F=Frame(F6,bd=5,relief=GROOVE)
        btn_F.place(x=870,width=470,height=145)
        
        total_btn=Button(btn_F,command=self.total,text="Total",bg="darkred",fg="white",pady=20,font="arila 15 bold",width=6,bd=5,relief=GROOVE).grid(row=0,column=0,padx=7,pady=10)
        generate_btn=Button(btn_F,command=self.bill_area,text="Generate Bill",bg="cadetblue",fg="white",pady=20,font="arila 15 bold",width=11,bd=5,relief=GROOVE).grid(row=0,column=1,padx=5,pady=10)
        reset_btn=Button(btn_F,command=self.reset,text="Reset",bg="lightyellow",fg="black",pady=20,font="arila 15 bold",width=6,bd=5,relief=GROOVE).grid(row=0,column=2,padx=5,pady=10)
        exit_btn=Button(btn_F,command=self.exit,text="Exit",bg="orange",fg="white",pady=20,font="arila 15 bold",width=6,bd=5,relief=GROOVE).grid(row=0,column=3,padx=5,pady=10)
        
        co_frame=Frame(self.root,bg=bg_color)
        co_frame.place(x=1100,y=640,width=245,height=35)
        auth=Label(co_frame,text="~TEAM BROGRAMMERS",font=("Calibri 14"),fg="black",pady=40,bg=bg_color).pack()
        self.welcome_bill()
        
    def total(self):
        self.bath_price= self.bath.get()*40
        self.face_cream_price= self.face_cream.get()*40
        self.face_wash_price= self.face_wash.get()*40
        self.hair_shampoo_price= self.hair_shampoo.get()*40
        self.hair_gel_price= self.hair_gel.get()*40
        self.body_lotion_price= self.body_lotion.get()*40
        
        self.rice_price= self.rice.get()*30
        self.food_oil_price= self.food_oil.get()*30
        self.pulses_price= self.pulses.get()*30
        self.wheat_price= self.wheat.get()*30
        self.sugar_price= self.sugar.get()*30
        self.tea_price= self.tea.get()*30
        
        self.roohAfza_price= self.roohAfza.get()*50
        self.milkShake_price= self.milkShake.get()*50
        self.rasna_price= self.rasna.get()*50
        self.coke_price= self.coke.get()*50
        self.maaza_price= self.maaza.get()*50
        self.lemonades_price= self.lemonades.get()*50 
        
        self.total_cosmetic= float(self.bath_price+
                                      self.face_cream_price+
                                      self.face_wash_price+
                                      self.hair_shampoo_price+
                                      self.hair_gel_price+
                                      self.body_lotion_price
                                  )
        self.m1.set(str(self.total_cosmetic))        # str me typecast kia hai because m1 is StringVar().       
            
        self.total_grocery=float(self.rice_price+
                                 self.food_oil_price+
                                 self.pulses_price+
                                 self.wheat_price+
                                 self.sugar_price+
                                 self.tea_price
                                )
        self.m2.set(str(self.total_grocery)) 
            
        self.total_drink=float(self.roohAfza_price+
                               self.milkShake_price+
                               self.rasna_price+
                               self.maaza_price+
                               self.coke_price+
                               self.lemonades_price
                              )
        self.m3.set(str(self.total_drink)) 
        
        self.cosmetic_tax=round(self.total_cosmetic*0.05,2)
        self.grocery_tax=round(self.total_grocery*0.03,2)
        self.drink_tax=round(self.total_drink*0.02,2)
        
        self.c1.set(self.cosmetic_tax)
        self.c2.set(self.grocery_tax)
        self.c3.set(self.drink_tax)
        
        self.Total=float(self.total_cosmetic+
                             self.total_grocery+
                             self.total_drink+
                             self.cosmetic_tax+
                             self.grocery_tax+
                             self.drink_tax)
                            
    # bill area  
    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\tBROGRAMMERS Super Mart Retail\n")
        self.textarea.insert(END,f"\nBill Number : {self.cbill.get()}")
        self.textarea.insert(END,f"\nCustomer Name :{self.cname.get()} ")
        self.textarea.insert(END,f"\nPhone Number :{self.cphone.get()}")
        self.textarea.insert(END,f"\n-------------------------------------------")
        self.textarea.insert(END,f"\n  Product\t\t       Qty\t\t  Price")
        self.textarea.insert(END,f"\n-------------------------------------------")
        
    
    def bill_area(self):
        if self.cname.get()=="" or self.cphone.get()=="":                               #Validation.
            messagebox.showerror("Error","Customer Details must be filled!")
        elif self.m1.get()=="0.0" and self.m2.get()=="0.0" and self.m3.get()=="0.0":
            messagebox.showerror("Error","No Products Choosen!")
        else:
            self.welcome_bill()               # Bill Area se welcome_bill ko call kia g hai.
            #----Cosmetics----
            if self.bath.get()!=0:
                self.textarea.insert(END,f"\n Bath Soap\t\t\t {self.bath.get()}\t {self.bath_price}")
            if self.face_cream.get()!=0:
                self.textarea.insert(END,f"\n Face Cream\t\t\t {self.face_cream.get()}\t {self.face_cream_price}")
            if self.face_wash.get()!=0:
                self.textarea.insert(END,f"\n Face Wash\t\t\t {self.face_wash.get()}\t {self.face_wash_price}")
            if self.hair_shampoo.get()!=0:
                self.textarea.insert(END,f"\n Hair Shampoo\t\t\t {self.hair_shampoo.get()}\t {self.hair_shampoo_price}")
            if self.hair_gel.get()!=0:
                self.textarea.insert(END,f"\n Hair Gel\t\t\t {self.hair_gel.get()}\t {self.hair_gel_price}")
            if self.body_lotion.get()!=0:
                self.textarea.insert(END,f"\n Body Lotion\t\t\t {self.body_lotion.get()}\t {self.body_lotion_price}")
                
             #----Groceriess----
            if self.rice.get()!=0:
                self.textarea.insert(END,f"\n Rice\t\t\t {self.rice.get()}\t {self.rice_price}")
            if self.food_oil.get()!=0:
                self.textarea.insert(END,f"\n Food Oil\t\t\t {self.food_oil.get()}\t {self.food_oil_price}")
            if self.pulses.get()!=0:
                self.textarea.insert(END,f"\n Pulses\t\t\t {self.pulses.get()}\t {self.pulses_price}")
            if self.wheat.get()!=0:
                self.textarea.insert(END,f"\n Wheat Flour\t\t\t {self.wheat.get()}\t {self.wheat_price}")
            if self.sugar.get()!=0:
                self.textarea.insert(END,f"\n Sugar\t\t\t {self.sugar.get()}\t {self.sugar_price}")
            if self.tea.get()!=0:
                self.textarea.insert(END,f"\n Tea\t\t\t {self.tea.get()}\t {self.tea_price}")
                
            #---Drinks----
            if self.roohAfza.get()!=0:
                self.textarea.insert(END,f"\n RoohAfza\t\t\t {self.roohAfza.get()}\t {self.roohAfza_price}")
            if self.milkShake.get()!=0:
                self.textarea.insert(END,f"\n Milk Shake\t\t\t {self.milkShake.get()}\t {self.milkShake_price}")
            if self.rasna.get()!=0:
                self.textarea.insert(END,f"\n Rasna\t\t\t {self.rasna.get()}\t {self.rasna_price}")
            if self.coke.get()!=0:
                self.textarea.insert(END,f"\n Coke/Coke Diet\t\t\t {self.coke.get()}\t {self.coke_price}")
            if self.maaza.get()!=0:
                self.textarea.insert(END,f"\n Maaza\t\t\t {self.maaza.get()}\t {self.maaza_price}")
            if self.lemonades.get()!=0:
                self.textarea.insert(END,f"\n Lemonades\t\t\t {self.lemonades.get()}\t {self.lemonades_price}")
            
       
            self.textarea.insert(END,f"\n-------------------------------------------")
            if self.c1.get()!="0.0":
                self.textarea.insert(END,f"\n Cosmetic Tax\t\t\t {self.cosmetic_tax}")
            if self.c2.get()!="0.0":
                self.textarea.insert(END,f"\n Grocery Tax\t\t\t {self.grocery_tax}")
            if self.c3.get()!="0.0":
                    self.textarea.insert(END,f"\n Drinks Tax\t\t\t {self.drink_tax}")
            self.textarea.insert(END,f"\n-------------------------------------------")  
        
        
           
            self.textarea.insert(END,f"\n Total Bill :\t\t\t\t Rs.{self.Total}")
            self.textarea.insert(END,f"\n-------------------------------------------")
            
            #self.textarea.config(state=DISABLED)      # To make the Textarea uneditable.
            self.save_bill()
            
    # save bill function will be called by save button
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you wish to save the Bill!")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END) # We also must specify the from which position to which, is the data needs to be fetched as arguments in get().
            f1=open("Bill_data"+str(self.cbill.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No. {self.cbill.get()} saved successfully!")
        else:
            return
        
    
    def find_bill(self):
        #for i in os.listdir("Bill_data/"):
        #    print(i)
        try:
            f1=open("Bill_data"+str(self.search_bill.get())+".txt","r")
            data=f1.read()
            self.textarea.delete('1.0',END)
            self.textarea.insert(END,data)
            f1.close()
        except FileNotFoundError:
            messagebox.showerror("Error","Invalid Bill Number!")
        except:
            print("oops")
            
            
    def reset(self):
        op=messagebox.askyesno("Reset","Do you wish to clear data!")
        if op>0:
            # *********Cosmetics***********
            self.bath.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.hair_gel.set(0)
            self.hair_shampoo.set(0)
            self.body_lotion.set(0)
        
            # *********Groceries***********
        
            self.rice.set(0)
            self.food_oil.set(0)
            self.pulses.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
        
            # *********Drinks***********
        
            self.roohAfza.set(0)
            self.milkShake.set(0)
            self.rasna.set(0)
            self.coke.set(0)
            self.maaza.set(0)
            self.lemonades.set(0)
        
            # *********Total Price and Tax Variables***********
            self.m1.set("")
            self.m2.set("")
            self.m3.set("")
        
            self.c1.set("")
            self.c2.set("")
            self.c3.set("")
        
            #************Customer Variables****************
        
            self.cname.set("")
            self.cphone.set("")
            self.cbill.set("")
            x=random.randint(1000,9999)
            self.cbill.set(str(x))
            self.search_bill.set("")
        
            self.welcome_bill()
            
        else:
            return
         
        
    def exit(self):
        op=messagebox.askyesno("Exit","Do you really want to exit!")
        if op>0:
            self.root.destroy()
        else:
            return

root=Tk()
obj=Bill_App(root)
root.mainloop()

