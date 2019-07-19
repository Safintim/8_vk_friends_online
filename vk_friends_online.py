import os
import vk
import getpass
from dotenv import load_dotenv


def main():
    load_dotenv()

    login = input('login:')
    password = getpass.getpass()
    api = connect_to_vk(login, password)
    friends_online = api.friends.getOnline()
    print_friends_to_console(api, friends_online)


def connect_to_vk(login, password):
    session = vk.AuthSession(
        app_id=os.environ.get('API_ID'),
        user_login=login,
        user_password=password,
        scope='friends',
    )
    api = vk.API(session, v='5.95')
    return api


def print_friends_to_console(api, friends_online):
    friends = api.users.get(user_ids=friends_online)
    for friend in friends:
        print('{} {}'.format(friend['first_name'], friend['last_name']))

if __name__ == '__main__':
    main()
