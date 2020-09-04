
class Message :

    def read_text (self):

        self.text = input("Enter the text: ")
        self.key = input("Enter the keyword with upper case: ")

    def encryption(self): 

        d = ord('a') - ord('A')
        encrypted_text = ''
        key_int = [ord(i) for i in self.key] 
        text_int = [ord(i) for i in self.text] 

        for i, j in enumerate(text_int):
            if j >= ord('A') and j <= ord('Z'): 
                c = (j + key_int[i % len(self.key)]) % 26
                encrypted_text = encrypted_text + chr(c + ord('A'))

            else:
                if j == ord(' '):
                    encrypted_text = encrypted_text + ' '

            if j >= ord('a') and j < ord('z'): 
                c = (j + key_int[i % len(self.key)] - d) % 26
                encrypted_text = encrypted_text + chr(c + ord('a'))

            else:
                if j == ord(' '):
                    encrypted_text = encrypted_text + ' '

        self.encrypted_text = encrypted_text
                
        return encrypted_text

    def decryption(self):

        d = ord('a') - ord('A')
        decrypted_text = ''
        key_int = [ord(i) for i in self.key] 
        encrypted_text_int = [ord(i) for i in self.text] 

        for i, j in enumerate(encrypted_text_int):
            if j >= ord('A') and j <= ord('Z'): 
                c = (j - key_int[i % len(self.key)]) % 26
                decrypted_text = decrypted_text + chr(c + ord('A'))

            else:
                if j == ord(' '):
                    decrypted_text = decrypted_text + ' '

            if j >= ord('a') and j < ord('z'): 
                c = (j - key_int[i % len(self.key)] - d) % 26
                decrypted_text = decrypted_text + chr(c + ord('a'))

            else:
                if j == ord(' '):
                    decrypted_text = decrypted_text + ' '

        self.decrypted_text = decrypted_text
                
        return decrypted_text


class Menu :

    def __init__(self):
        self.print_menu()


    def print_menu(self):
        message = Message()
        message.read_text()

        case = input("Press E for encryption or D for decryption: ")

        if case == 'E' : 
            print("Encrypted message: ", message.encryption())

        else:
            if case == 'D' :
                print("Decrypted message: ", message.decryption())

########################

menu = Menu()















