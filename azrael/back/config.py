import keyring

########################################################################################################################
charset = 'utf8mb4'
########################################################################################################################
tracker_token = keyring.get_password('yandex_tracker', 'token')
tracker_org_id = keyring.get_password('yandex_tracker', 'org_id')
########################################################################################################################
sql_host = keyring.get_password('postgresql', 'host')
sql_user = keyring.get_password('postgresql', 'user')
sql_password = keyring.get_password('postgresql', sql_user)
sql_database = keyring.get_password('postgresql', 'db_name')
########################################################################################################################
