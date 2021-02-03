def user_upload():
    user_file = input(str("Please enter path to your file: "))
    user_data = []
    with open(user_file, 'r') as data_file:
        user_data = data_file.readlines()
    return user_data

def frequency_file_upload():
    frequency_data = []
    with open('frequency_lists/netflix12k.txt', 'r') as freq_data_file:
        frequency_data = freq_data_file.readlines()
    return frequency_data

def compare_data():
    user_words = list(user_upload())
    frequency_words = list(frequency_file_upload())
    output_data = []
    for word in user_words:
        if word in frequency_words:
            output_data.append('%s,%s' % (frequency_words.index(word), word))
    return output_data

def writing_output_file():
    output_data = list(compare_data())
    print(output_data)
    output_file_name = input("Please enter a new filename: ")
    with open(output_file_name, 'w') as output_file:
        for word in output_data:
            output_file.write(word)

writing_output_file()
