class Settings:
    def __init__(self, *args, **kwargs):
        self.list_number = "1"

    def set_list_number(self):
        print('Frequency lists settings')
        for key in Frequency_list.list_collection:
            print("%s: %s" % (key, Frequency_list.list_collection[key]))
        self.list_number = input("Please choose a frequency list by number: ")
        if self.list_number not in Frequency_list.list_collection.keys():
            self.list_number = '1'
        print("You chose %s frequency list" % Frequency_list.list_collection[self.list_number])
        return self.list_number

class Frequency_list:
    list_collection = {"1": "frequency_lists/netflix12k.txt",
                       "2": "frequency_lists/japanese15k.txt",
                       "3": "frequency_lists/japanese20k.txt",
                       "4": "frequency_lists/japanese45k.txt",
                       }

    def __init__(self, list_number, list_title=None):
        self.list_number = list_number
        self.list_title = list_title
        self.frequency_data = []
        
    def upload_list(self):
        file_name = self.list_collection.get(self.list_number)
        with open(file_name, 'r') as collection_file:
            file_data = collection_file.read()
            self.frequency_data = file_data.split()
        return self.frequency_data

class User_input:
    def __init__(self, *args, **kwargs):
        self.user_data = []
        self.output_data = []

    def user_data_upload(self):
        self.user_data = input("Please enter a name or your file or your words divided by spaces: ")
        try:
            with open(self.user_data, 'r') as collection_file:
                file_data = collection_file.read()
                self.output_data = file_data.split()
        except FileNotFoundError:
            self.output_data = (str(self.user_data) + ' ').split()
        return self.output_data

class Output:
    def __init__(self, set_list, user_words):
        self.set_list = set_list
        self.user_words = user_words
        self.output_words = []

    def compare_data(self):
        output_words = []
        for word in self.user_words:
            if word in self.set_list:
                 word_number_pair = [word, self.set_list.index(word)]
                 output_words.append(word_number_pair)
        self.output_words = dict(output_words)
        return self.output_words

    def print_output_data(self):
        for word in self.output_words:
            print("%s %s" % (word, self.output_words[word]))

    def write_output_file(self):
        output_file_name = input("Please enter a new filename or path to a file: ")
        if output_file_name:
            with open(output_file_name, 'w') as output_file:
                for word in self.output_words:
                    print(("%s %s" % (word, self.output_words[word])), file = output_file)
        print("Thank you for using our app!")
