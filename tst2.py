class usr:
    name =' '
    password = ' '
    login = False

    def login(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        if name == self.name and password == self.password:
             login = True
             print("Login success")
        else:
            print("Login Failed")
            quit()

    def logout(self):
        login = False
        print("User logged out")

    def is_login(self):
        if self.login():
            return True
        else:
            return False

    def profile(self):
        if self.is_login():
            print('Name: ', self.name , 'password: ', self.password )
            
            #student management system's code star here
        students = [['Harry', 37.21], ['Berry', 23.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
        name = input("Enter your name: \n")
        for item in students:
            if name == item[0]:
                if item[1] > 40:
                    print(f"You score first\nName: {name}\nScore : {item[1]} ")
                if item[1] > 35 and item[1] < 40:
                    print(f"You score second\nName: {name}\nScore : {item[1]} ")
                if item[1] < 30:
                    print(f"{name} You are failed! Better Luck next time!!\nYour score is: {item[1]} ")

    def about_us(self):
        a = input("what do know about us?\n1.about us"
                  "\n2.About this management system\nChose anything>>")

        choice = ['1', '2']
        if a in choice[0]:
            print("We are a cyber security expert, we work for any corporation industry ")
        if a in choice[1]:
            print("It's a simple student management system, developed by one of our best\nsenior member Emon Joy")
            print("LOL Just kidding!!!")



# making user
user1 = usr()
user1.name = "Joy"
user1.password ="1234"

# user method calling
# user1.login()

user1.profile()
user1.about_us()










