request = {'form': {'usename': 'Esaú', 'password': 'pass'}}
db = []

def new_acc(request):
  if len(password := request['form'].get('password')) > 5:
    db.append(password)

    return 'Account successfully created!'
  else:
    return 'Password is so short... Try other password'

