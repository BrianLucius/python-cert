import configparser

config = configparser.ConfigParser(inline_comment_prefixes=('#'))
print(config.read('/Users/brian/Repositories/python-cert/pcpp1_configparser/config.ini'))

print('Sections:',config.sections(), '\n')
print('mariadb section:')
print('Host:', config.get('mariadb', 'host'))
print('Host:', config['mariadb']['host'])
print('Database:', config['mariadb']['name'])
print('Username:', config['mariadb']['user'])
print('Password:', config['mariadb']['password'], '\n')

print('redis section:')
print('Host:', config['redis']['host'])
print('Port:', config['redis']['port'])
print('Database Number:', config['redis']['db'])