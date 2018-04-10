# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 12:35:48 2018
SCRAPPING COMBINED !!!
@author: Tawhid
"""


import selenium
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re

caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True
browser = selenium.webdriver.Firefox(capabilities=caps)
'''
FUNCTIONS
'''
def mine_alphanum(mylist, shop_name):
    import re
    
    if shop_name == 'meena': key_string = '  ADD TO BAG'
    elif shop_name == 'shpno': key_string = 'Add to cart'
    start_veg = True # it was False, but changed on 1st Jan 2018 because this function was returning empty list for Meena
    products=[]
    product = ''
    for index, value in enumerate(mylist):
        if shop_name == 'shpno':
            start_veg = True
        if start_veg == False and re.search('Showing', value):
            start_veg = True
            continue
        
        if start_veg == True and index < len(mylist) - 2:
            if mylist[index] != key_string:
                product = product + value
            if mylist[index] == key_string:
                products.append(product)
                product=''
    #print(products)   
    
    refined_products = []
    for index, value in enumerate(products):
        alnum_product = ''
        for ch in value:
            if re.search('[a-zA-Z0-9./() ]', ch):
                if ch == '/': ch = ' '
                alnum_product = alnum_product + ch
        refined_products.append(alnum_product)

    refined_products_sh = []
    for index, value in enumerate(refined_products):
        x = re.split(r'[1][ ][K][g]', value) 
        refined_products_sh.append(x[0])
            
    if shop_name == 'shpno': return refined_products_sh
    elif shop_name == 'meena': return refined_products

'''
Scrap Meeena:
'''
url_meena = 'http://www.meenaclick.com/category/vegetable-1'
browser.get(url_meena)
x = browser.find_element_by_xpath('//*[@id="ng-app"]/body/div[8]/div/div[2]/div[1]/div[4]/div[1]')
mylist=[]
mylist=x.text.splitlines()
#print(x.text,'type of x: ', type(x.text), type(mylist))  #  'len: ', len(x)  # ok code
#print('MEENA: ', '\n',  mine_alphanum(mylist, 'meena'), '\n', 'M END', '\n','\n','\n','\n', )
meena = []
meena = mine_alphanum(mylist, 'meena')

'''
Scrap Shpno:
'''
from selenium.webdriver.support.ui import Select   # this library to give automated input in the dropdown list
import time

url_sh = 'http://www.shwapno.com/categories/fruits--vegetables-vegetables/cid-CU00336652.aspx'
browser.get(url_sh)

myselelem = browser.find_element_by_id('state')
drpdwn = Select(myselelem)
drpdwn.select_by_visible_text('Dhaka')
time.sleep(5) # give some time to internet to load list of areas under Dhaka city

myselelem2 = browser.find_element_by_id('city')
#print(myselelem2.text) # dont know why Taw printed this
drpdwn2 = Select(myselelem2)
drpdwn2.select_by_visible_text('Banani')
time.sleep(5) # again give some time before clicking "Submit"

search_form = browser.find_element_by_id('btnFindStore')
search_form.click()
time.sleep(5)

# /html/body/form/div[3]/center/div/div/center/div/div[3]/div[2]/div[3]/div/div/div/div[2]/div[1]/div   # this works better for firefox
# //*[@id="3641451_CU00336652"]/div[1]/div # this works better for google chrome 
y = browser.find_element_by_xpath('/html/body/form/div[3]/center/div/div/center/div/div[3]/div[2]/div[3]/div/div/div/div[2]/div[1]/div') 
#print(y.text, 'type of y(shpno)', type(y.text))
mylist=[]
mylist=y.text.splitlines()
#print('SHPNO: ', '\n',  mine_alphanum(mylist, 'shpno') )
shpno = []
shpno = mine_alphanum(mylist, 'shpno')

'''
start working using re
'''
print('meena: ', meena, '\n\n\nshpno: ', shpno)
browser.get('http://www.google.com/ncr')

'''
re meena:
'''

name_unit_price_separated = []
name_unit_price_unsorted = []
for entity in meena:
    if re.search('Bulk', entity):
        
        for i in re.finditer('Bulk', entity):
            x = i.span()
        name = entity[:x[0] - 1 ]
        for i in re.finditer('KG', entity):
            y = i.span()
        unit = entity[y[0]-5:y[1]]
        price = entity[y[1]: ]
#        rest_name = entity[x[1]:]
        local_list=[]
        local_list.append(name); local_list.append(unit); local_list.append(price)
        name_unit_price_separated.append(local_list)

    
    elif re.search('BULK', entity):
        for i in re.finditer('BULK', entity):
            x = i.span()
        name = entity[:x[0] - 1 ]
        for i in re.finditer('KG', entity):
            y = i.span()
        unit = entity[y[0]-5:y[1]]
        price = entity[y[1]: ]
#        rest_name = entity[x[1]:]
        local_list=[]
        local_list.append(name); local_list.append(unit); local_list.append(price)
        name_unit_price_separated.append(local_list)

    elif re.search('bulk', entity):
        for i in re.finditer('bulk', entity):
            x = i.span()
        name = entity[:x[0] - 1 ]
        for i in re.finditer('KG', entity):
            y = i.span()
        unit = entity[y[0]-5:y[1]]
        price = entity[y[1]: ]
#        rest_name = entity[x[1]:]
        local_list=[]
        local_list.append(name); local_list.append(unit); local_list.append(price)
        name_unit_price_separated.append(local_list)

    elif re.search('PACK', entity):
        
        for i in re.finditer('PACK', entity):
            x = i.span()
        name = entity[:x[0]-1]
        unit_number = entity[ x[1] : x[1] + 1 ]
        unit_name = ' packet'
        unit = unit_number + ' ' + unit_name

        for i in re.finditer('EA', entity):
            y = i.span()
        price = entity[y[1]+1:]
        local_list=[]
        local_list.append(name); local_list.append(unit); local_list.append(price)
        name_unit_price_separated.append(local_list)

    elif re.search('Pack', entity):
        
        for i in re.finditer('Pack', entity):
            x = i.span()
        name = entity[:x[0]-1]
        unit_number = entity[ x[1] : x[1] + 1 ]
        unit_name = ' packet'
        unit = unit_number + ' ' + unit_name

        for i in re.finditer('EA', entity):
            y = i.span()
        price = entity[y[1]+1:]
        local_list=[]
        local_list.append(name); local_list.append(unit); local_list.append(price)
        name_unit_price_separated.append(local_list)
    
    elif re.search('PCS', entity):
        
        for i in re.finditer('PCS', entity):
            x = i.span()
        name = entity[:x[0]-1]
        unit_number = entity[ x[1] : x[1] + 1 ]
        unit_name = 'Per Piece'
        unit = unit_name

        for i in re.finditer('EA', entity):
            y = i.span()
        price = entity[y[1]+1:]
        local_list=[]
        local_list.append(name); local_list.append(unit); local_list.append(price)
        name_unit_price_separated.append(local_list)

    elif re.search('PC', entity):
        
        for i in re.finditer('PC', entity):
            x = i.span()
        name = entity[:x[0]-1]
        unit_number = entity[ x[1] : x[1] + 1 ]
        unit_name = 'Per Piece'
        unit = unit_name

        for i in re.finditer('EA', entity):
            y = i.span()
        price = entity[y[1]+1:]
        local_list=[]
        local_list.append(name); local_list.append(unit); local_list.append(price)
        name_unit_price_separated.append(local_list)
        
    elif re.search('Pcs', entity):
        
        for i in re.finditer('Pcs', entity):
            x = i.span()
        name = entity[:x[0]-1]
        unit_number = entity[ x[1] : x[1] + 1 ]
        unit_name = 'Per Piece'
        unit = unit_name

        for i in re.finditer('EA', entity):
            y = i.span()
        price = entity[y[1]+1:]
        local_list=[]
        local_list.append(name); local_list.append(unit); local_list.append(price)
        name_unit_price_separated.append(local_list)
    
    else: 
        #name_unit_price_unsorted.append(entity)
        continue

#for value in name_unit_price_separated:
#    print(value)
#print('--------------')
#for value in name_unit_price_unsorted:
#    print(value)

for entity in name_unit_price_unsorted:
    if re.search('KG', entity):
        
        for i in re.finditer('KG', entity):
            x = i.span()
        name = entity[ : x[0]-5]
        unit = entity[ x[0]-5 : x[1] ]
        price = entity[x[1]+1:]
        local_list=[]
        local_list.append(name);  local_list.append(unit); local_list.append(price)
        name_unit_price_separated.append(local_list)

print('------  Meena  --------')
print(name_unit_price_separated)
meena = name_unit_price_separated
meena_picked=[1]*len(meena)
#for value in name_unit_price_separated:
#    print(value)
    
'''
re: Shpno
'''
name_unit_price_separated = []
name_unit_price_unsorted = []

for entity in shpno:
    if 'Per Kg' in entity:
        xx = re.split(r'[P][e][r]', entity)
        entity = xx[0]+xx[1] 
        
    if re.search('kg', entity):
        for i in re.finditer('kg', entity):
            x = i.span()
        name = entity[: x[0] - 1 ]

        unit = entity[x[0] : x[1]]
        price = entity[x[1]+1 : ]
#        rest_name = entity[x[1]:]
        local_list=[]
        local_list.append(name); local_list.append(unit); local_list.append(price)
        name_unit_price_separated.append(local_list)

    elif re.search('Kg', entity):
        
        for i in re.finditer('Kg', entity):
            x = i.span()
        name = entity[: x[0] - 1 ]

        unit = entity[x[0] : x[1]]
        price = entity[x[1]+1 : ]
#        rest_name = entity[x[1]:]
        local_list=[]
        local_list.append(name); local_list.append(unit); local_list.append(price)
        name_unit_price_separated.append(local_list)        

    elif re.search('Per Kg', entity):
        
        for i in re.finditer('Per Kg', entity):
            x = i.span()
        name = entity[: x[0] ]

        unit = entity[x[0]+4 : x[1]]
        price = entity[x[1]+1 : ]
#        rest_name = entity[x[1]:]
        local_list=[]
        local_list.append(name); local_list.append(unit); local_list.append(price)
        name_unit_price_separated.append(local_list)                

    elif re.search('ati', entity):
        
        for i in re.finditer('ati', entity):
            x = i.span()
        name = entity[: x[0] - 1 ]

        unit = entity[x[0] : x[1]]
        price = entity[x[1]+1 : ]
#        rest_name = entity[x[1]:]
        local_list=[]
        local_list.append(name); local_list.append(unit); local_list.append(price)
        name_unit_price_separated.append(local_list)        
        
    elif re.search('Per Piece', entity):
        
        for i in re.finditer('Per Piece', entity):
            x = i.span()
        name = entity[: x[0] - 1 ]

        unit = entity[x[0] : x[1]]
        price = entity[x[1]+1 : ]
#        rest_name = entity[x[1]:]
        local_list=[]
        local_list.append(name); local_list.append(unit); local_list.append(price)
        name_unit_price_separated.append(local_list)        

print('------  Shpno  --------')
print(name_unit_price_separated)
shpno = name_unit_price_separated
shpno_picked=[1]*len(shpno)
#for value in name_unit_price_separated:
#    print(value)

from prettytable import PrettyTable

master = ['cucumber', 'tomato', 'onion', 'garlic', 'ginger', ['potato', 'alu'], ['chilli', 'chili'], 'capsicum', ['potol','potal'], 'carrot', 'brinjal', 'chichinga', 'koliflower', 'broccoli', 'shak', 'lettuce', 'kochu', 'lemon', 'banana', 'papaya', 'potol', ['kumra', 'pumpkin'], ['pata', 'leaf'], ['aloe','alovera'], ['kopi', 'cabbage'], 'begun' ] #
#shpno = [['Mishti Kumra', 'kg', '45'], ['Lal Shak', 'ati', '10  6tk 4Off'], ['Tomato Lal', 'kg', '160'], ['Potol', 'kg', '60'], ['Tomato Green', 'Kg', '40'], ['Centella (Thankuni Pata', 'Per Piece', '4'], ['Bean (', 'Kg', ' 58'], ['Spinach (Palong Shak', 'Per Piece', '12'], ['Lemon (Lomba Lebu', 'Per Piece', '10'], ['Bitter Gourd (korola)', 'Kg', '60'], ['Water Spinach (Kolmi Shak', 'Per Piece', '10'], ['Taro Roots (Kochu', 'Per Piece', '40'], ['Green Papaya (Kacha Pepe)', 'Kg', '30'], ['Banana Gree', 'Per Piece', '8'], ['Lettuce (Ice Berg)', 'Kg', '650'], ['Carrot (Gajor)', 'Kg', '55'], ['Spinach (Data Shak', 'Per Piece', '11'], ['Snake Gourd (Chichinga)', 'Kg', '50'], ['Cherry Tomato (local)', 'Kg', '685'], ['Capsicum (Yellow)', 'Kg', '480'], ['Capsicum (Green)', 'Kg', '190'], ['Eggplant Begun (Long)', 'Kg', '42'], ['Eggplant Begun (Bottle Shape) (', 'Kg', ' 45'], ['Long Bean (Borboti)', 'Kg', '75'], ['Aloe Vera', 'Kg', '130'], ['Tomato (Round)', 'Kg', '75'], ['Cabbage (Red)', 'Kg', '180'], ['Onion Leaves (Peyaj Pata)', 'Kg', '80'], ['Chilli Green', 'Kg', '120'], ['Zucchini', 'Kg', '70'], ['Green Peas (Motor Shuti)', 'Kg', '190'], ['Okra (Dherosh)', 'Kg', '55'], ['Coriander Leaf (Dhone Pata)', 'Kg', '250'], ['Lettuce (Coral Shape', 'Per Piece', '55'], ['Capsicum (Red)', 'Kg', '480'], ['Chal Kumra', 'Kg', '50']]
#meena = [['Capsicum Green', '0.50 KG', ' 112.5'], ['CAPSICUM RED', '0.50 KG', ' 437.5'], ['CAPSICUM YELLOW', '0.50 KG', ' 437.5'], ['BABY CORN NON PROCESSED', '1  packet', '75'], ['CABBAGE BADACOPI LOCAL', 'Per Piece', '25'], ['LEMON GRASS CHINA', '0.50 KG', ' 160'], ['CORIANDER LEAF DHONIA LOCAL', '0.10 KG', ' 9'], ['LAL SHAK RED SPINACH', 'Per Piece', '8'], ['LETTUCE LEAF', '0.10 KG', ' 9'], ['MULA SHAK RADISH LEAF', 'Per Piece', '7'], ['PUDINA PATA PEPPERMINT', 'Per Piece', '25'], ['ORGANIC PUI MECHURI', '0.50 KG', ' 8'], ['GINGER CHINA', '1.00 KG', ' 145'], ['GINGER LOCAL', '1.00 KG', ' 95'], ['POTATO SEASONAL (NEW)', '1.00 KG', ' 26  271 off'], ['SHALGOM GREEN TURNIP', '1.00 KG', ' 25'], ['GARLIC INDIA', '1.00 KG', ' 95'], ['KOCHUR LOTI', '1.00 KG', ' 45'], ['KOCHUR CHARA', '1.00 KG', ' 50'], ['MULA RADISH', '1.00 KG', ' 17'], ['ONION LOCAL', '1.00 KG', ' 90'], ['ONION INDIAN', '1.00 KG', ' 65  8419 off'], ['POTATO RED SKIN', '1.00 KG', ' 35'], ['BEAT ROOT', '0.50 KG', ' 75'], ['Shosha Cucumber', '1.00 KG', ' 35'], ['POTATO DARK (JAM)', '1.00 KG', ' 35'], ['Begun Brinjal Green Round', '1.00 KG', ' 30'], ['BEGUN BRINJAL LONG', '1.00 KG', ' 40'], ['CARROT GAJOR LOCAL', '1.00 KG', ' 54'], ['GARLIC SINGLE CELL', '0.50 KG', ' 170'], ['GARLIC LOCAL', '1.00 KG', ' 85'], ['GREEN CHILI LOCAL', '0.10 KG', ' 57  6710 off'], ['LEMON ELACHI', 'Per Piece', '9'], ['ALOVERA LOCAL', 'Per Piece', '27'], ['GOURD LAU LOCAL', 'Per Piece', '55'], ['BANANA RAW KACHA KOLA', 'Per Piece', '8'], ['GREEN CHILI BOMBAY', 'Per Piece', '6'], ['LEMON KAGOJI LEMON CITRON', 'Per Piece', '9'], ['LEMON LOCAL', 'Per Piece', '9'], ['Papaya raw Kacha papaya)', '1.00 KG', ' 24'], ['PUMPKIN SWEET GOURD', 'Per Piece', '52'], ['PUMPKIN GREEN SWEET GOURD', 'Per Piece', '52'], ['TOMATO LOCAL', '1.00 KG', ' 60'], ['OLIVE LOCAL', '1.00 KG', ' 70'], ['POTAL PARBAL LOCAL', '1.00 KG', ' 55'], ['BEGUN BRINJAL TAL ', '1.00 KG', ' 59'], ['Brocoli Local', 'Per Piece', '38  5012 off'], ['Potato White', '1.00 KG', ' 16'], ['Carrot China', '1.00 KG', ' 120'], ['ONION LOCAL PREMIUM 2 KG', '1  packet', '192'], ['Onion Local Premium 5 Kg', '1  packet', '475'], ['Potato White Premium 2 Kg', '1  packet', '42'], ['Potato White Premium 5 Kg', '1  packet', '100'], ['TOMATO INDIAN', '1.00 KG', ' 110']]

x = PrettyTable(["Vegitable", "Shpno", "Meena"])
for index, value in enumerate(master):
    if isinstance(value, str):
        
        u = value.lower()
    
        shpno_single_row=''
        for index2, value2 in enumerate(shpno):
            if u in value2[0].lower():
                 shpno_single_row = shpno_single_row + str(value2) + '\n'
                 shpno_picked[index2] = 0
    
        meena_single_row=''
        for index2, value2 in enumerate(meena):
            if u in value2[0].lower():
                 meena_single_row = meena_single_row + str(value2) + '\n'
                 meena_picked[index2] = 0
    
        x.add_row([u.upper(), shpno_single_row, meena_single_row])

    if isinstance(value, list):
        shpno_single_row=''
        meena_single_row=''
        for u in value:
            u = u.lower()
        
            for index2, value2 in enumerate(shpno):
                if u in value2[0].lower():
                     shpno_single_row = shpno_single_row + str(value2) + '\n'
                     shpno_picked[index2] = 0
        
            
            for index2, value2 in enumerate(meena):
                if u in value2[0].lower():
                     meena_single_row = meena_single_row + str(value2) + '\n'
                     meena_picked[index2] = 0
        
        x.add_row([value[0].upper(), shpno_single_row, meena_single_row])

rest_shpno = ''
for index, value in enumerate(shpno_picked):
    if value == 1:
        rest_shpno = rest_shpno + str(shpno[index]) + '\n'

rest_meena = ''
for index, value in enumerate(meena_picked):
    if value == 1:
        rest_meena = rest_meena + str(meena[index]) + '\n'

x.add_row(['Other different', rest_shpno, rest_meena])
print (x)
