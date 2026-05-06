Database Schema

Users
Stores registered users.

Fields:
- id
- username
- email
- password_hash
- balance
- is_defaulted // if the User is bankrupt 
- registered_at

Trades
Stores buy and sell transactions.

Fields:
- id // number of a transaction
- user_id
- ticker // AAPL, TSLA, etc.
- trade_type //buy or sell
- quantity
- price
- total_value //price * quantity
- timestamp //when the transaction took place