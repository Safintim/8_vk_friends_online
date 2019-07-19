import vk
import getpass


def main():
    login = input('login:')
    password = getpass.getpass()
    api = connect_to_vk(login, password)
    friends_online = api.friends.getOnline()
    print_friends_to_console(api, friends_online)


def connect_to_vk(login, password):
    APP_ID = 7063582
    session = vk.AuthSession(
        app_id=APP_ID,
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
