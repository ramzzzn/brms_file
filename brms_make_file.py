import csv
import glob
from itertools import islice


def make_output_file():
    inp_files = glob.glob('input/*.inp')
    n = 31
    for inp_file in inp_files:
        output_name = (inp_file.replace('.inp', '.out')).split('\\')[1]
        with open(inp_file, 'r') as inp_file:
            lines = list(islice(inp_file, 0, n))
        imsi1 = int(lines[23].replace('IMSI1:', ''))
        iccid = int(lines[22].replace('ICCID:', ''))
        msisdn = int(lines[30])
        make_brms_data(imsi1, iccid, msisdn, other='1111', count=10000)
        with open(f"output/{output_name}", 'w') as out_file:
            for x in lines[:-1]:
                out_file.write(x)
            with open("result.csv", newline='') as brms_file:
                reader = csv.reader(brms_file)
                for row in reader:
                    out_file.write(row[0]+"\n")


def make_brms_data(imsi1, iccid, msisdn, other='1111', count=1):
    n = 0
    iccid = int(str(iccid) + '2')
    with open("result.csv", "w", newline='') as file:
        writer = csv.writer(file, delimiter=' ')
        while n < count:
            result_row = [imsi1, iccid, msisdn]
            for x in range(15):
                result_row.append(other)
            writer.writerow(result_row)
            imsi1 += 1
            msisdn += 1
            iccid += 10
            n += 1
    return file


# with open("result.csv", "w") as file:
#     fieldnames = ['IMSI1', 'ICCID', 'MSISDN', 'EKI', 'PUK1', 'PUK2', 'PIN1', 'PIN2', 'ADM', 'KIC1', 'KID1', 'KIK1',
#                   'KIC2', 'KID2', 'KIK2', 'KIC3', 'KID3', 'KIK3']
#     writer = csv.DictWriter(file, fieldnames=fieldnames, delimetr=' ')


if __name__ == '__main__':
    make_brms_data(999990000113489, 8970120062490143549, 78947050000, 1111, count=6513)
    # make_output_file()
    # imsi1 = int(input('Введите imsi: '))
    # iccid = int(input('Введите iccid: '))
    # msisdn = int(input('Введите msisdn: '))
    # count = int(input('Введите количество SIM-карт: '))
    # make_brms_data(imsi1, iccid, msisdn, 1111, count=count)
