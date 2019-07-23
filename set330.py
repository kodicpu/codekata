hrs1,mins1=input().split()
hrs2,mins2=input().split()
hrs1=int(hrs1)
hrs2=int(hrs2)
mins1=int(mins1)
mins2=int(mins2)
totmin1=(hrs1*60)+mins1
totmin2=(hrs2*60)+mins2
totmin3=abs(totmin1-totmin2)
hrs3=totmin3//60
mins3=totmin3%60
print (str(hrs3)+" "+str(mins3))
