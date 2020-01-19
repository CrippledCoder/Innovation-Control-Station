import hashlib, binascii, os


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

print(hash_password("Inn0v@te!"))

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

print(verify_password("15ee291d3cb10199c15cda3c22daa06ffce02e670cdef0ffbdab2c27f8bd6ced717bdc27084c153c5e7cc66f93d2c6f43bdbe684cf32784a7378c7c3c7df343d0631b712d1471d26aeae7c1389a7510c90d937920643717673ebdd0566d0a07c","Inn0v@te!"))
with open("login.txt", "r") as file:
    print(file.read().split("\n"))