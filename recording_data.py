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


def rec_txt(data):
    if os.path.exists('rec_data.txt'):
        with open('rec_data.txt', 'a', newline='') as f:
            f.writelines(data)
    else:
        print(-1)
        with open('rec_data.txt', 'w', newline='') as f:
            f.writelines(data)


def output_txt():
    with open('rec_data.txt') as f:
        for line in f:
            print(line)

# вывод списком из csv

def output_csv():
    with open('rec_data.csv') as f:
        reader = csv.reader(f)
        return list(reader)

