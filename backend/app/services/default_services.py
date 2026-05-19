from sqlalchemy.orm import Session

from app.models.users import User


DEFAULT_THRESHOLD = 100.0 #100 dollars is the threshold for bankruptcy


def update_bankruptcy_status(
    user: User,
    net_worth: float,
    db: Session,
) -> User:
    """
    Marks the user as bankrupt if net worth falls below the threshold.
    """

    if net_worth < DEFAULT_THRESHOLD:
        user.is_bankrupt = True
    else:
        user.is_bankrupt = False

    db.commit()
    db.refresh(user)

    return user