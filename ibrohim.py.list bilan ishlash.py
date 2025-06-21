# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 09:08:10 

MUALLIF IBROHIM
@author: 
    
    
    
"""


#telephons = ["samsung","vivo","poco","iphone","asus"]
#narxlar = [1000,15000,45000,63000,20000]
#arzon =min(narxlar)
#qimmat=max(narxlar)
#jami=sum(narxlar)
#print("Eng arzon narx",arzon,".Eng qimmati",qimmat,".Jami summa:",jami)

#toys = ('cars','bus','balun','bear')

# FOR SIKL BBILAN TANISHUV 9 dars

#mehmonlar = ["ASILBEK","JAVOHIR","RUSLAN","AMIR"]
#for mehmon in mehmonlar:
 #   print(f"Hurmarli {mehmon},seni va oila a'zolaringizni10-iyun kuni mexmonga taklif qilamiz ")
 #   print("Hrmat bilan paloncheyevlar oilasi\n")
    

#sonlar = list(range(1,11))
#for son in sonlar:
 #   print(f"{son} ning kvadrati {son**2} ga teng bo'ladi")
    
#sonlar =list(range(11))
#sonlar_kvadrati=[]
#for son in sonlar:
#    sonlar_kvadrati.append(son**2)
    
#print(sonlar)    
#print(sonlar_kvadrati)
#
  
    
#doslar = []    
#print("5 ta eng yaqin do'stingizni kim?")
#for n in range(5):
 #   doslar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
#print(doslar)
 

# DARS 10 if 

#ilovalar = ["watsapp","netfliks","aka","telegram","fasebook","galareya"] 
#for ilova in ilovalar:
   # if ilova == 'bmw':
  #      print(ilova.upper())
 #   else:
#        print(ilova.title())
    

#ism =input("Isming nima?\n>>>") 
#if ism.lower() != 'ibrohim':
 #   print(f" Uzr, kechirasiz {ism.title ()}  biz Ibrohim ni kutayabmiz.")
#else:
#    print("Salom Ibrohim")
    



#avob = float(input("12x6 nechi bo'ladi?>>>"))
#f javob !=72:
 #   print("javob xato")
#lse:
 # print("javob to'g'ri")


            
#t_yil =int( input("Salom tug'ilgan yilingizni kiriting\n>>>>") )    
#yosh = 2025 -t_yil

#print("Siz ",yosh,"yoshda ekansiz")

#print("tashrifingiz uchun raxmat\n Agar yana yoshingizni bilmoqchi bo'lsangiz marxamat f5 ni bosing")




#IF ELSE BUYRUQ APERATORI
    
  #  if ilova == 'bmw':  agar shu shunga teng bo'lsa
   #      print(ilova.upper())
  #   else:aks holda shu buyruq bajarilmasa 
 #        print(ilova.title())  manabu bajarilsin
 
# mana bu belgi == mi yani shunga reng mi degan manoni bildiradi  ism =='ibrohim' True yoki ism =='vv' False


#ism =input("Isming nima?\n>>>") 
#if ism.lower() != 'ibrohim':
#    print(f" Uzr, kechirasiz {ism.title() } biz Ibrohim ni kutayabmiz")
#else :
#    print("Salom",ism,"yaxshimisiz")
 
 
 
 
#yosh = int(input("Yoshingizni tasdiqlang  siz 18 yoshda kattamisiz\n>>>>"))
#if yosh>=18:  
   ## print("Xush kelibsiz kirishingiz mumkin")
  #  print("SHaxsingizni tasdiqlang")
 #   print("EMAIL manzil,yoki Telefon raqamingizni kiriting\n>>>") 
#
#    print("Kirishingiz mumkin")

#else:
 #   print("Kechirasiz kirish taqiqlanadi!")
#    print("Siz 18 yoshdan kichik ekanziz sizni kirishingi taqiqlanadi")
 
 

#login =input("Yangi login kiriting:\n>>>")
#if len(login)>=8:
#    print("Login kamida 8ta harf ,(A-z ) ,(belgi @ ) raqam (1,2,3,) lardan ibborat kam bo'lmasligi kerak")
#else:
#    print("Xato belgilar soni 8 tadan kam")
 
 

#yil =int(input("Tug'ilgan yilingizni kiriting:>>>"))
#if 2025 -yil<18:
 #   print(f"Yoshingiz {2025-yil} da ekan.")
#    print("Kirish taqiqlanadi!")
#else:
  #  print(f"Siz {2025-yil} yoshda ekansiz kirishingiz mumkin")
 #   print("Velcome")
#    print("Xush kelibsiz")



#  IF  ELIF ELSE APERATORLARI

#yosh = int(input("Yoshingiz nechida? "))
#if yosh<=12:
 #   narx = 0
#elif yosh<=18:
 #   narx = 5000
#else:
 #   narx = 10000
          
#print(f"Sizga kirish {narx} ming so'm")


 #OR YOKI AND VA 
#kun = input('bugun kun nima?>>>')
#if kun.lower()=='shanba'or kun.lower()=='yakshanba':
 #   print("Bugun dam olish kuni")
#else:
#    print("Bugun ish kuni ")





#kun = input("Bugun kun nima?")
#harorat = float(input("Havo harorati qanday?"))

#if (kun.lower()=='yakshanba'or kun.lower()=='shanba') and harorat>=30:
 #   print("CHo'milishga boramiz")
#elif kun.lower()=='yakshanba' and harorat<30:
 #   print("uyda qolib dam olamiz")
#




#narx = 20000
#choy = True
#non = True
#osh=True
#salat=False
#pepsi=True

#if choy:
 #   print("mijoz choy oldi.")
 #   narx =narx+5000
    
#if non:
 #  print("mijoz non oldi.")    
  # narx =narx+6000
#   
#if osh:
 #   print("mijoz osh oldi.")
  #  narx =narx+10000
    
#if salat:
  #  print("mijoz salat oldi")
 #   narx =narx+60000
    
#if pepsi:
 #   print("mijoz salat oldi")    
  #  narx=narx+16000
    
#print(f"jami {narx} so'm")    



#menu = ['somsa','norin','osh','katishka','quymoq']
#ovqat = input("Nima ovqat yemoqchisiz?>>>")

#if ovqat.lower() in menu:
 #   print("  Buyutmangiz qabul qilindi Buyurtma tayyor qilinmoqda")
    
#else:
 #   print("Afsuski bizda unday ovqat yo'q")    
    
    

#telefonlar = ['iphone','samsung','redmi','poco','asus','infinix']
#buyurtmalar = ['samsung','tecno','vivo','fox','iphone']

#for gajet in buyurtmalar:
   #if gajet in telefonlar:
   #    print(f"Bizda {gajet} telefonlar bor")
  # else:
   #   print(f"kechirasiz bizda {gajet} telefonlar yo'q")
           
       
       

















  