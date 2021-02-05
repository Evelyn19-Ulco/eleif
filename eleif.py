# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:15:49 2021

@author: DELL
"""

acl=int(input("Ingrese el numero de ACL: "))
if acl>=1 and acl <=99:
    print("es una ACL estandar")
    
elif acl>=100 and acl <=199:
     print("es una ACL extendida")
else:
    print('No es un número de ACL válido')