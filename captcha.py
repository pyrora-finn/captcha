from captcha.image import ImageCaptcha
import random
import string

def generate_captcha_text(length=5):
    # Generiert einen zufälligen Text aus Buchstaben und Zahlen für das CAPTCHA
    letters_and_digits = string.ascii_uppercase + string.digits
    captcha_text = ''.join(random.choice(letters_and_digits) for _ in range(length))
    return captcha_text

def create_captcha_image(captcha_text):
    # Erstellt ein CAPTCHA-Bild mit dem Text
    image = ImageCaptcha(width=280, height=90)
    data = image.generate(captcha_text)
    image_path = f"captcha_{captcha_text}.png"
    image.write(captcha_text, image_path)
    return image_path

def verify_captcha(user_input, actual_text):
    # Verifiziert, ob der Benutzereingabe mit dem CAPTCHA-Text übereinstimmt
    return user_input.upper() == actual_text.upper()

# Generiere ein CAPTCHA
captcha_text = generate_captcha_text()
image_path = create_captcha_image(captcha_text)
print(f"Captcha generated and saved as {image_path}")

# Frage den Benutzer, das CAPTCHA einzugeben
user_input = input("Please enter the CAPTCHA: ")

# Überprüfe das CAPTCHA
if verify_captcha(user_input, captcha_text):
    print("Verification successful!")
else:
    print("Verification failed. Please try again.")
