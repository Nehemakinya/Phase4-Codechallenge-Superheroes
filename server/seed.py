from app import app, db, Hero, Power, HeroPower

def seed_data():
    # Create Hero and Power records
    hero1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    hero2 = Hero(name="Doreen Green", super_name="Squirrel Girl")
    hero3 = Hero(name="Gwen Stacy", super_name="Spider-Gwen")
    power1 = Power(description="Super Strength")
    power2 = Power(description="Flight and more")
    power3 = Power(description="Telekinesis")

    # Add records to the session
    db.session.add(hero1)
    db.session.add(hero2)
    db.session.add(hero3)
    db.session.add(power1)
    db.session.add(power2)
    db.session.add(power3)

    # Commit the changes to the database
    db.session.commit()

    # Create associations between heroes and powers using HeroPower
    hero_power1 = HeroPower(hero_id=hero1.id, power_id=power1.id)
    hero_power2 = HeroPower(hero_id=hero1.id, power_id=power2.id)
    hero_power3 = HeroPower(hero_id=hero2.id, power_id=power3.id)

    # Add associations to the session and commit
    db.session.add(hero_power1)
    db.session.add(hero_power2)
    db.session.add(hero_power3)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_data()
