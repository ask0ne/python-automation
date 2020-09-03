'''
Regular Expressions for validation and matching
'''
import re


class regex:
    '''Class'''
    def __init__(self):
        self.enter_input()

    def is_phone(self, example):
        '''Check if given string contains phone number'''
        phone_regex = re.compile(r'\d{10}')
        return phone_regex.findall(example)


    def is_email(self, example):
        '''Email'''
        email_regex = re.compile(r"( [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}) )")
        return email_regex.findall(example)


    def enter_input(self):
        '''Input'''
        example = input("Enter text ::")
        phone_no = self.is_phone(example)
        email_address = self.is_email(example)
        print('Phone Number Found ::', phone_no)
        print('Email Found ::', email_address)



regex()
