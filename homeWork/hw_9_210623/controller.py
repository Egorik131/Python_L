import view
import model
import text


def start():
    while True:
        select = view.menu()
        match select:
            case 1:
                if model.open_file():
                    view.print_message(text.load_successful)
                else:
                    view.print_message(text.error_load)
            case 2:
                if model.save_file():
                    view.print_message(text.save_successful)
                else:
                    view.print_message(text.error_save)
            case 3:
                view.show_contacts(model.phone_book, text.empty_book)
            case 4:
                new = view.add_contact()
                model.add_contact(new)
                view.print_message(text.add_successful(new.get('name')))
            case 5:
                word = view.search_word()
                result = model.search(word)
                view.show_contacts(result, text.empty_search(word))
            case 6:
                word = view.search_word()
                search_word = model.search(word)
                view.show_contacts(search_word, text.empty_search(word))
                index = view.input_change_id()
                new = view.change_contact()
                result = model.change_contact(index, new)
                if result:
                    view.print_message(text.change_successful(result))
                else:
                    view.print_message(text.error_changed)
            case 7:
                word = view.search_word()
                search_word = model.search(word)
                view.show_contacts(search_word, text.empty_search(word))
                index = view.input_del_id()
                result = model.remove_contact(index)
                if result:
                    view.print_message(text.del_successful(result))
                else:
                    view.print_message(text.error_deleted)
            case 8:
                view.print_message(text.exit_message)
                break
