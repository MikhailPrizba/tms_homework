class Cipher():
    string1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    string2 = 'CRYPTOABDEFGHIJKLMNQSUVWXZ'
    def __init__(self) -> None:
        pass

        
    
    def encode(self, your_string:str )-> str:
        string3 = ''
        for i in your_string:
            if i in Cipher.string1:
                string3 += Cipher.string2[Cipher.string1.find(i)]
            elif i in Cipher.string1.lower():
               string3 += Cipher.string2[Cipher.string1.lower().find(i)].lower() 
            
            else:
                string3 += i
        return string3

    def decode(self, decode_string: str)-> str:
        string3 = ''
        for i in decode_string:
            if i in Cipher.string2:
                string3 += Cipher.string1[Cipher.string2.find(i)]
            elif i in Cipher.string1.lower():
               string3 += Cipher.string1[Cipher.string2.lower().find(i)].lower() 
            
            else:
                string3 += i
        return string3

cipher = Cipher()
print(cipher.encode("Hello world"))
print(cipher.decode("Fjedhc dn atidsn"))