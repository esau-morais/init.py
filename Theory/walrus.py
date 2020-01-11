# The account info request
request = {'form': {'usename': 'Esaú', 'password': 'password'}}
# The database
db = []

def new_acc(request):
  """ New Account Help
    ':=' is the walrus operator (to define a variable in one line (on conditions, loops, etc...) and to simplify code)
    'password' is the value that will be entred by user
  """
  if len(password := request['form'].get('password')) > 5:
    db.append(password)
    # If password length is > 5
    return 'Account successfully created!'
  else:
    # If password length is < 5
    return 'Password is so short... Try other password'

print(new_acc(request))
print(db)