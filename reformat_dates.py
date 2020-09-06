'''
Changes date types from files in given folder
MM-DD-YYYY -> DD-MM-YYYY
DD-MM-YYYY -> MM-DD-YYYY
'''
import os
import re
import shutil

class DateSwap:
    '''Base Class'''
    def __init__(self):
        self.date_pattern = re.compile(r"""(.*)?(\d{2})-(\d{2})-(\d{4})(.*)?""", re.VERBOSE)
        self.input_dir()

    def find_files(self, directory):
        '''Iterate through the files in directory'''
        for files in os.listdir(directory):
            file_name = self.date_pattern.search(files)
            if file_name is None:
                continue
            else:
                print (file_name)
                prev_text = file_name.group(1)
                month = file_name.group(2)
                day = file_name.group(3)
                year = file_name.group(4)
                after_text = file_name.group(5)
                for i in range(0,4):
                    print (file_name.group(i+1))     
                new_files, absolute_dir = self.rename_file(prev_text, month, day, year, after_text)
                files = os.path.join(absolute_dir, files)
                file_new_name = os.path.join(absolute_dir, new_files)
                print("Renaming "+ files + " to " + file_new_name + "...")
                shutil.move(files, file_new_name)

    def rename_file(self, prev_text, month, day, year, after_text):
        '''Rename files & obtain absolute path'''
        new_files = prev_text + day + '-' + month + '-' + year + after_text
        absolute_dir = os.path.abspath('.')
        return (new_files, absolute_dir)

    def input_dir(self):
        directory = input("Enter Directory Absolute Path (Leave blank for current directory) ")
        if directory:
            self.find_files(directory)
        else:
            directory = "."
            self.find_files(directory)



if __name__ == "__main__":
    DateSwap()
