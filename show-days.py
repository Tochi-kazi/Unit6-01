# Created by: Tochukwu Iroakazi
# Created on: Nov 2017
# Created for: ICS3U
# This program shiw days of the week 

from enum import Enum

Days = Enum('1','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')

number = input('Type in the number of your favourite day of the week: ')
while number <= 0 or number > 7:
    print('Type in a number between 1-7 ')
    number = input('Type in the number of your favourite day of the week: ')

if number in Days:
    print(number + 'This is not a valid number in the days of the week')
else:
    print('Your favorite day of the week is: ' + str(Days[number]))


