import os

filename = os.path.basename(__file__)

if __name__ == '__main__':
    print('module', filename, 'run as main')
else:
    print('module', filename, 'imported')


def hello_from_module():
    print('hello from module')
