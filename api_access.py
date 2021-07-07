import xmlrpc.client

info = xmlrpc.client.ServerProxy('https://demo.odoo.com/start').start()
url, db, username, password = \
    info['host'], info['database'], info['user'], info['password']

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())
print()

uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

print(models.execute_kw(db, uid, password,
    'res.partner', 'search',
    [[['is_company', '=', True]]]))
