def use_qrcode_gen():
    #using py -m pip install qrcode, install the qrcode generator library from pypi 
    #if it doesn't work, install pillow using py -m pip install pillow
    import qrcode

    website = input("Enter the text or URL for the QR code: ").strip()
    filename = input("Enter the filename: ").strip()
    fill_color = input("Enter the fill color you want: ")
    back_color = input("Enter the back color you want: ")

    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(website)
    qr_image = qr.make_image(fill_color = fill_color, back_color = back_color)

    qr_image.save(filename)
    print(f"QR code saved as {filename}")
    return