import random



def get_command(commands):
    return random.choice(commands)


def is_reload(command):
    return command == 'reload'


def is_shoot(command):
    return command == 'shoot'


def check_shoot(bullets):
    if bullets > 1:
        return True
    else:
        return False


def check_reload(bullets):
    if bullets < 6:
        return True
    else:
        return False


def update_bullets(command, bullets):
    if is_shoot(command):
        return bullets - 1
    elif is_reload(command):
        return bullets + 1
    else:
        return bullets


def check_command(command, bullets):
    if is_shoot(command):
        return check_shoot(bullets)
    if is_reload(command):
        return check_reload(bullets)
    return True


def send_command(command):
    print(command)


print("Anthony")

count_bullets = 1
commands = ['dodge', 'dodge', 'dodge', 'reload', 'shoot', 'shoot']

while True:
    command = get_command(commands)
    if check_command(command, count_bullets):
        count_bullets = update_bullets(command, count_bullets)
        send_command(command)
        #print("Bullets = {0}".format(count_bullets))
        other_action = input()
