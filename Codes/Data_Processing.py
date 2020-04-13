# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 00:46:35 2020

@author: SUBHAM KUNDU
"""
import pandas as pd
import tkinter as tk
from tkinter import simpledialog
from tabulate import tabulate
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']


#for accessing the airway travels
credentials_air= ServiceAccountCredentials.from_json_keyfile_name('<Enter the Credentials from the google account>',scope)
gc=gspread.authorize(credentials_air)
sheetid_air='1H4rtt5S3vXi-BDiCzGi5QKENJzKaLfgWC-CAVQgEhVE'
workbook = gc.open_by_key(sheetid_air)
sheet1 = workbook.get_worksheet(0)
values = sheet1.get_all_values()
air_data = pd.DataFrame(values[1:],columns=values[0])

#for accessing the railway travels
credentials_train= ServiceAccountCredentials.from_json_keyfile_name('robotic-abode-273818-d137dd7ac099.json',scope)
gc=gspread.authorize(credentials_train)
sheetid_train='1uzNPCS8l9iG7sajBSTTLiLcSxBEoHlWEu36t880ihyE'
workbook = gc.open_by_key(sheetid_train)
sheet2 = workbook.get_worksheet(0)
values = sheet2.get_all_values()
train_data = pd.DataFrame(values[1:],columns=values[0])

#for accessing the bus travels
credentials_bus= ServiceAccountCredentials.from_json_keyfile_name('robotic-abode-273818-d137dd7ac099.json',scope)
gc=gspread.authorize(credentials_bus)
sheetid_bus='1RutV395z_mRkRGaxb5OZsS5XyaWJm25_hFEgcf8C3QU'
workbook = gc.open_by_key(sheetid_bus)
sheet3 = workbook.get_worksheet(0)
values = sheet3.get_all_values()
bus_data = pd.DataFrame(values[1:],columns=values[0])

#for accessing the community details
credentials_com= ServiceAccountCredentials.from_json_keyfile_name('robotic-abode-273818-d137dd7ac099.json',scope)
gc=gspread.authorize(credentials_com)
sheetid_com='1f5eX5L3a5Xb4Vi5amFH2d0hFgqWa-suHfh_m5XAjzTc'
workbook = gc.open_by_key(sheetid_com)
sheet4 = workbook.get_worksheet(0)
values = sheet4.get_all_values()
com_data = pd.DataFrame(values[1:],columns=values[0])

#for accessing the hotspot details
credentials_hotspot= ServiceAccountCredentials.from_json_keyfile_name('robotic-abode-273818-d137dd7ac099.json',scope)
gc=gspread.authorize(credentials_hotspot)
sheetid_hotspot='1MySoMsZ05Ny6rypELfOSnbpwElEeiLs4Dh-bADcXiqg'
workbook = gc.open_by_key(sheetid_hotspot)
sheet5 = workbook.get_worksheet(0)
values = sheet5.get_all_values()
hotspot_data = pd.DataFrame(values[1:],columns=values[0])

#converting the parameters into timeframe
air_data['Departure_Date'] =  pd.to_datetime(air_data['Departure_Date'])
air_data['Arrival_Date'] =  pd.to_datetime(air_data['Arrival_Date'])
bus_data['Departure_Date'] =  pd.to_datetime(bus_data['Departure_Date'])
bus_data['Arrival_Date'] =  pd.to_datetime(bus_data['Arrival_Date'])
train_data['Departure_Date'] =  pd.to_datetime(train_data['Departure_Date'])
train_data['Arrival_Date'] =  pd.to_datetime(train_data['Arrival_Date'])
air_data['Departure_Time']= pd.to_datetime(air_data['Departure_Time'])
train_data['Departure_Time']= pd.to_datetime(train_data['Departure_Time'])
bus_data['Departure_Time']= pd.to_datetime(bus_data['Departure_Time'])
air_data['Arrival_Time']= pd.to_datetime(air_data['Arrival_Time'])
train_data['Arrival_Time']= pd.to_datetime(train_data['Arrival_Time'])
bus_data['Arrival_Time']= pd.to_datetime(bus_data['Arrival_Time'])

com_data['Date'] =  pd.to_datetime(com_data['Date'])
com_data['Time'] =  pd.to_datetime(com_data['Time'])



A_Contact=[]
A_Pincode=[]
A_Flight=[]
A_From=[]
A_To=[]

T_Contact=[]
T_Pincode=[]
T_No=[]
T_From=[]
T_To=[]

B_Contact=[]
B_From=[]
B_To=[]



#for checking the patient is present in the air list
def Air_Search(phone):
    for i,j in air_data.iterrows():
        if(j.Contact ==initial_no ):
            index=i
            break
        else:
            index=-1
            
    return index

#for checking the patient is present in the rail list
def Train_Search(phone):
    for i,j in train_data.iterrows():
        if(j.Contact == initial_no):
            index=i
            break
        else:
            index= -1
            
    return index

#for checking the patient is present in the bus list
def Bus_Search(phone):
    for i,j in bus_data.iterrows():
        if(j.Contact == initial_no):
            index=i
            break
        else:
            index= -1
            
    return index


#persons with common flight
def FlightNo_Common(flight,depart,arrival):
    for i,j in air_data.iterrows():
        if(j.FlightNo == flight and j.Departure_Date == depart or j.Arrival_Date == arrival ):
            A_Contact.append(j.Contact)
            A_Pincode.append(j.Pincode)
            A_Flight.append(j.FlightNo)
            A_From.append(j.From)
            A_To.append(j.To)
    return 0




#persons with common train
def TrainNo_Common(train,depart,arrival):
    for i,j in train_data.iterrows():
        if(j.TrainNo == train and j.Departure_Date == depart or j.Arrival_Date == arrival ):
            T_Contact.append(j.Contact)
            T_Pincode.append(j.Pincode)
            T_No.append(j.TrainNo)
            T_From.append(j.From)
            T_From.append(j.To)
            
    return 0
#persons with common bus
def Bus_Common(frm, to, depart):
    for i,j in bus_data.iterrows():
        if(j.From == frm and j.To == to or j.Departure_Time == depart ):
            B_Contact.append(j.Contact)
            B_From.append(j.From)
            B_To.append(j.To)
    return 0
#Taking input using a user friendly dialog box
ROOT = tk.Tk()
ROOT.withdraw()
# the input dialog
affected_No = simpledialog.askstring(title="TrackCovid-19",
                                  prompt="Enter the Number of the affected Person")
initial_no=affected_No



def gatherings(phone):
    for i,j in com_data.iterrows():
        if(j.Contact==phone):
            print ('\n')
            print ('The person attended the gathering on '+ (str)(j.Date)[0:10]+ ' at '+ (str)(j.Time)[10:16] + ' of approx gatherings ' + j.ApproxGathering + ' in '+ j.Place)
            
    return None

#Creating the hotspot details
def hotspots(pin):
    for i,j in hotspot_data.iterrows():
        starting_pincode=j.PinCodeStarting
        ending_pincode=j.PinCodeEnding
        if(pin>=starting_pincode and pin<=ending_pincode):
            print('\n')
            print('The person belongs to the hotspot '+ j.City + ' located in the state '+ j.State)
    return None
        
            
def Main(phone):
    
    index_air=Air_Search(phone)
    if(index_air!=-1):
        a=air_data.iloc[index_air]
        FlightNo_Common(a.FlightNo,a.Departure_Date,a.Arrival_Date)
        
    index_train=Train_Search(phone)
    if(index_train!=-1):
        t=train_data.iloc[index_train]
        TrainNo_Common(t.TrainNo,t.Departure_Date,t.Arrival_Date)
    
    index_bus=Bus_Search(phone)
    if(index_bus!=-1):
        b=bus_data.iloc[index_bus]
        Bus_Common(b.From,b.To,b.Departure_Time)
    
    return 0

Main(initial_no)

#displaying direct contacts with the affected person
if(len(A_Contact)!=0):  #There is association with the person in the list
    print('\n')
    print('\n')
    print ("The persons associated with the person with Contact No directly through flight-->"+initial_no+" are as follows")
    print('\n')
    print(tabulate({"Contact No": A_Contact,"Pin Code" : A_Pincode, "Flight No" : A_Flight},headers = "keys",showindex="always",tablefmt="github"))
    for i in A_Contact:
        gatherings(i)
    for j in A_Pincode:
        hotspots(j)
else:
    print("No record found with air history")
    
print('\n')
print('************************************************************************************************************')

#displaying direct contacts with the affected person in train
if(len(T_Contact)!=0):  #There is association with the person in the list
    print ("The persons associated with the person with Contact No directly through train details-->"+initial_no+" are as follows")
    print('\n')
    print(tabulate({"Contact No": T_Contact,"Pin Code" : T_Pincode, "Train No" : T_No},headers = "keys",showindex="always",tablefmt="github"))
    for i in T_Contact:
        gatherings(i)
else:
    print("No record found with train history")
    
print('\n')
print('*************************************************************************************************************')

if(len(B_Contact)!=0):  #There is association with the person in the list
    print ("The persons associated with the person with Contact No directly through bus details-->"+initial_no+" are as follows")
    print('\n')
    print(tabulate({"Contact No": B_Contact,"Pin Code" : B_Pincode},headers = "keys",showindex="always",tablefmt="github"))
    for i in B_Contact:
        gatherings(i)
else:
    print('\n')
    print("No record found with bus history")



    

    
        



        


    


