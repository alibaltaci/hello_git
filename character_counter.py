# Character Counter

# Adımlar:

# 1- Git üzerinden character_counter.py scriptini oluştur, kontrol et ve kaydet.
# --> type nul> character_counter.py (oluşturuldu)
# --> git add *
#--> git commit -m "character_counter.py dosyası oluşturuldu."
# --> dir (kontrol edildi)



# 2- Pycharmda character_counter fonksiyonunu oluştur.

def character_counter():
    """
    Note: spaces also count as characters.

    :return:
    """
    print("Note: spaces also count as characters.")
    txt = input("Enter text: ")
    print(txt, "text consists of {} characters".format(len(txt)))

character_counter()



# 3- git üzerinden değişiklikleri kontrol et.
# --> git status



# 4- git üzerinden değişiklikleri kaydet.
# --> git add *



# 5- not ekle.
#--> git commit -m "character_counter fonksiyonu tanımlandı ve içerik oluşturuldu."



# 6- Değişiklikleri git üzerinden github'da bulunan hello_git reposununa kaydet.
# --> git push origin master

