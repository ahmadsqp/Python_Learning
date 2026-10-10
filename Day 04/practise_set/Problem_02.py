Name = input("Enter your Name: ")
Date = input("Enter Date: ")

letter = f'''
        Dear <|{Name}|>,
        You are selected!
        <|{Date}|>
        '''

print(letter)

letter = '''
        Dear <|Name|>,
        You are selected!
        <|Date|>
        '''

print(letter.replace("<|Name|>", Name).replace("<|Date|>", Date))