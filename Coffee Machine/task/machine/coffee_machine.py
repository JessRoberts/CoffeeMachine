class Coffee:
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550

    def __init__(self):
        self.user_choice = ()
        self.start()

    def start(self):
        while True:
            user_wants = input('Write action (buy, fill, take, remaining, exit):')
            print()
            if user_wants == 'buy':
                self.user_choice = input("What do you want to buy? "
                                         "1 - espresso, 2 - latte, 3 - cappuccino, "
                                         "back - to main menu:")
                if self.user_choice == "back":
                    continue
                else:
                    self.buy()
            elif user_wants == 'fill':
                self.fill()
            elif user_wants == 'take':
                self.take()
            elif user_wants == 'remaining':
                self.remaining()
            elif user_wants == 'exit':
                break

    def remaining(self):
        print('The coffee machine has:')
        print(Coffee.water, 'of water')
        print(Coffee.milk, 'of milk')
        print(Coffee.beans, 'of coffee beans')
        print(Coffee.cups, 'of disposable cups')
        print(Coffee.money, 'of money')

    def espresso(self):
        if Coffee.water >= 250 and Coffee.beans >= 16 and Coffee.cups >= 1:
            print('I have enough resources, making you a coffee!')
            Coffee.water = Coffee.water - 250
            Coffee.beans = Coffee.beans - 16
            Coffee.cups = Coffee.cups - 1
            Coffee.money = Coffee.money + 4
        elif Coffee.water < 250:
            print('Sorry, not enough water!')
        elif Coffee.beans < 16:
            print('Sorry not enough coffee beans!')
        elif Coffee.cups < 1:
            print('Sorry, not enough cups!')

    def latte(self):
        if Coffee.water >= 350 and Coffee.milk >= 75 and Coffee.beans >= 20 and Coffee.cups >= 1:
            print('I have enough resources, making you a coffee!')
            Coffee.water = Coffee.water - 350
            Coffee.milk = Coffee.milk - 75
            Coffee.beans = Coffee.beans - 20
            Coffee.cups = Coffee.cups - 1
            Coffee.money = Coffee.money + 7
        elif Coffee.water < 350:
            print('Sorry, not enough water!')
        elif Coffee.milk < 75:
            print('Sorry, not enough milk!')
        elif Coffee.beans < 20:
            print('Sorry not enough coffee beans!')
        elif Coffee.cups < 1:
            print('Sorry, not enough cups!')

    def cappuccino(self):
        if Coffee.water >= 200 and Coffee.milk >= 100 and Coffee.beans >= 12 and Coffee.cups >= 1:
            print('I have enough resources, making you a coffee!')
            Coffee.water = Coffee.water - 200
            Coffee.milk = Coffee.milk - 100
            Coffee.beans = Coffee.beans - 12
            Coffee.cups = Coffee.cups - 1
            Coffee.money = Coffee.money + 6
        elif Coffee.water < 200:
            print('Sorry, not enough water!')
        elif Coffee.milk < 100:
            print('Sorry, not enough milk!')
        elif Coffee.beans < 12:
            print('Sorry not enough coffee beans!')
        elif Coffee.cups < 1:
            print('Sorry, not enough cups!')

    def buy(self):
        if self.user_choice == '1':
            self.espresso()
        elif self.user_choice == '2':
            self.latte()
        elif self.user_choice == '3':
            self.cappuccino()
        elif self.user_choice == 'back':
            return

    def fill(self):
        print('Write how many ml of water do you want to add:')
        Coffee.water = Coffee.water + int(input())
        print('Write how many ml of milk do you want to add:')
        Coffee.milk = Coffee.milk + int(input())
        print('Write how many grams of coffee beans do you want to add:')
        Coffee.beans = Coffee.beans + int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        Coffee.cups = Coffee.cups + int(input())

    def take(self):
        Coffee.money = str(Coffee.money)
        print('I gave you $' + Coffee.money)
        Coffee.money = int(Coffee.money)
        Coffee.money = Coffee.money - Coffee.money

Coffee()
