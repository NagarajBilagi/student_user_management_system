from app.db import SessionLocal
from app.models import InterestResource

INTEREST_RESOURCE_DATA = [
    {
        "interest_tag": "AI",
        "workshops": "AI Workshop",
        "training": "AI Training Program",
        "event": "AI Summit"
    },
    {
        "interest_tag": "Robotics",
        "workshops": "Robotics Bootcamp",
        "training": "Robotics Certification",
        "event": "Robotics Expo"
    },
    {
        "interest_tag": "Data Science",
        "workshops": "Data Science Hands-on",
        "training": "Data Analytics Course",
        "event": "Data Summit"
    },
    {
        "interest_tag": "Software Development",
        "workshops": "Full Stack Workshop",
        "training": "Web Dev Course",
        "event": "Developer Conference"
    }
]

def seed_interest_resources(db_session=None):
    """
    Seeds the InterestResource table.
    If db_session is provided (like in tests), use that.
    Otherwise, use SessionLocal() from the main app database.
    """

    db = db_session or SessionLocal()

    # Avoid duplicate seeding
    if db.query(InterestResource).first():
        return  # already seeded

    for item in INTEREST_RESOURCE_DATA:
        db.add(InterestResource(**item))

    db.commit()
    db.close()
