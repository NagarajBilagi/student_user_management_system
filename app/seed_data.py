# app/seed_data.py

from .db import SessionLocal
from .models import InterestResource


def seed_interest_resources():
    """
    Seed the interest_resources table with initial data if it's empty.
    This function is safe to call multiple times: it won't duplicate data.
    """
    db = SessionLocal()
    try:
        # Check if there is already data
        existing_count = db.query(InterestResource).count()
        if existing_count > 0:
            print(f"[seed] interest_resources already has {existing_count} rows. Skipping seeding.")
            return

        print("[seed] Seeding interest_resources table...")

        rows = [
            InterestResource(
                interest_tag="AI",
                workshops="Intro to AI Workshop; Hands-on with Neural Networks",
                training="AI Fundamentals Online Training",
                event="AI Conference 2025",
            ),
            InterestResource(
                interest_tag="Robotics",
                workshops="Robotics Bootcamp; Robot Arm Programming",
                training="ROS (Robot Operating System) Training",
                event="Robotics Hackathon",
            ),
            InterestResource(
                interest_tag="Data Science",
                workshops="Data Visualization Workshop; SQL for Analysts",
                training="Python for Data Science Training",
                event="Data Summit 2025",
            ),
            InterestResource(
                interest_tag="Software Development",
                workshops="Clean Code Workshop; Git & GitHub Basics",
                training="Full-Stack Web Development Training",
                event="Developer Meetup: Modern Backend APIs",
            ),
        ]

        db.add_all(rows)
        db.commit()
        print("[seed] Seeding completed.")
    finally:
        db.close()


if __name__ == "__main__":
    # Allows you to run:  python -m app.seed_data
    seed_interest_resources()
