# запись данных с консоли (список) в csv и txt
#
import csv
import os.path

def rec_csv(data):
    if os.path.exists('rec_data.csv'):
        with open('rec_data.csv', 'a', newline='') as f:
            writer_object = csv.writer(f)
            writer_object.writerow(data)
            f.close()
    else:
        print(-1)
        with open('rec_data.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)


# def rec_txt():
# def output_txt():


# вывод списком из csv

def output_csv():
    with open('rec_data.csv') as f:
        reader = csv.reader(f)
        return list(reader)

