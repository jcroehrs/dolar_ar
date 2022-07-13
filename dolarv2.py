#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 12:06:37 2022

@author: jcroehrs
"""
import sys
import time
import requests        
from bs4 import BeautifulSoup


def VerDolarBcoProvincia():
    url = 'https://www.bancoprovincia.com.ar/web'
    #print('Sacando datos de  bancoprovincia.com.ar')
    pagina = requests.get(url)
    bs = BeautifulSoup(pagina.content, 'html.parser')


    Edolar = bs.find_all('div', class_='ft-dolar-bold currency-bar-line')
    Dolarv= str(Edolar[0])
    Dolarc= str(Edolar[0])
    av=Dolarv.find('Venta: ')
    bv=Dolarv.find('</div></div>')
    ac=Dolarc.find('Compra: ')
    bc=Dolarc.find('</div></div>')
    DolarVenta= Dolarv[av+7: bv]
    DolarCompra= Dolarc[ac+8: bc-42]

    DolarP = 'Dolar Banco Provincia Venta: {0} Compra: {1}'.format(DolarVenta,DolarCompra)
    return DolarP

def VerDolarDolarHoy():
    url = 'https://dolarhoy.com/'
    #print('Sacando datos de  dolarhoy.com/')
    pagina = requests.get(url)
    bs = BeautifulSoup(pagina.content, 'html.parser')


    Edolar = bs.find_all('div', class_='values')
    DolarCompra = str(Edolar[0])
    DolarVenta = str(Edolar[1])
    a=DolarCompra.find('Compra: ')
    b=DolarCompra.find('<class="value"></div></div></div')
    DolarC = DolarCompra[a+89: b-99]
    a=DolarVenta.find('Venta: ')
    b=DolarVenta.find('<class="value"></div></div></div')
    DolarV = DolarVenta[a+174: b-20]
    Dolar ='Dolar Blue Compra: {0} Venta: {1}'.format(DolarC, DolarV)
    #print(DolarV)
    return Dolar

dbp=''
ddh=''
while True:
    try:
        dbpt=VerDolarBcoProvincia()
        ddht=VerDolarDolarHoy()
        if dbp != dbpt or ddh != ddht :
            fecha=time.strftime("%d/%m/%y")
            hora=time.strftime("%H:%M:%S")
            print('Fecha:{0} Hora:{1}'.format(fecha, hora))
            print('{0} {1}'.format(dbpt,ddht))
            dbp=dbpt
            ddh=ddht
            print('------------------------------')
            f = open('dolar.txt','a')
            f.write('\nFecha:{0} Hora:{1}'.format(fecha, hora))
            f.write('\n{0} {1}'.format(dbpt,ddht))
            f.write('\n------------------------------')
            f.close()
            time.sleep(90)
    except KeyboardInterrupt:
        print(' Saliendo del programa...!')
        break
    
    except requests.exceptions.ConnectionError:
        print('error al intertar conectar...!')
        
    except:
        print("Error Inesperado ...! :", sys.exc_info()[0])
        
        

        
