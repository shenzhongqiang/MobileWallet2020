# MobileWallet2020

## How to run the application

```bash
docker run -p8000:8000 -d mobile/wallet:1.0
```


## API Doc
#### Login
POST /api/login/

Params:

  username=&lt;username&gt;

  password=&lt;password&gt;

#### Logout
GET /api/logout/

#### List all users
GET /api/users/

#### Retrieve balance - login required
GET /api/balance/

#### Retrieve Transactions - login required
GET /api/transactions/

#### Get all transactions - login required
GET /api/all_transactions/

#### Transfer money - login required
POST /api/transfer/

Params:

  to=&lt;username of user who received the money&gt;

  amount=&lt;amount&gt;
