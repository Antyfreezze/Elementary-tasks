#!/usr/bin/env python3.5
# Filename:num_to_text.py
# -*- coding: utf-8 -*-

def main():
    print('''Может преобразовывать числа в прописные до 12ти разрядов, 
        число нужно вводить без пробелов. Например: 100000000000''')
    error = True
    while error:
        try:
            some_num = int(input('Введите число для преобразования: '))
        except:
            print('Используйте целое число, пожалуйста.')
    
        if some_num < 0:
            print('Используйте положительные числа, пожалуйста')
            continue
        elif some_num > 999999999999:
            print('Программа пока не умеет обрабатывать числа в которых больше 12ти знаков')
            continue
        else:
            error = False
  
  
    fear = Converter(str(some_num))
    fear.convert()


# noinspection PyUnreachableCode
class Converter(object):
    #dictionaries for convertation
    dict1_9 = {'1':'один', '2':'два', '3':'три', 
             '4':'четыре', '5':'пять', '6':'шесть',
             '7':'семь', '8':'восемь', '9':'девять'}
    dict10_19 = {'10':'десять', '11':'одиннадцать', '12':'двенадцать',
              '13':'тринадцать', '14':'четырнадцать', '15':'пятнадцать',
              '16':'шестнадцать', '17':'семнадцать', '18':'восемьнадцать',
              '19':'девятнадцать'}
    dict20_90 = {'2':'двадцать', '3':'тридцать', '4':'сорок',
           '5':'пятьдесят', '6':'шестьдесят', '7':'семьдесят',
           '8':'восемьдесят', '9':'девяносто'}
    dict_hundred = {'1':'сто', '2':'двести', '3':'триста',
           '4':'четыреста', '5':'пятсот', '6':'шестьсот',
           '7':'семьсот', '8':'восемьсот', '9':'девятьсот'}
    dict_thousand = {'1':'одна тысяча', '2':'две тысячи', '3':'тысячи', '5':'тысяч'}
    dict_million = {'1':'миллион', '2':'миллиона', '5':'миллионов'}
    dict_milliard = {'1':'миллиард', '2':'миллиарда', '5':'миллиардов'}
  
  
    def __init__(self, num):
        self.num = num
    
    def division(self, part):
        res_list = []
        while len(part) > 0:
            if len(part) == 3:
                if part[0] == '0':
                    part = part[1:]
            else:
                res_list.append(self.dict_hundred[part[0]])
                part = part[1:]
        if len(part) == 2:
            if part[0] == '0':
                part = part[1:]
            elif part[0] == '1':
                res_list.append(self.dict10_19[ part ])
                part = ''
            elif int(part[0]) > 1:
                res_list.append(self.dict20_90[ part[0] ])          
                part = part[1:]

        if len(part) == 1:
            if part[0] != '0':
                res_list.append(self.dict1_9[ part[0] ])
                del(part)
            del(part)
    return res_list
  
    def convert(self):
        result = []
        while len(self.num) > 0:
            num_len = len(self.num)
            if num_len <= 12 and num_len > 9:
                result += self.division(self, self.num[0:-9])   
            if int(self.num[-11:-9]) >= 5:          
                result.append( self.dict_milliard['5'] )
            elif int(self.num[-11:-9]) == 0 and int(self.num[-12]) > 0:
                result.append( self.dict_milliard['5'] )
            elif int(self.num[-11:-9]) > 1 and int(self.num[-11:-9]) < 5: 
                result.append( self.dict_milliard['2'] )
            elif int(self.num[-11:-9]) == 1:
                result.append( self.dict_milliard['1'] )
                self.num = self.num[-9:]

        if num_len <= 9 and num_len > 6:
            result += self.division(self, self.num[0:-6])        
            if int(self.num[-8:-6]) >= 5:          
                result.append( self.dict_million['5'] )
            elif int(self.num[-8:-6]) == 0 and int(self.num[-9]) > 0:
                result.append( self.dict_million['5'] )
            elif int(self.num[-8:-6]) > 1 and int(self.num[-7:-5]) < 5: 
                result.append( self.dict_million['2'] )
            elif int(self.num[-8:-6]) == 1:
                result.append( self.dict_million['1'] )
                self.num = self.num[-6:]
        
        if num_len <= 6 and num_len > 3:
            result += self.division(self, self.num[0:-3])
            if int(self.num[-5:-3]) >= 5:          
                result.append(self.dict_thousand['5'])
            elif int(self.num[-5:-3]) == 0 and int(self.num[-6]) > 0:
                result.append(self.dict_thousand['5'])
            elif int(self.num[-5:-3]) > 2 and int(self.num[-5:-3]) < 5: 
                result.append( self.dict_thousand[ '3' ] )
            elif int(self.num[-5:-3]) == 2:
                result.pop()
                result.append( self.dict_thousand[ '2' ] )
            elif int(self.num[-5:-3]) == 1:
                result.pop()
                result.append( self.dict_thousand['1'] )
                self.num = self.num[-3:]
        
        if num_len <= 3:
            result += self.division(self, self.num)        
            self.num = ''
            
        print(' '.join(result))
    
if __name__ == '__main__':
    main()
  