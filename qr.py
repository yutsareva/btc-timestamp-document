import qrcode
from PIL import Image


def create_qr_code(tx_id):
    url = f"https://www.blockchain.com/search?search={tx_id}"
    img = qrcode.make(url)
    file_name = f"{tx_id[:5]}.png"
    img.save(file_name)
    print(f"QR code for tx '{tx_id}' was saved to file {file_name}")
    Image.open(file_name).show()


