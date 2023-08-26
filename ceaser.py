


class Ceaser:
    

    def Main(self):
        banner = """
             ,-.                        ,-.             .       
            /                          /                |       
            |    ,-. ,-: ,-. ,-. ;-.   |    ;-. . . ;-. |-  ,-. 
            \    |-' | | `-. |-' |     \    |   | | | | |   | | 
             `-' `-' `-` `-' `-' '      `-' '   `-| |-' `-' `-' 
                                                `-' '           
        """

        menu = """
                            |-----------------|
                            |   1-Encrypt     |
                            |   2-Decrypt     |
                            |-----------------|
        """
        
        while True:
            print(banner)
            print(menu)

            
            choice = input(">>")

            if choice == "1":
                try:
                    txt = input("Enter Message : ")
                    key = input("Enter Key (Number) : ")

                    keyToInt = int(key)

                    self.Encrypt(key=keyToInt, msg=txt)
                except ValueError: 
                    print("Key is not number, please try again !! ")
            elif choice == "2":
                try:
                    txt = input("Enter Crypted Message : ")
                    key = input("Enter Key (Number) : ")

                    keyToInt = int(key)

                    self.Decrypt(key=keyToInt, msg=txt)
                except ValueError: 
                    print("Key is not number, please try again !! ")
            else:
                print("This choice not available !!, try again")  
    


            


    def Encrypt(self, key, msg):
        __alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        __result = ""


        messasge = msg.upper()

        for letter in messasge:
            # Check letter in alpha !
            if letter in __alpha:

                # Find index
                letter_index = (__alpha.find(letter) + key) % len(__alpha)

                __result =  __result + __alpha[letter_index]
              
            else:
                __result = __result + letter
        
        print(f"\nOriginal Text : {messasge}\nEncrypted Text: {__result}\n")
    
    def Decrypt(self, key, msg):
        __alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        __result = ""


        messasge = msg.upper()

        for letter in messasge:
            # Check letter in alpha !
            if letter in __alpha:

                # Find index
                letter_index = (__alpha.find(letter) - key) % len(__alpha)

                __result =  __result + __alpha[letter_index]
              
            else:
                __result = __result + letter
        
        print(f"\nOriginal Text : {messasge}\nDecrypted Text: {__result}\n")


app = Ceaser()
app.Main()