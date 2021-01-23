from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    office = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    start_date = models.DateField()
    salary = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class reco_data(models.Model):
    Reference_ID = models.CharField(max_length=150)
    Receipt_No = models.CharField(max_length=150)
    Order_ID = models.CharField(max_length=150)
    Branch_name = models.CharField(max_length=150)
    Branch_code = models.CharField(max_length=150)
    Transaction_date = models.CharField(max_length=150)
    Channel_Partner =models.CharField(max_length=150)
    Amount =models.CharField(max_length=150)
    unmatched_data_count=models.CharField(max_length=150)

class merchant_data(models.Model):
    branch_name = models.CharField(max_length=150)
    branch_Code = models.CharField(max_length=150)
    Business_Date = models.CharField(max_length=150)
    ReceiptNo = models.CharField(max_length=150)
    ReferenceID = models.CharField(max_length=150)
    OrderId = models.CharField(max_length=150)
    ProfitCenterType =models.CharField(max_length=150)
    comments =models.CharField(max_length=150)
    entry_date =models.CharField(max_length=150)
    net_amount =models.CharField(max_length=150)

class transaction_data(models.Model):
    ID_No = models.CharField(max_length=150)
    Order_ref_ID = models.CharField(max_length=150)
    External_Platform_ID = models.CharField(max_length=150)
    Channel = models.CharField(max_length=150)
    Created_Date = models.CharField(max_length=150)
    Order_State = models.CharField(max_length=150)
    Request_Delivery_Time =models.CharField(max_length=150)
    Time_Slot_Start =models.CharField(max_length=150)
    Time_Slot_End =models.CharField(max_length=150)
    Payment_Mode =models.CharField(max_length=150)
    Payment_Transaction_ID =models.CharField(max_length=150)
    Customer_Name =models.CharField(max_length=150)
    Customer_ID =models.CharField(max_length=150)
    Store_Name =models.CharField(max_length=150)
    Store_ID =models.CharField(max_length=150)
    Store_ref_ID =models.CharField(max_length=150)
    Total_Amount =models.CharField(max_length=150)
    Merchant_Total =models.CharField(max_length=150)
    Sub_total_Amount =models.CharField(max_length=150)
    Discount =models.CharField(max_length=150)
    Aggregator_Discount =models.CharField(max_length=150)
    Merchant_Discount =models.CharField(max_length=150)
    Taxes =models.CharField(max_length=150)
    Charges =models.CharField(max_length=150)
    Fulfillment_mode =models.CharField(max_length=150)
    Wallet_credit_amount =models.CharField(max_length=150)
    City =models.CharField(max_length=150)

