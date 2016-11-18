import sys


def ip_available(ip):



        if int(ip.split('/')[1]) == 24:
                tmp = ip.split('/')[0].split('.')
                tmp[3] = '1'
                ip_start = '.'.join(tmp)
                tmp[3] = '254'
                ip_end = '.'.join(tmp)
                return(ip_start,'-',ip_end)

        elif int(ip.split('/')[1]) == 16:
                tmp = ip.split('/')[0].split('.')
                tmp[2] = '0'
                tmp[3] = '1'
                ip_start = '.'.join(tmp)
                tmp[2] = '255'
                tmp[3] = '254'
                ip_end = '.'.join(tmp)
                return(ip_start,'-',ip_end)

        elif int(ip.split('/')[1]) == 8:
                tmp = ip.split('/')[0].split('.')
                tmp[2] = tmp[1] = '0'
                tmp[3] = '1'
                ip_start = '.'.join(tmp)
                tmp[2] = tmp[1] = '255'
                tmp[3] = '254'
                ip_end = '.'.join(tmp)
                return(ip_start,'-',ip_end)

        elif 32 > int(ip.split('/')[1]) > 24:
                tmp = ip.split('/')[0].split('.')
                tmp3 = int(tmp[3])
                tmp3 = tmp3 - tmp3 % (2 ** (32 - int(ip.split('/')[1]))) + 1
                tmp[3] = str(tmp3)
                ip_start = '.'.join(tmp)
                tmp[3] = str(tmp3 + (2 ** (32 - int(ip.split('/')[1]))) - 3)
                ip_end = '.'.join(tmp)
                return(ip_start,'-',ip_end)

        elif 16 < int(ip.split('/')[1]) < 24:
                tmp = ip.split('/')[0].split('.')
                tmp2 = int(tmp[2])
                tmp2 = tmp2 - tmp2 % (2 ** (24 - int(ip.split('/')[1])))
                tmp[2] = str(tmp2)
                tmp[3] = '1'
                ip_start = '.'.join(tmp)
                tmp[2] = str(tmp2 + (2 ** (24 - int(ip.split('/')[1])))-1)
                tmp[3] = '254'
                ip_end = '.'.join(tmp)
                return(ip_start,'-',ip_end)

        elif 8 < int(ip.split('/')[1]) < 16:
                tmp = ip.split('/')[0].split('.')
                tmp1 = int(tmp[1])
                tmp1 = tmp1 - tmp1 % (2 ** (16 - int(ip.split('/')[1])))
                tmp[1] = str(tmp1)
                tmp[2] = '0'
                tmp[3] = '1'
                ip_start = '.'.join(tmp)
                tmp[1] = str(tmp1 + (2 ** (16 - int(ip.split('/')[1])))-1)
                tmp[2] = '255'
                tmp[3] = '254'
                ip_end = '.'.join(tmp)
                return(ip_start,'-',ip_end)

        elif 0 < int(ip.split('/')[1]) < 8:
                tmp = ip.split('/')[0].split('.')
                tmp0 = int(tmp[0])
                tmp0 = tmp0 - tmp0 % (2 ** (8 - int(ip.split('/')[1])))
                tmp[0] = str(tmp0)
                tmp[1] = tmp[2] = '0'
                tmp[3] = '1'
                ip_start = '.'.join(tmp)
                tmp[0] = str(tmp0 + (2 ** (8 - int(ip.split('/')[1])))-1)
                tmp[1] = tmp[2] = '255'
                tmp[3] = '254'
                ip_end = '.'.join(tmp)
                return(ip_start,'-',ip_end)


        else:
                return('Error')

#print('Available IP is : ',' '.join(ip_available(ip)))

while True:
        ip_address = input("Please input an IP address like x.x.x.x/x or press 'q' to quit : ")
        ip = str(ip_address)
        if ip == "q":
                break

        print('Available IP is : ',' '.join(ip_available(ip)))
