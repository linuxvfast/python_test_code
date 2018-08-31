import random
i = 0
while i < 10000:
    adm1 = str(random.randint(100000000,999999999))
    adm2 = str(random.randint(1000000000000,9999999999999))
    adm3 = str(random.randint(1000,9999))
    data=adm1+'  '+adm2+'  '+adm3
    with open('fixed_width-1M.txt','a') as f:
        f.write(data+'\n')
    i= i+1
    if i == 10000:
        break

