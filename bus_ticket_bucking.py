class User:
    def __init__(self,name,password) -> None:
        self.name = name
        self.password = password

class Bus:
    def __init__(self,coach,driver,arrival,departur,from_des,to) -> None:
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departur = departur
        self.from_des = from_des
        self.to = to

        self.seat = ['Empty' for i in range(20)]

  #  def __repr__(self) -> str:
     #   print(f'coach:{self.coach}\n driver:{self.driver}\n arrival:{self.arrival} \n departur:{self.departur} \n From:{self.from_des}\n To:{self.to}')
class Company():
    total_bus = 5
    total_bus_list = []

    def install(self):
        bus_no = int(input("Enter bus number: "))
        fleg = 1

        for w in self.total_bus_list:
            if w['coach']==bus_no:
                print("This bus is already exist.")
                flag=0
                break
                

        if fleg:
            
            driver = input("Enter driver's name: ")
            arrival = input("Enter arrival time: ")
            departur = input("Enter Departure time: ")
            from_des = input("Enter from start: ")
            to = input("Enter destination name: ")

            self.bus = Bus(bus_no,driver,arrival,departur,from_des,to)
            self.total_bus_list.append(vars(self.bus))
            print("Bus successfully installed\n\n")


class Counter(Company):
    user_list = []

    def reservation(self):
        bus_no = int(input("Enter bus no: "))
        flag =0

        for w in self.total_bus_list:
            if w['coach'] == bus_no:
                flag+=1
                name = input("Enter your name: ")
                seat_no = int(input("Enter seat number: "))

                if seat_no > 20:
                    print("Sorry. Bus has only 20 seats.\n")
                    
                    break
                elif w['seat'][seat_no-1]!= 'Empty':
                    print("This seat is alrady booked.\n\n")
                    
                    break

                else:
                    w['seat'][seat_no-1] = name
                    print("Seat booked successfully")
                    
                    break
        if flag==0:
            print("NO bus available.\n\n")

    
    #-------------- show funciotn ----------------

    def show(self):
        bus_no = int(input("Enter the bus number: "))
        flag = 1
        for w in self.total_bus_list:
            if w['coach'] == bus_no:
                flag=0

                print('*'*50)
                print()
                print(f'{' '*10} {'#'*10} Bus Info {'#'*10}')

                print(f'Bus Number: {bus_no}\t\t Driver: {w['driver']}\n Arrival: {w['arrival']}\t\tDeparture:{w['departur']}\n')
                print(f'Start from :{w['from_des']}\t\t Destination:{w['to']}')
                print()

                a=1
                for i in range(5):
                    for j in range(2):
                        print(f'{a}. {w['seat'][a-1]} ' ,end="\t")
                        a +=1

                    print()

                    for j in range(2):
                        print(f'{a}. {w['seat'][a-1]}',end="\t")
                        a +=1
                    print()
                print('*'*50)

        if flag:
            print("No bus available here.\n")
    
    #------------- get user -------------------

    def get_user(self):
        return self.user_list   

    #-------------  create  account --------------

    def create_accout(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        new_user = User(name,password)
        self.user_list.append(vars(new_user))

        print("Account created successfully.")


    def available_buses(self):
        if len(self.total_bus_list)==0:
            print("No Bus available.")
        else:
            for w in self.total_bus_list:
                print('*'*50)
                print()
                print(f'{' '*10} {'#'*10} Bus Info {'#'*10}')

                print(f'Bus Number: {w['coach']}\t\t Driver: {w['driver']}\n Arrival: {w['arrival']}\t\tDeparture:{w['departur']}\n')
                print(f'Start from :{w['from_des']}\t\t Destination:{w['to']}')
                print()


while True:
    b = Counter()
    print('1.Create account: \n 2.Login account: \n 3.Exit')

    user_input = int(input('Enter your chouce: '))
    if user_input== 3:
        break
    elif user_input==1:
        b.create_accout()
    else:
        
        name = input('Enter your name: ')
        password = input('Enter you password: ')
        isAdmin = False
        flag = 0

        if name == 'admin' and password=='admin':
            isAdmin = True
        if isAdmin==False:
            for user in b.get_user():
                if user['name']==name and user['password']== password:
                    flag =1
                    break

            if flag:
                while True:
                    print(f"{' '*10} Welcome to bus tickit booking system .")
                    print('1.Avalilable Bus\n 2.Show bus info\n 3.Reserve\n 4.Exit\n')
                    a = int(input("Enter yur choice: "))
                    if a==4:
                        break
                    elif a==1:
                        b.available_buses()
                    elif a==2:
                        b.show()
                    elif a==3:
                        b.reservation()

            else:
                print("No user name found. Who are you? ")
        else:
            while True:
                print("Welcome admin view")
                print("1.Add new bus \n 2.check available buses\n 3.show bus info \n 4.exit")
                a = int(input("Enter your choice: "))
                
                if a==1:
                    b.install()
                elif a==2:
                    b.available_buses()
                elif a==3:
                    b.show()
                else:
                    break




           



# sylhet_counter = Counter()
# sylhet_counter.install()
# sylhet_counter.reservation()
# sylhet_counter.show()
# sylhet_counter.get_user()
# sylhet_counter.create_accout()
# sylhet_counter.available_buses()
    

# bus = Bus(2,"shorif",'33pm','33am','Sylhet','Dhaka')
# print(bus)

# phitron = Company()
# phitron.install()