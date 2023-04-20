x = 1 #1
cont = 0 #0
while x < 3: #True #True #False
    y = 0 #0 #0
    while y <= 4: #True #True #True #True #True #False (x2)
        # Iteração #1 + 1 + 1 + 1 + 1 (x2) #10
        y = y + 1 #1 #2 #3 #4 #5
    x = x + 1 #2 #3



fora = 5 #5
while fora > 0: #True #True
  dentro = 0 #0 #0
  while dentro < fora: #True #True #True #True #True #False #True #True #True #True
    print("oi") #1 + 1 + 1 + 1 + 1 + 1
    dentro = dentro + 1 #1 #2 #3 #4 #5 #1 
  fora = fora - 1 #4
#15



    tab = 1
    while tab <= 10:
        print("Tabuada do", tab, ":", end="\t")
        i = 1
        print(tab*i, end = "\t")
        i = i + 1
        print()
        tab = tab + 1
        #não
  
    tab = 0
    while tab < 10:
        tab = tab + 1 #1
        i = 0 #0
        while i < 10: #True
            i = i + 1 #1 #2
            print(tab,"x",i,"=",tab*i) #1 x 1 = 1 #1 x 2 = 2
        print()
        #não?

    tab = 1 #1
    i = 1 #1
    while tab <= 10 and i <= 10:
        print(tab,"x",i,"=",tab*i) #1 x 1 = 1
        i = i + 1 #2
        tab = tab + 1 #2
    print()
    #não

    tab = 1 #1
    while tab <= 10: #True
        i = 1 #1
        while i <= 10: #True
            print(tab,"x",i,"=",tab*i) #1 x 1 = 1
            i = i + 1 #2
        print()
        tab = tab + 1
        #sim

    tab = 1
    while tab <= 10:
        print("Tabuada do", tab, ":", end="\t")
        i = 1
        while i <= 10:
            print(tab*i, end = "\t")
            i = i + 1
        print()
        tab = tab + 1
        #sim


        
x = 2 #2
cont = 0 #0
while x >= 0: #True
    y = 0 #0
    while y >= 4:#False
        #comando qualquer #nenhumaVez
        y = y + 1
    x = x - 1



x = 2 #2
cont = 0 #0
while x >= 0: #True
    y = 0 #0
    while y <= 4: #True
        #comando qualquer #1 +
        y = y - 1 #-1 #infinitasVezes
    x = x - 1    



i = 0 #0
while i < 3: #True #True #True #False
  j = 0 #0 #0 #0
  while j < 3: #True #True #True #False (x3)
    #expressão # # # (x3)
    j = j + 1 #1 #2 #3 (x3)
  i = i + 1 #1 #2
  #print(3 * i + j + 1, end=" ")
