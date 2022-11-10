import secrets
chars = 'qwertzuiopüasdfghjklöäyxcvbnmQWERTZUIOPÜASDFGHJKLÖÄYXCVBNM1234567890!"§$%&/()='

def create(number_of_passwords, pass_length):
    for i in range(number_of_passwords):
        list = []
        for i in range(pass_length):
            select = secrets.choice(chars)
            list.append(select)
        l = ''.join(list)
        print(l)
    return l

create(int(5),int(20))