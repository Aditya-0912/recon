from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Employee
import pandas as pd
# import pyodbc
import numpy as np
import os
from tkinter.filedialog import askopenfilename, asksaveasfilename

import tkinter as tk
from tkinter import messagebox
# from .forms import FilterForm
from .models import  reco_data
from .models import  merchant_data
from pandas import DataFrame
from .models import transaction_data
from django.db import  connection
filepath=""
gb_value=""

class Index(LoginRequiredMixin, View):
    template = 'index.html'
    login_url = '/login/'
    
    def get(self, request):
        employees = Employee.objects.all()
        return render(request, self.template, {'employees': employees})


class Login(View):
    template = 'login.html'
    
    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, self.template, {'form': form})

def open_file(request):
    dd_value=request.session['ddvalue']

    window = tk.Tk()
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.csv"), ("All Files", "*.*")]
    )           
    window.title(f"Simple Text Editor - {filepath}")  
    data_1=pd.read_csv(filepath)
    

    # data_1=pd.read_csv(r"C:\Temp\san\KritungaOnlineSales.csv")
    # data_2=pd.read_csv(r"C:\Temp\san\Kritunga_order-transactions.csv")

    df1 = pd.DataFrame(data_1)
    df1.replace([np.inf, -np.inf], np.nan, inplace = True)
    df1 = df1.fillna(0)
    print(df1.head())

    if(dd_value=="1"):
        del_merchantdata=merchant_data.objects.get_queryset()
        for del2 in del_merchantdata:
            del2.delete()
    elif (dd_value=="2"):
        del_transactiondata=transaction_data.objects.get_queryset()
        for del2 in del_transactiondata:
            del2.delete()

    # del_merchantdata=merchant_data.objects.get_queryset()
    # for del2 in del_merchantdata:
    #     del2.delete()

    # del_transactiondata=transaction_data.objects.get_queryset()
    # for del2 in del_transactiondata:
    #     del2.delete()

    
    if(dd_value=="1"):
        for index, row in df1.iterrows():
            model_merchantdata = merchant_data()

            model_merchantdata.branch_name = row['branchName']
            model_merchantdata.branch_Code = row['branchCode']
            model_merchantdata.Business_Date = row['BusinessDate']
            model_merchantdata.ReceiptNo = row['ReceiptNo']
            model_merchantdata.ReferenceID = row['ReferenceID']
            model_merchantdata.OrderId = row['OrderId']
            model_merchantdata.ProfitCenterType = row['ProfitCenterType']
            model_merchantdata.comments = row['comments']
            model_merchantdata.entry_date = row['entry_date']
            model_merchantdata.net_amount = row['net_amount']

            model_merchantdata.save()

    elif (dd_value=="2"):
        for index, row in df1.iterrows():
            model_transactiondata = transaction_data()

            model_transactiondata.ID_No = row['ID']
            model_transactiondata.Order_ref_ID = row['Order_ref_ID']
            model_transactiondata.External_Platform_ID = row['External_Platform_ID']
            model_transactiondata.Channel = row['Channel']
            model_transactiondata.Created_Date = row['Created_At']
            model_transactiondata.Order_State = row['Order_State']
            model_transactiondata.Request_Delivery_Time = row['Request_Delivery_Time']
            model_transactiondata.Time_Slot_Start = row['Time_Slot_Start']
            model_transactiondata.Time_Slot_End = row['Time_Slot_End']
            model_transactiondata.Payment_Mode = row['Payment_Mode']
            model_transactiondata.Payment_Transaction_ID = row['Payment_Transaction_ID']
            model_transactiondata.Customer_Name = row['Customer_Name']
            model_transactiondata.Customer_ID = row['Customer_ID']
            model_transactiondata.Store_Name = row['Store_Name']
            model_transactiondata.Store_ID = row['Store_ID']
            model_transactiondata.Store_ref_ID = row['Store_ref_ID']
            model_transactiondata.Total_Amount = row['Total_Amount']
            model_transactiondata.Merchant_Total = row['Merchant_Total']
            model_transactiondata.Sub_total_Amount = row['Sub_total_Amount']
            model_transactiondata.Discount = row['Discount']
            model_transactiondata.Aggregator_Discount = row['Aggregator_Discount']
            model_transactiondata.Merchant_Discount = row['Merchant_Discount']
            model_transactiondata.Taxes = row['Taxes']
            model_transactiondata.Charges = row['Charges']
            model_transactiondata.Fulfillment_mode = row['Fulfillment_mode']
            model_transactiondata.Wallet_credit_amount = row['Wallet_credit_amount']
            model_transactiondata.City = row['City']

            model_transactiondata.save()
    # data=pd.read_excel(filepath,engine='openpyxl')    
    # df = pd.DataFrame(data, columns= ['Quick_Report','credit','Debit'])
    # df.replace([np.inf, -np.inf], np.nan, inplace = True)
    # df = df.fillna(0)
    # print(df.head())
    # conn = pyodbc.connect('Driver={SQL Server};'
    #                       'Server=IN-5CD0129158;'
    #                       'Database=Recon;'
    #                       'Trusted_Connection=yes;'
    #                       'username=cscmws\akumar988;')
    # cursor = conn.cursor()
    # if(dd_value=="1"):
    #     cursor.execute("delete from Merchant_data")
    # elif (dd_value=="2"):
    #     cursor.execute("delete from transaction_data")
    # for index, row in df1.iterrows():
    #     if(dd_value=="1"):
            
    #         cursor.execute("INSERT INTO Merchant_data (branch_name,branch_Code,Business_Date,ReceiptNo,ReferenceID,OrderId,ProfitCenterType,comments,entry_date,net_amount) values(?,?,?,?,?,?,?,?,?,?)", row.branchName, row.branchCode, row.BusinessDate,row.ReceiptNo,row.ReferenceID,row.OrderId,row.ProfitCenterType,row.comments,row.entry_date,row.net_amount)
            
    #     # cursor.execute("INSERT INTO Recon_Master (Quick_Report,Credit_Data,Debit_Card) values(?,?,?)", row.Quick_Report, row.credit, row.Debit)
    #     elif(dd_value=="2"):
            
    #         cursor.execute("INSERT INTO transaction_data (ID_No,Order_ref_ID,External_Platform_ID,Channel,Created_Date,Order_State,Request_Delivery_Time,Time_Slot_Start,Time_Slot_End,Payment_Mode,Payment_Transaction_ID,Customer_Name,Customer_ID,Store_Name,Store_ID,Store_ref_ID,Total_Amount,Merchant_Total,Sub_total_Amount,Discount,Aggregator_Discount,Merchant_Discount,Taxes,Charges,Fulfillment_mode,Wallet_credit_amount,City) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row.ID,row.Order_ref_ID,row.External_Platform_ID,row.Channel,row.Created_At,row.Order_State,row.Request_Delivery_Time,row.Time_Slot_Start,row.Time_Slot_End	,row.Payment_Mode,row.Payment_Transaction_ID,row.Customer_Name,row.Customer_ID,row.Store_Name,row.Store_ID,row.Store_ref_ID,row.Total_Amount,row.Merchant_Total	,row.Sub_total_Amount,row.Discount,row.Aggregator_Discount,row.Merchant_Discount,row.Taxes,row.Charges,row.Fulfillment_mode,row.Wallet_credit_amount,row.City)
    # conn.commit()
    # cursor.close()
    # tk.messagebox.showinfo("showinfo", "Data has been successfully uploaded")
    # tk.messagebox.showinfo("showinfo", gb_value)
    
    # print("this is data dump:" + dd_value)
    window.destroy()
    # return HttpResponseRedirect('/')
    y="*File uploaded Successfully !! Pls choose another file to upload"
    
    return render(request,"index.html",{'matched_data':y})
    return HttpResponseRedirect('/')

def ddlist(request):
    # root = tk.Tk()
    # root.withdraw()    
    answer = request.GET['ddlist']  
    # print('this is user selection',answer)
    request.session['ddvalue'] = answer
    # gb_value=answer
    # tk.messagebox.showinfo("showinfo", answer)
    # tk.messagebox.showinfo("showinfo", gb_value)
    
    # print("this is drop down:" + gb_value)
    # return gb_value
    
    
    # HttpResponse(simplejson.dumps({"success" : "true", "message" : ... }, mimetype = "application/json"))  
    return HttpResponseRedirect('/')

def reco_details(request):
    del1=reco_data.objects.get_queryset()
    for del2 in del1:
        del2.delete()
    
    # conn = pyodbc.connect('Driver={SQL Server};'
    #                       'Server=IN-5CD0129158;'
    #                       'Database=Recon;'
    #                       'Trusted_Connection=yes;'
    #                       'username=cscmws\akumar988;')
    # cursor = conn.cursor()
    
    # matched_data=pd.read_sql_query('select count( *) from [Merchant_data] t1 inner join [transaction_data] t2 on t1.ReferenceID=t2.Order_ref_ID where t1.net_amount<>t2.Total_Amount',conn)
 

    
    # sql_query = pd.read_sql_query('select t1.* from [Merchant_data] t1 inner join [transaction_data] t2 on t1.ReferenceID=t2.Order_ref_ID where t1.net_amount<>t2.Total_Amount',conn)
    
    # print("this is unmatched data details", matched_data.head())
    # print(type(matched_data))
    # sql_query1=merchant_data.objects.all().values()
    # sql_query2=transaction_data.objects.all().values()
    # sql_query3=sql_query1.select_related(sql_query2)

    cursor=connection.cursor()
    #below code worksfor mysql
    # cursor.execute('select t1.* from recoso_db.core_Merchant_data t1 inner join recoso_db.core_transaction_data t2 on t1.ReferenceID=t2.Order_ref_ID where t1.net_amount<>t2.Total_Amount')
    cursor.execute('select t1.* from core_Merchant_data t1 inner join core_transaction_data t2 on t1."ReferenceID"=t2."Order_ref_ID" where t1.net_amount<>t2."Total_Amount"')
    sql_query=cursor.fetchall()
    cursor.execute('select count(t1.*) from core_Merchant_data t1 inner join core_transaction_data t2 on t1."ReferenceID"=t2."Order_ref_ID" where t1.net_amount<>t2."Total_Amount"')
    count_query=cursor.fetchall()
    # sql_query.append(count_query)
    print(count_query)
    # print('this is final data',sql_query)
    # for index, row in sql_query.iterrows():
    # for  row in sql_query:
    #     model = reco_data()
    #     model.Reference_ID = row['ReferenceID']
    #     model.Receipt_No = row['ReceiptNo']
    #     model.Order_ID = row['OrderId']
    #     model.Branch_name = row['branch_name']
    #     model.Branch_code = row['branch_Code']
    #     model.Transaction_date = row['entry_date']
    #     model.Channel_Partner = row['ProfitCenterType']
    #     model.Amount = row['net_amount']
    #     model.unmatched_data_count=len(sql_query)
    #     model.save()

    # all_data=reco_data.objects.all()

    return render(request,"index.html",{'aldata':sql_query,'countdata':count_query})
    # return render(request,"index.html",context)
    # {'aldata':all_data},