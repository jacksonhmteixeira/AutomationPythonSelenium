import os

def automation():
    os.system("behave .\BDD\login.feature")

if __name__ == '__main__':
    automation()