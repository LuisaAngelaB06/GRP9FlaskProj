from app import app
from models.db import db
from models.user_model import User
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from datetime import date

def seed_date():
    with app.app_context():
        try:
            print("Starting database seeding")

            seed_users = [
                User(
                    fname="Admin",
                    mname="Us",
                    lname="User",
                    uname="admin",
                    email="admin@example.com",
                    pass_word=generate_password_hash("adminpass"),
                    birthday=date(1990, 1, 1),
                    gender="Male",
                    phone_num="09123456789",
                    address="PUP Manila",
                    stud_num="00000001"
                ),
                User(
                    fname="Juan",
                    mname="D",
                    lname="Dela Cruz",
                    uname="JuanDC",
                    email="juan@example.com",
                    pass_word=generate_password_hash("juanpass"),
                    birthday=date(2000, 5, 20),
                    gender="Male",
                    phone_num="09987654321",
                    address="Quezon City",
                    stud_num="00000002"
                )
            ]

            # Insert only if email not already existing
            for user in seed_users:
                existing_user = User.query.filter_by(email=user.email).first()
                if existing_user:
                    print(f"Skipping existing user: {user.email}")
                    continue
                db.session.add(user)

            db.session.commit()
            print("Database seeded successfully.")

        except IntegrityError as e:
            db.session.rollback()
            print(f"Integrity error: {e}")

        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"SQLALCHEMY error: {e}")

        except Exception as e:
            db.session.rollback()
            print(f"Unexpected error during seeding: {e}")

        finally:
            db.session.close()

if __name__ == "__main__":
    seed_date()
