import text


def menu() -> int:
    print(text.main_menu[0])
    for i in range(1, len(text.main_menu)):
        print(f'\t{i}. {text.main_menu[i]}')
    while True:
        select = input(text.select_menu)
        if select.isdigit() and 0 < int(select) < int(len(text.main_menu)):
            return int(select)
        print(text.input_error)


def show_contacts(book: dict[int:dict[str, str]], message):
    if book:
        max_name = []
        max_phone = []
        max_comment = []
        for contact in book.values():
            max_name.append(len(contact.get('name')))
            max_phone.append(len(contact.get('phone')))
            max_comment.append(len(contact.get('comment')))
        size_name = max(max_name)
        size_phone = max(max_name)
        size_comment = max(max_name)
        print('\n' + '=' * (size_name + size_phone + size_comment + 7))
        for index, contact in book.items():
            print(f'{index:>3}.'
                  f'{contact.get("name"):<{size_name + 1}}'
                  f'{contact.get("phone"):<{size_phone + 1}}'
                  f'{contact.get("comment"):<{size_comment + 1}}')
        print('=' * (size_name + size_phone + size_comment + 7) + '\n')

    else:
        print_message(message)


def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def add_contact():
    new = {}
    for key, value in text.new_contact.items():
        new[key] = input(value)
    return new


def search_word() -> str:
    return input(text.search_word)


def change_contact():
    new = {}
    for key, value in text.new_contact.items():
        new[key] = input(value)
    return new


def input_change_id():
    return str(input(text.input_chgindex))


def input_del_id():
    return int(input(text.input_delindex))
