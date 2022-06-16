import os

def automation():
    os.system("behave ./BDD/login.feature")
    os.system("behave ./BDD/market.feature")
    os.system("behave ./BDD/product.feature")

if __name__ == '__main__':
    automation()