from tkinter import*
import time
import datetime
import pygame
import sys
import random
import tkinter.messagebox

pygame.init()
root = Tk()
root.geometry("1600x800+0+0")
root.title("Salse Management System")
root.configure(background='white')

# ==================Frame======================================
ABC = Frame(root, bg="blue", bd=20, relief=RIDGE)
ABC.grid()
ABC1 = Frame(ABC, bg="Cadet Blue", bd=10, relief=RIDGE)
ABC1.grid(row=0, column=0, columnspan=4, sticky=W)
ABC2 = Frame(ABC, bg="powder blue", bd=10, relief=RIDGE)
ABC2.grid(row=1, column=1, sticky=W)
ABC3 = Frame(ABC, bg="powder blue", bd=10, relief=RIDGE)
ABC3.grid(row=1, column=0, sticky=W)
ABC4 = Frame(ABC, bg="blue", bd=10, relief=RIDGE)
ABC4.grid(row=1, column=2, sticky=W)
ABC5 = Frame(ABC4, bg="blue", bd=10, relief=RIDGE)
ABC5.grid(row=0, column=0, sticky=W)
ABC6 = Frame(ABC4, bg="blue", bd=10, relief=RIDGE)
ABC6.grid(row=1, column=0, columnspan=4, sticky=W)

# ==================Variables======================================
Date1 = StringVar()
Time1 = StringVar()
Receipt_Ref = StringVar()
Tax = StringVar()
SubTotal = StringVar()
Total = StringVar()

JeansJeggers = StringVar()
CoatsJackets = StringVar()
SportWear = StringVar()
Shirts = StringVar()
Dressess = StringVar()
Skirts = StringVar()
Swimwer = StringVar()
SchoolUniform = StringVar()
Payjama = StringVar()

Jackets_Blazer = StringVar()
Formal_Trousers = StringVar()
Formal_Shirts = StringVar()
Mens_Boots = StringVar()
Bed_Sheet = StringVar()
Pillows_Cases = StringVar()
Patterned_Bedding = StringVar()
Mattress_Protectors = StringVar()
Knife = StringVar()

JeansJeggers.set(0)
CoatsJackets.set(0)
SportWear.set(0)
Shirts.set(0)
Dressess.set(0)
Skirts.set(0)
Swimwer.set(0)
SchoolUniform.set(0)
Payjama.set(0)

Jackets_Blazer.set(0)
Formal_Trousers.set(0)
Formal_Shirts.set(0)
Mens_Boots.set(0)
Bed_Sheet.set(0)
Pillows_Cases.set(0)
Patterned_Bedding.set(0)
Mattress_Protectors.set(0)
Knife.set(0)

# ==================Date and time======================================
Date1.set(time.strftime("%d/%m/%y"))
Time1.set(time.strftime("%H:%M:%S"))
# ==================Function Declaration======================================


def iExit():
    iExit = tkinter.messagebox.askyesno(
        "Salse Management System", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return


def Reset():
    txtReceipt.delete("1.0", END)
    JeansJeggers.set(0)
    CoatsJackets.set(0)
    SportWear.set(0)
    Shirts.set(0)
    Dressess.set(0)
    Skirts.set(0)
    Swimwer.set(0)
    SchoolUniform.set(0)
    Payjama.set(0)

    Jackets_Blazer.set(0)
    Formal_Trousers.set(0)
    Formal_Shirts.set(0)
    Mens_Boots.set(0)
    Bed_Sheet.set(0)
    Pillows_Cases.set(0)
    Patterned_Bedding.set(0)
    Mattress_Protectors.set(0)
    Knife.set(0)


def Total():
    Item1 = float(JeansJeggers.get())
    Item2 = float(CoatsJackets.get())
    Item3 = float(SportWear.get())
    Item4 = float(Shirts.get())
    Item5 = float(Dressess.get())
    Item6 = float(Skirts.get())
    Item7 = float(Swimwer.get())
    Item8 = float(SchoolUniform.get())
    Item9 = float(Payjama.get())

    Item10 = float(Jackets_Blazer.get())
    Item11 = float(Formal_Trousers.get())
    Item12 = float(Formal_Shirts.get())
    Item13 = float(Mens_Boots.get())
    Item14 = float(Bed_Sheet.get())
    Item15 = float(Pillows_Cases.get())
    Item16 = float(Patterned_Bedding.get())
    Item17 = float(Mattress_Protectors.get())
    Item18 = float(Knife.get())

    PriceofItem1 = ("Tk") + str('%.2f' % (Item1 * 400))
    PriceofItem2 = ("Tk") + str('%.2f' % (Item2 * 500))
    PriceofItem3 = ("Tk") + str('%.2f' % (Item3 * 700))
    PriceofItem4 = ("Tk") + str('%.2f' % (Item4 * 1000))
    PriceofItem5 = ("Tk") + str('%.2f' % (Item5 * 900))
    PriceofItem6 = ("Tk") + str('%.2f' % (Item6 * 300))
    PriceofItem7 = ("Tk") + str('%.2f' % (Item7 * 600))
    PriceofItem8 = ("Tk") + str('%.2f' % (Item8 * 700))
    PriceofItem9 = ("Tk") + str('%.2f' % (Item9 * 200))
    PriceofItem10 = ("Tk") + str('%.2f' % (Item10 * 100))
    PriceofItem11 = ("Tk") + str('%.2f' % (Item11 * 490))
    PriceofItem12 = ("Tk") + str('%.2f' % (Item12 * 350))
    PriceofItem13 = ("Tk") + str('%.2f' % (Item13 * 480))
    PriceofItem14 = ("Tk") + str('%.2f' % (Item14 * 650))
    PriceofItem15 = ("Tk") + str('%.2f' % (Item15 * 990))
    PriceofItem16 = ("Tk") + str('%.2f' % (Item16 * 250))
    PriceofItem17 = ("Tk") + str('%.2f' % (Item17 * 690))
    PriceofItem18 = ("Tk") + str('%.2f' % (Item18 * 100))

    PriceofWomen = (Item1 * 400) + (Item2 * 500) + \
        (Item3 * 700)+(Item4 * 1000)+(Item5 * 900)
    PriceofKids = (Item6 * 300)+(Item7 * 600)+(Item8 * 700)+(Item9 * 200)
    PriceofMen = (Item10 * 100)+(Item11 * 490) + \
        (Item12 * 350)+(Item13 * 480)+(Item14 * 650)
    PriceofHomeware = (Item15 * 990)+(Item16 * 250) + \
        (Item17 * 690)+(Item18 * 100)

    SubTotalofITEMS = ("Tk")+str('%.2f' %
                                 (PriceofWomen+PriceofKids+PriceofMen+PriceofHomeware))
    iTax = ("Tk")+str('%.2f' %
                      ((PriceofWomen+PriceofKids+PriceofMen+PriceofHomeware)*0.15))

    TT = (PriceofWomen+PriceofKids+PriceofMen+PriceofHomeware)
    TC = (((PriceofWomen+PriceofKids+PriceofMen+PriceofHomeware)*0.15))
    TotalCost = ("Tk")+str('%.2f' % (TT + TC))

    txtReceipt.delete("1.0", END)
    x = random.randint(10747, 500298)
    randomRef = str(x)
    Receipt_Ref.set("BILL"+randomRef)

    txtReceipt.insert(END, 'Receipt Ref:\t\t\t\t'+Receipt_Ref.get() +
                      '\n' + Date1.get()+'\t\t\t\t' + Time1.get() + '\n')
    txtReceipt.insert(
        END, '---------------------------------------------------------------------------------------')
    txtReceipt.insert(END, 'Item:\t\t\t\t'+"Cost of Items:"'\n')
    txtReceipt.insert(
        END, '---------------------------------------------------------------------------------------')
    txtReceipt.insert(END, 'Jeans Jeggers:\t\t\t\t'+PriceofItem1+"\n")
    txtReceipt.insert(END, 'Coats Jackets:\t\t\t\t'+PriceofItem2+"\n")
    txtReceipt.insert(END, 'Sportwear:\t\t\t\t'+PriceofItem3+"\n")
    txtReceipt.insert(END, 'Dresses:\t\t\t\t'+PriceofItem4+"\n")
    txtReceipt.insert(END, 'Shirts:\t\t\t\t'+PriceofItem5+"\n")
    txtReceipt.insert(END, 'Skirts:\t\t\t\t'+PriceofItem6+"\n")
    txtReceipt.insert(END, 'Swimwear:\t\t\t\t'+PriceofItem17+"\n")
    txtReceipt.insert(END, 'School Uniform:\t\t\t\t'+PriceofItem8+"\n")
    txtReceipt.insert(END, 'Pyjama:\t\t\t\t'+PriceofItem9+"\n")
    txtReceipt.insert(END, 'Jackets Blazers:\t\t\t\t'+PriceofItem10+"\n")
    txtReceipt.insert(END, 'Formal Trousers:\t\t\t\t'+PriceofItem11+"\n")
    txtReceipt.insert(END, 'Formal Shirts:\t\t\t\t'+PriceofItem12+"\n")
    txtReceipt.insert(END, 'Mens Boots:\t\t\t\t'+PriceofItem13+"\n")
    txtReceipt.insert(END, 'Bed Sheet:\t\t\t\t'+PriceofItem14+"\n")
    txtReceipt.insert(END, 'Pillows Cases:\t\t\t\t'+PriceofItem15+"\n")
    txtReceipt.insert(END, 'Patterned Bedding:\t\t\t\t'+PriceofItem16+"\n")
    txtReceipt.insert(END, 'Mattress Protectors:\t\t\t\t'+PriceofItem17+"\n")
    txtReceipt.insert(END, 'Knife:\t\t\t\t'+PriceofItem18+"\n")
    txtReceipt.insert(END, 'Tax Paid:\t\t\t\t'+iTax+"\n")
    txtReceipt.insert(END, 'SubTotal:\t\t\t\t'+SubTotalofITEMS+"\n")
    txtReceipt.insert(END, 'Total Cost:\t\t\t\t'+TotalCost+"\n")
# ==================frame======================================


lblDate = Label(ABC1, textvariable=Date1, font=('arial', 30, 'bold'), padx=46, pady=75,
                bd=5, bg="cadet Blue", fg="Cornsilk").grid(row=0, column=0)

lblTitle = Label(ABC1, text="\tSalse Management System\t", font=('arial', 30, 'bold'), padx=46, pady=75,
                 bd=14, bg="cadet Blue", fg="Cornsilk", justify=CENTER).grid(row=0, column=1)

lblTime = Label(ABC1, textvariable=Time1,  font=('arial', 30, 'bold'), padx=46, pady=75,
                bd=5, bg="cadet Blue", fg="Cornsilk").grid(row=0, column=2)
# ==================Labels and text Entry======================================
lblWomen = Label(ABC2, text="Women", font=('arial', 20, 'bold'), pady=1, bd=8, bg="black",
                 fg="Cornsilk", width=25, justify=CENTER).grid(row=0, column=0, columnspan=4)
lblJeansJeggers = Label(ABC2, text="Jeans & Jeggers", bg="powder blue", font=(
    'arial', 18), justify=LEFT).grid(row=1, column=0, sticky=W)
lblCoatsJackets = Label(ABC2, text="Coats & Jackets ", bg="powder blue", font=(
    'arial', 18), justify=LEFT).grid(row=2, column=0, sticky=W)
lblSportWear = Label(ABC2, text="SportWear", bg="powder blue", font=(
    'arial', 18), justify=LEFT).grid(row=3, column=0, sticky=W)
lblShirts = Label(ABC2, text="Shirts", bg="powder blue", font=(
    'arial', 18), justify=LEFT).grid(row=4, column=0, sticky=W)
lblDressess = Label(ABC2, text="Dressess", bg="powder blue", font=(
    'arial', 18), justify=LEFT).grid(row=5, column=0, sticky=W)
lblKids = Label(ABC2, text="Kids", font=('arial', 20, 'bold'), pady=1, bd=8, bg="black",
                fg="Cornsilk", width=25, justify=CENTER).grid(row=6, column=0, columnspan=4)
lblSkirts = Label(ABC2, text="Skirts ", bg="powder blue", font=(
    'arial', 18), justify=LEFT).grid(row=7, column=0, sticky=W)
lblSwimwer = Label(ABC2, text="Swimwer", bg="powder blue", font=(
    'arial', 18), justify=LEFT).grid(row=8, column=0, sticky=W)
lblSchoolUniform = Label(ABC2, text="School Uniform", bg="powder blue", font=(
    'arial', 18), justify=LEFT).grid(row=9, column=0, sticky=W)
lblPayjama = Label(ABC2, text="Payjama & Dressing", bg="powder blue", font=(
    'arial', 18), justify=LEFT).grid(row=10, column=0, sticky=W)
# ==================TEXT Entry======================================
txtJeansJeggers = Entry(ABC2, textvariable=JeansJeggers, font=('arial', 16, 'bold'),  bd=8, bg="powder blue",
                        fg="black", width=12, justify=CENTER).grid(row=1, column=1, pady=1)
txtCoatsJackets = Entry(ABC2, textvariable=CoatsJackets, font=('arial', 16, 'bold'),  bd=8, bg="powder blue",
                        fg="black", width=12, justify=CENTER).grid(row=2, column=1, pady=1)
txtSportWea = Entry(ABC2, textvariable=SportWear, font=('arial', 16, 'bold'),  bd=8, bg="powder blue",
                    fg="black", width=12, justify=CENTER).grid(row=3, column=1, pady=1)
txtShirts = Entry(ABC2, textvariable=Shirts, font=('arial', 16, 'bold'),  bd=8, bg="powder blue",
                  fg="black", width=12, justify=CENTER).grid(row=4, column=1, pady=1)
txtDressess = Entry(ABC2, textvariable=Dressess, font=('arial', 16, 'bold'),  bd=8, bg="powder blue",
                    fg="black", width=12, justify=CENTER).grid(row=5, column=1, pady=1)
txtSkirts = Entry(ABC2, textvariable=Skirts, font=('arial', 16, 'bold'),  bd=8, bg="powder blue",
                  fg="black", width=12, justify=CENTER).grid(row=7, column=1, pady=1)
txtSwimwer = Entry(ABC2, textvariable=Swimwer, font=('arial', 16, 'bold'),  bd=8, bg="powder blue",
                   fg="black", width=12, justify=CENTER).grid(row=8, column=1, pady=1)
txtSchoolUniform = Entry(ABC2, textvariable=SchoolUniform, font=('arial', 16, 'bold'),  bd=8, bg="powder blue",
                         fg="black", width=12, justify=CENTER).grid(row=9, column=1, pady=1)
txtPayjama = Entry(ABC2, textvariable=Payjama, font=('arial', 16, 'bold'),  bd=8, bg="powder blue",
                   fg="black", width=12, justify=CENTER).grid(row=10, column=1, pady=1)
# ========================================================================================================
# ==================Labels and text Entry======================================
lblmen = Label(ABC3, text="Men", font=('arial', 20, 'bold'), pady=1, bd=8, bg="black",
               fg="Cornsilk", width=25, justify=CENTER).grid(row=0, column=0, columnspan=4)
lblJackets_Blazer = Label(ABC3, text="Jackets Blazer", bg="powder blue", font=(
    'arial', 18), justify=LEFT).grid(row=1, column=0, sticky=W)
lblFormal_Trousers = Label(ABC3, text="Formal Trousers ", bg="powder blue", font=(
    'arial', 18), justify=LEFT).grid(row=2, column=0, sticky=W)
lblFormal_Shirts = Label(ABC3, text="Formal Shirts", bg="powder blue", font=(
    'arial', 18), justify=LEFT).grid(row=3, column=0, sticky=W)
lblMens_Boots = Label(ABC3, text="Mens Boots", bg="powder blue", font=(
    'arial', 18), justify=LEFT).grid(row=4, column=0, sticky=W)
lblBed_Sheet = Label(ABC3, text="Bed Sheet", bg="powder blue", font=(
    'arial', 18), justify=LEFT).grid(row=5, column=0, sticky=W)
lblHoeware = Label(ABC3, text="Hoeware", font=('arial', 20, 'bold'), pady=1, bd=8, bg="black",
                   fg="Cornsilk", width=25, justify=CENTER).grid(row=6, column=0, columnspan=4)
lblPillows_Cases = Label(ABC3, text="Pillows Cases ", bg="powder blue", font=(
    'arial', 18), justify=LEFT).grid(row=7, column=0, sticky=W)
lblPatterned_Bedding = Label(ABC3, text="Patterned Bedding", bg="powder blue", font=(
    'arial', 18), justify=LEFT).grid(row=8, column=0, sticky=W)
lblMattress_Protectors = Label(ABC3, text="Mattress Protectors", bg="powder blue", font=(
    'arial', 18), justify=LEFT).grid(row=9, column=0, sticky=W)
lblKnife = Label(ABC3, text="Knife", bg="powder blue", font=(
    'arial', 18), justify=LEFT).grid(row=10, column=0, sticky=W)
# ==================TEXT Entry======================================
txtJackets_Blazer = Entry(ABC3, textvariable=Jackets_Blazer, font=('arial', 16, 'bold'),  bd=8, bg="powder blue",
                          fg="black", width=12, justify=CENTER).grid(row=1, column=1, pady=1)
txtFormal_Trousers = Entry(ABC3, textvariable=Formal_Trousers, font=('arial', 16, 'bold'),  bd=8, bg="powder blue",
                           fg="black", width=12, justify=CENTER).grid(row=2, column=1, pady=1)
txtFormal_Shirts = Entry(ABC3, textvariable=Formal_Shirts, font=('arial', 16, 'bold'),  bd=8, bg="powder blue",
                         fg="black", width=12, justify=CENTER).grid(row=3, column=1, pady=1)
txtMens_Boots = Entry(ABC3, textvariable=Mens_Boots, font=('arial', 16, 'bold'),  bd=8, bg="powder blue",
                      fg="black", width=12, justify=CENTER).grid(row=4, column=1, pady=1)
txtBed_Sheet = Entry(ABC3, textvariable=Bed_Sheet, font=('arial', 16, 'bold'),  bd=8, bg="powder blue",
                     fg="black", width=12, justify=CENTER).grid(row=5, column=1, pady=1)
txtPillows_Cases = Entry(ABC3, textvariable=Pillows_Cases, font=('arial', 16, 'bold'),  bd=8, bg="powder blue",
                         fg="black", width=12, justify=CENTER).grid(row=7, column=1, pady=1)
txtPatterned_Bedding = Entry(ABC3, textvariable=Patterned_Bedding, font=('arial', 16, 'bold'),  bd=8, bg="powder blue",
                             fg="black", width=12, justify=CENTER).grid(row=8, column=1, pady=1)
txtMattress_Protectors = Entry(ABC3, textvariable=Mattress_Protectors, font=('arial', 16, 'bold'),  bd=8, bg="powder blue",
                               fg="black", width=12, justify=CENTER).grid(row=9, column=1, pady=1)
txtKnife = Entry(ABC3, textvariable=Knife, font=('arial', 16, 'bold'),  bd=8, bg="powder blue",
                 fg="black", width=12, justify=CENTER).grid(row=10, column=1, pady=1)
# ==================TEXT ======================================
txtReceipt = Text(ABC5, height=24, width=50, bd=20, font=('arial', 9, 'bold'))
txtReceipt.grid(row=0, column=0)
# ==================Button ======================================
btnTotal = Button(ABC6, command=Total, padx=1, pady=1, bd=4, fg="black", font=(
    'arial', 16, 'bold'), width=9, bg="powder blue", text="Total").grid(row=0, column=0)
btnReset = Button(ABC6, command=Reset, padx=1, pady=1, bd=4, fg="black", font=(
    'arial', 16, 'bold'), width=9, bg="powder blue", text="Reset").grid(row=0, column=1)
btnExit = Button(ABC6, command=iExit, padx=1, pady=1, bd=4, fg="black", font=(
    'arial', 16, 'bold'), width=9, bg="powder blue", text="Exit").grid(row=0, column=2)

root.mainloop()
