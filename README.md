# MobileWallet2020

## Run application


## API Doc
### Login
POST /api/login/
Params:
  username=<username>
  password=<password>

### Logout
GET /api/logout/

### List all users - login required
GET /api/users/

### Retrieve balance - login required
GET /api/balance/

### Retrieve Transactions - login required
GET /api/transactions/

### Get all transactions - login required
GET /api/all_transactions/

### Transfer money - login required
POST /api/transfer/
Params:
  to=<username of user who received the money>
  amount=<amount>
