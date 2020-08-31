
class Message :

    def read_text (self):

        self.text = input("Enter the text: ")
        self.key = input("Enter the keyword: ")

    #def print(self):
    #    print("Text: " + self.text +  " Key: " + self.key)

    def encryption(self): 

        encrypted_text = ''
        key_int = [ord(i) for i in self.key] 
        text_int = [ord(i) for i in self.text] 

        for i, j in enumerate(text_int):
            if j == 32:
                encrypted_text = encrypted_text + ' '
            else: 
                c = (j + key_int[i % len(self.key)]) % 26
                encrypted_text = encrypted_text + chr(c + 65)

        self.encrypted_text = encrypted_text
                
        return encrypted_text

    def decryption(self):
        decrypted_text = ''
        key_int = [ord(i) for i in self.key] 
        encrypted_text_int = [ord(i) for i in self.text] 

        for i, j in enumerate(encrypted_text_int):
            if j == 32:
                decrypted_text = decrypted_text + ' '
            else: 
                c = (j - key_int[i % len(self.key)]) % 26
                decrypted_text = decrypted_text + chr(c + 65)

        self.decrypted_text = decrypted_text
                
        return decrypted_text


class Menu :

    def __init__(self):
        self.print_menu()


    def print_menu(self):
        message = Message()
        message.read_text()

        de = input("Press c for encryption or d for decryption: ")

        if de == 'c' : 
            print("Encrypted message: ", message.encryption())

        else:
            if de == 'd' :
                print("Decrypted message: ", message.decryption())

########################

menu = Menu()















