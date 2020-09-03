'''
Regular Expressions for validation and matching
'''
import re

class RegexClass:
    '''Main class'''
    def __init__(self):
        input_text = self.enter_input()
        self.find_patterns(input_text)

    def is_phone(self, example):
        '''Contains phone number'''
        phone_regex = re.compile(r'\d{10}')
        return phone_regex.findall(example)

    def is_email(self, example):
        '''Contains Email'''
        email_regex = re.compile(r''' [a-zA-Z0-9.+]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+ ''', re.VERBOSE)
        return email_regex.findall(example)

    def enter_input(self):
        '''Input'''
        example = input("Enter text ::")
        return example

    def find_patterns(self, example):
        '''Find patterns in string'''
        phone_no = self.is_phone(example)
        email_address = self.is_email(example)
        print('Phone Number Found ::', phone_no)
        print('Email Found ::', email_address)

if __name__ == "__main__":
    RegexClass()
