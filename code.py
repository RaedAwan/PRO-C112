import pandas as pd
import statistics as st
import plotly.express as pe
import plotly.graph_objects as go
import csv

# -----------------------------------------------------------------------------------------------------------------------

data = pd.read_csv("data.csv")

amountSaved = data["quant_saved"].tolist()

remindedList = data["rem_any"].tolist()

graph = pe.scatter(data, y = amountSaved , color = "rem_any")

# graph.show()

# -----------------------------------------------------------------------------------------------------------------------

mean = st.mean(amountSaved)
stdev = st.stdev(amountSaved)
median = st.median(amountSaved)
mode = st.mode(amountSaved)

print("--------------------------------------------------------------------")

print("Mean of the amount saved by everyone : " , mean)
print("Median of the amount saved by everyone : " , median)
print("Mode of the amount saved by everyone : " , mode)

print("Stdev of the amount saved by everyone : " , stdev)

print("--------------------------------------------------------------------")


# -----------------------------------------------------------------------------------------------------------------------


totalPeople = len(remindedList)

no_of_people_who_reminded = 0

for i in remindedList: 
    if i == 1 :
        no_of_people_who_reminded  += 1


no_of_people_who_not_reminded = totalPeople - no_of_people_who_reminded

graph = go.Figure(go.Bar( x = ["Reminded" , "Not Reminded"]  , y = [no_of_people_who_reminded , no_of_people_who_not_reminded ] ))

# graph.show()

# -----------------------------------------------------------------------------------------------------------------------

with open("data.csv") as f:
    a = csv.reader(f)
    savingData = list(a)

savingData.pop(0)

reminded_Savings = []

not_Reminded_Savings = []

for i in savingData:
    if int(i[3]) == 1 :
        reminded_Savings.append(float(i[0]))
    else :
        not_Reminded_Savings.append(float(i[0]))


meanR = st.mean(reminded_Savings)
stdevR = st.stdev(reminded_Savings)
medianR = st.median(reminded_Savings)
modeR = st.mode(reminded_Savings)


print("Mean of the amount saved by those who were reminded : " , meanR)
print("Median of the amount saved by those who were reminded : " , medianR)
print("Mode of the amount saved by those who were reminded : " , modeR)

print("Stdev of the amount saved by those who were reminded : " , stdevR)

print("--------------------------------------------------------------------")



meanNR = st.mean(not_Reminded_Savings)
stdevNR = st.stdev(not_Reminded_Savings)
medianNR = st.median(not_Reminded_Savings)
modeNR = st.mode(not_Reminded_Savings)


print("Mean of the amount saved by those who were not reminded : " , meanNR)
print("Median of the amount saved by those who were not reminded : " , medianNR)
print("Mode of the amount saved by those who were not reminded : " , modeNR)

print("Stdev of the amount saved by those who were not reminded : " , stdevNR)

print("--------------------------------------------------------------------")



