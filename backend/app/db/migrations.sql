CREATE TABLE holding_history (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id),
    ticker VARCHAR NOT NULL,
    quantity INTEGER NOT NULL,
    average_buy_price FLOAT NOT NULL,
    current_price FLOAT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_holding_history_timestamp ON holding_history(timestamp);