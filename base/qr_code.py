import qrcode as QR_GEN

def gen_qrcodes(qr_encodalbe_data):
    img= QR_GEN.make(qr_encodalbe_data)
    img.save('host.png')
    
gen_qrcodes("www.google.com")