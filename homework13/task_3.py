import re
class Validator():

    
    rlogin = r"^[A-Za-z](?=.{5,9}$)"
    remail = r"^[\w.-]+@([\w-]+\.)+[\w-]{2}$"
    rpassword = r"(?=.*[a-z])(?=.*[A-Z])(?=.*[^A-Za-z0-9])(?=.{8,})"
    @staticmethod
    def  validate(user_data:tuple)->bool:
        login,email,password = user_data
        
        if re.search(Validator.rlogin,login) and re.search(Validator.remail,email) and re.search(Validator.rpassword,password):
            return True
        else:
            return False




val = Validator()
print((val.validate(('mish111','misha@tut.by','Misha1234?'))))
