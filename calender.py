import sys
from datetime import datetime
import calendar
from dateutil import relativedelta
import argparse


def print_date(date, current):
	date = str(date)
	res = ''
	if(len(date) == 1):
                res += ' '
	res += date

	if(current):
		print('\x1b[7;33;40m' + res + '\x1b[0m', end ='')
		print(" ", end='')
	else:
		res += ' '
		print(res, end ='')

def init(first_day):
	res = ''
	temp = ' '
	temp *= first_day*3;
	res += temp
	res += ''
	print(res,end='')

def print_month(month, year):
	res = month;
	res += ' '
	res += year

	res = ' '*((20 - len(res))//2) + res;
	print(res)

def cal(x):
        date = datetime.now() + relativedelta.relativedelta(months=x)
        current_date = int(date.strftime("%-d"))

        first = date.replace(day=1)

        first_day = int(first.strftime("%w"))
        number_of_days = int(calendar.monthrange(first.year, first.month)[1])
        counter = 1
        print_month(date.strftime("%B"), date.strftime("%Y"))
        print("Su Mo Tu We Th Fr Sa")
        init(first_day)
        while(number_of_days > 0):
                if(first_day == 7):
                        first_day = 0
                        print()
                print_date(counter, counter == current_date)
                counter += 1
                first_day += 1
                number_of_days -= 1

        print()
        
        

if __name__ == "__main__":

        p=argparse.ArgumentParser(description='Arbab khan, Calender python project, Cisco intern ')
        p.add_argument("-p","--param",action="store",required=False,help="integer +12 through -12, including 0")
        args=p.parse_args()
        
        if args.param:
                if int(args.param) in range(-12,12):
                        cal(int(args.param))
                else:
                        p.print_help()
        else:
                cal(0)
                
