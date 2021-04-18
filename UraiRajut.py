def urai(word):
    huruf = '' #list kosong untuk menampung hasil looping 1
    char_2 = ''  #list kosong untuk menampung hasil looping 2
    for i in range(1,len(word)+1): #untuk looping pertama
        huruf = huruf + word[0:i]
    for j in range(len(word)-1): #untuk looping kedua
        char_2 = char_2 + word[j:]
    return huruf + char_2



print(urai('Code'))
print(urai('Python'))

