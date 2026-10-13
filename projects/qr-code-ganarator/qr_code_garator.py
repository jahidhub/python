import qrcode
import os


def get_file_name():
    # Ask for the file name and replace spaces with dashes
    name = input("Enter the file name: ").lower().strip()
    name = name.replace(" ", "-")

    # Check for the extension
    if not name.endswith((".png", ".jpg", ".jpeg")):
        name += ".png"

    return name


def ganarate_qr():
    data = input("Enter the text and url: ").strip()
    file_name = get_file_name()

    #   multiFolderCreate
    # if file_name.endswith((".png", ".jpg", ".jpeg")):
    #     new_folder, extension = os.path.splitext(file_name)
    #     print(new_folder)
    # folder_name = new_folder


    # SingleFolder
    folder_name = "qr-images"

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    path = os.path.join(folder_name, file_name)
    qr = qrcode.QRCode(
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(path)
    print(f"QR saved as {file_name}")


ganarate_qr()
