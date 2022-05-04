# kullanıcı adı ve şifre ile giris yapıp yeni pence açıyorsun ve açılan penceredeki text box a yazdığın
# yazıyı kaydet butonuyla txt dosyasına kaydediyorsun çıkış butonuyla çıkıyorsun pencereden 
# tekrar giris yapabilirsin yazmak için
# her kaydet dediğinde yeni bölüm oluşturuyor txt dosyasında

# id: koray
# password: 123


from tkinter import *
from datetime import datetime

root = Tk() #ana pencerieyi oluşturuyorsun
root.geometry("300x200") # ana pencere boyutu
root.title("Kullanıcı Girişi") # pencere title ı


# birden fazla pencere açılmasını istemediğim için counter oluşturuyorum
global counter
counter = 1

# write fonksyonu ile text box içerisindeki yazıları txt dosyasına ekliyorsun
def write(text):
	with open("günlük.txt", "a+", encoding="UTF-8") as file:

		#önce tarihi yazdırıyor altına kendi yadıkların ve altına da ayırmak için tirelerden çişgi oluşturuyor ve txt ye ekliyor
		file.write(f"{datetime.now()}\n\n {text}\n----------------------------------------------------------------------------------\n")
		file.close()
	print("Başarıyla Kaydedildi!")


# giris butonuna basıldığında buraya girecek
def giris():
	# eğer bilgiler doğru girildiyse giriş yapacak ve diğer işlemler çalışacak
	if ent_id.get() == "koray" and ent_pass.get() == "123":
		ent_pass.delete(0,len(ent_pass.get()))# entryden password siler 
		ent_id.delete(0,len(ent_id.get()))# entryden id siler

		# giris basarılı olduğu için hata mesajını labeldan siliyorum
		label.config(text="")
		
		print("Giris Yapıldı!")
		# counter global bir değişken oldugu için burada global olarak ekliorum
		global counter

		# counter zaten 1 ve butona bastığında pencere açılacak ama counter 2 olacak ve tekrar giris butonuna bastığında yeni pencere açılmayacak
		if counter < 2: 
			main = Toplevel() # yeni pencere oluşturuyor
			main.geometry("910x520")
			main.title("GÜNLÜK")

			def counter_reset(): # çıkış butonuna tıklayınca counter sıfırlanacak ve pencere kapanacak ve main local değisken oldugu icin fonsyonu iceri yazdım
				global counter
				counter = 1
				main.destroy() # main penceresini kapatır

			lable1 = Label(main, text="Günlüğünü aşağıya yazabilirsin..")
			lable1.place(x=50, y=20)

			# günlüğü yazabileceğin bir text box oluşturur
			textBox = Text(main, height=25, width=100)
			textBox.place(x=50, y=50)

			# kaydet butonu 
			btn1=Button(main, text="Kaydet", command=lambda:write(textBox.get(1.0, END)))
			btn1.place(x=50,y=460,width=100)
			# çıkış butonu

			btn2=Button(main, text="Çıkış", command=lambda:counter_reset())
			btn2.place(x=175,y=460,width=100)

			counter += 1
	else:
		# eğer hatalı giris yapılırsa label text i degisecek
		label.config(text = "Hatalı giris yaptın! Tekrar Dene!", fg="darkred")


# entryleri tanımlayan lable lar
lable1 = Label(root, text="User ID:")
lable1.place(x=30, y=30)
lable2 = Label(root, text="Password:")
lable2.place(x=30, y=60)

# hatalı giris yapılırsa bu label a yazdırılacak
label = Label(root, text="")
label.place(x=100, y=140)


# kullanucu adi ve sifre yi gireceğin entry ler
ent_id = Entry(root)
ent_id.place(x = 100, y=30, width=150)
ent_pass = Entry(root)
ent_pass.place(x = 100, y=60, width=150)


#giris yapmak için buton oluşturuyorsun
btn1=Button(root, text="Giris", command=lambda:giris())
btn1.place(x=100,y=90,width=100)


root.mainloop()