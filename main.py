import izly_api

credentials = izly_api.get_credentials(*izly_api.get_csrf(), "u5u5@yahoo.com", "814587")
balance = str(izly_api.get_balance(credentials))
print(balance)