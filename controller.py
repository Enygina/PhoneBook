import recording_data
import view
import extract
import logger


def button_click():
    menu = view.option()
    while menu != 5:
        match menu:
            case 1:
                data = view.get_info()
                recording_data.rec_csv(data)
                # recording_data.rec_txt(data)
                # logger.log_data(data)
                exit(button_click())
            case 2:
                lastname = recording_data.output_csv()
                res_search = extract.empty_fnd(extract.fnd_lastname(lastname))
                view.output_data(res_search)
                exit(button_click())
            case 3:
                print_all = recording_data.output_csv()
                view.output_data(print_all)
                exit(button_click())
            case 4:
                view.bye()
                break
