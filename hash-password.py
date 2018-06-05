import bcrypt


class HashPassword:
    '''Hash password, compare hash with bcrypt, salt and pepper'''
    
    def __init__(self, pepper):
        self.pepper = pepper
    
    def create_hashed(self, plaintext):
        '''Return hashed password from plain text password'''
        return bcrypt.hashpw(plaintext + self.pepper, bcrypt.gensalt(12))

    def compare_hashed(self, plaintext, hashed):
        '''Return boolean when compare plain text password and hashed password'''
        return bcrypt.checkpw(plaintext + self.pepper, hashed)
