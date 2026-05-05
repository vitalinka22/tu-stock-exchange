## Database Schema

## Users
Stores registered users.

Fields:
- id
- username
- email
- password_hash
- balance
- is_bankrupt // if the User is bankrupt 
- registered_at

## Trades
Stores buy and sell transactions.

Fields:
- id // number of a transaction
- user_id
- ticker //  stock symbol, AAPL, TSLA, etc.
- trade_type //buy or sell
- quantity
- price
- total_value //price * quantity
- timestamp //when the transaction took place

## holdings

Stores the current portfolio of each user.

Fields:
- id // unique holding ID
- user_id // reference to users.id
- ticker // stock symbol, e.g. AAPL, TSLA
- quantity // number of shares currently owned
- average_buy_price // average purchase price for this ticker
- updated_at // when this holding was last updated

## stock_price_history

Stores historical stock prices.

Fields:
- id // unique price history ID
- ticker // stock symbol, e.g. AAPL, TSLA
- price // stock price at the recorded time
- timestamp // when the price was recorded

## net_worth_history

Stores the user's net worth over time.

Fields:
- id // unique net worth history ID
- user_id // reference to users.id
- net_worth // total user value: cash balance + current value of holdings
- timestamp // when the net worth was recorded


## auto_trades

Stores automatic buy/sell trading rules.

Fields:
- id // unique auto-trade ID
- user_id // reference to users.id
- ticker // stock symbol, e.g. AAPL, TSLA
- trade_type // buy or sell
- target_price // price condition for executing the trade
- quantity // number of shares to buy or sell
- is_active // true if the auto-trade rule is still active
- created_at // when the auto-trade rule was created