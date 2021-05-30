import csv
from collections import Counter

def find_mean(data):
    sum_of_data = 0

    for i in data:
        sum_of_data = sum_of_data + i
    print("Total Sum Of Data: " + str(sum_of_data))

    mean = sum_of_data / len(data)
    print("Mean Of Data: " + str(mean))

def find_median(sorted_data):
    print(sorted_data)
    data_length = len(sorted_data)
    if data_length % 2 == 0:
        first_num = float(sorted_data[data_length // 2])
        second_num = float(sorted_data[data_length // 2 - 1])
        
        median = (first_num + second_num) / 2
    else:
        median = float(sorted_data[data_length // 2])
    print("Median: " + str(median))

def find_mode(sorted_data):
    pass

with open("./files/data/SOCR-HeightWeight.csv", newline="") as csv_file:
    reader = csv.reader(csv_file)
    file_data = list(reader)

file_data.pop(0)
new_data = []

for i in file_data:
    new_data.append(float(i[1]))

find_mean(new_data)
#find_median(new_data.sort())