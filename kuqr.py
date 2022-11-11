import qrcode
NUM =8080520097, "kupakwashe mapuranga"

password = qrcode.make(NUM)

password.save("My details.jpg")