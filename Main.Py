meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            }
print(meme_dict)

# dictionary
dictionary = { "Skibap Toilet" : "Brainrot/Cringe in People Eyes",
                "Meme" : "Funny' / LoL in People Eyes",}
print(dictionary)

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys() or dictionary.keys():
    print ('the meaning of',word)
    print (word,'is',meme_dict[word])
else:
    print('Nothing')
