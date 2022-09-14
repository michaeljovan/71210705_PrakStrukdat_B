rangedata = int(input("Masukkan range data : ")) 
dict = {} 
for i in range(rangedata) : 
    if i%2 == 0 : 
        if i != 0 : 
            fact = 1 
            for f in range(2,i+1) : 
                fact *= f 
            dict[i] = fact 
        else : 
            dict[i] = 1 

print(dict)
data= int(input("Data ditampilkan : "))
if data in dict : 
    print(dict[data]) 
else : 
    print("Data tidak ditemukan")