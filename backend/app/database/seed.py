from app.database.connection import SessionLocal
from app.database.seeders.painting_types import seed_painting_types


def main():
    db = SessionLocal()

    try:
        seed_painting_types(db)
        print("Painting types seeded successfully.")
    finally:
        db.close()


if __name__ == "__main__":
    main()