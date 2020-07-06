# MobileWallet2020

## How to run the application

```bash
docker pull shenzhongqiang/mobilewallet:1.0
docker run -p8000:8000 -d shenzhongqiang/mobilewallet:1.0
```

## See existing users
open browser, go to

http://localhost:8000/api/users/

password for admin is admin, for john and jack is 12345678

## How to login
go to http://localhost:8000/api/login/

use one of the username/password

## How to transfer money
go to http://localhost:8000/api/transfer/

input target username and amount of money


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
