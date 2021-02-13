import lib

settings = lib.Settings()
chosen_number = settings.set_list_number()

frequency_list = lib.Frequency_list(chosen_number)
chosen_list = frequency_list.upload_list()

user_input = lib.User_input()
chosen_words = user_input.user_data_upload()

output = lib.Output(chosen_list, chosen_words)
output.compare_data()
output.print_output_data()
output.write_output_file()
