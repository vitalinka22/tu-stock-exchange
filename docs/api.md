Base URL:
http://localhost:8000

Auth endpoints:
## POST /auth/register

## POST /auth/login

## GET /users/me 
We use it when the frontend needs information about the currently logged-in user.

Response Example: 
{
  "id": 1,
  "email": "user@example.com",
  "balance": 10000,
  "is_bankrupt": false,
  "registered_at": "2026-05-05T12:30:00"
} or 
ERROR RESPONSE: 401 Unauthorized  "detail": "Invalid or expired token"


## GET /users/{user_id}
We use GET /users/{user_id} when displaying another user, for example from the leaderboard.

Response Example: {
  "id": 1,
  "email": "user@example.com",
  "balance": 10000,
  "is_bankrupt": false,
  "registered_at": "2026-05-05T12:30:00"
} or 
ERROR RESPONSE: 401 Unauthorized  "detail": "User not found"