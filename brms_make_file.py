import csv


def make_brms_data(imsi1, iccid, msisdn, other, count=1):
    n = 0
    iccid = int(str(iccid) + '2')
    with open("result.csv", "w", newline='') as file:
        writer = csv.writer(file, delimiter=' ')
        while n < count:
            result_row = [imsi1, iccid, msisdn]
            for x in range(11):
                result_row.append(other)
            writer.writerow(result_row)
            imsi1 += 1
            msisdn += 1
            iccid += 10
            n += 1

# with open("result.csv", "w") as file:
#     fieldnames = ['IMSI1', 'ICCID', 'MSISDN', 'EKI', 'PUK1', 'PUK2', 'PIN1', 'PIN2', 'ADM', 'KIC1', 'KID1', 'KIK1',
#                   'KIC2', 'KID2', 'KIK2', 'KIC3', 'KID3', 'KIK3']
#     writer = csv.DictWriter(file, fieldnames=fieldnames, delimetr=' ')


if __name__ == '__main__':
    make_brms_data(250203399008438, 89701200624900000602, 78946900011, 1111, count=10000)
    # imsi1 = int(input('Введите imsi: '))
    # iccid = int(input('Введите iccid: '))
    # msisdn = int(input('Введите msisdn: '))
    # count = int(input('Введите количество SIM-карт: '))
    # make_brms_data(imsi1, iccid, msisdn, 1111, count=count)
