# Created by tung.dao thanhtungpfiev@gmail.com at 5/11/2022
def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', 5432),
        'user': options.get('user', ''),
        'pwd': options.get('pwd', ''),
    }
    print(conn_params)


connect()
connect(host='127.0.0.42', port=4453)
connect(port=5431, user='fab', pwd='gandalf')
