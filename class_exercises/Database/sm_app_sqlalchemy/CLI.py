import pyinputplus as pyip

from controller_sm import Controller


class CLI:
    def __init__(self):
        self.controller = Controller()
        self.current_menu = self.login
        self.running = True
        self.run_menus()

    @staticmethod
    def show_title(title):
        print('\n' + title)
        print('-' * len(title) + '\n')

    def run_menus(self):
        while self.running:
            self.current_menu = self.current_menu()

    def exit_menus(self):
        self.running = False
        print("Goodbye")

    def login(self):
        self.show_title('Login Screen')
        users = self.controller.get_user_names()
        menu_items = ['Login',
                      'Create a new account',
                      'Exit',
                       ]
        menu_choice = pyip.inputMenu(menu_items,
                                     prompt='Select user or create a new account\n',
                                     numbered=True,
                                     )
        if menu_choice.lower() == 'create a new account':
            next_menu = self.create_account
        elif menu_choice.lower() == 'exit':
            next_menu = self.exit_menus
        else:
            user_name = input('Enter your name: ')
            if user_name in users:
                self.controller.set_current_user_from_name(user_name)
                next_menu = self.user_home
            else:
                print(f'Name: "{user_name.title()}" not recognised')
                next_menu = self.login
        return next_menu

    def create_account(self):
        genders = {1: 'Male', 2: 'Female', 3: 'Other', 4: 'Professional'}
        self.show_title('Create Account')
        name = input('Enter your name: ')
        age = int(input('Enter your age: '))
        print("1 = Male\n2 = Female\n3 = Other\n4 = Professional")
        gender = genders[int(input('Enter your gender: '))]
        nationality = input('Enter your nationality: ')
        self.controller.add_new_user(name, age, gender, nationality)
        return self.login

    def user_home(self):
        user_name = self.controller.get_user_name()
        self.show_title(f'User Home - {user_name.title()}')
        print("1 = Posts, 2 = Profiles, 3 = Settings")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            return self.post_home()
        elif choice == 2:
            return self.profiles()
        elif choice == 3:
            return self.settings()
        else:
            return self.login

    def post_home(self):
        print("Under construction")
        next_menu = self.user_home()
        post_type = int(input('1 to view own posts, 2 to view other posts\nEnter your choice: '))
        if post_type == 1:
                next_menu = self.view_my_posts()
        elif post_type == 2:
            next_menu = self.view_other_posts()
        return next_menu

    def view_my_posts(self):
        print("Under construction")
        return self.user_home()

    def view_other_posts(self):
        print("Under construction")
        return self.user_home()


    def profiles(self):
        print("Under construction")
        return self.user_home()

    def settings(self):
        print("Under construction")
        return self.user_home()

if __name__ == '__main__':
    cli = CLI()
# controller = Controller()