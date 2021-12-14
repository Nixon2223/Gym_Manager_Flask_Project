from db.run_sql import run_sql
from models.booking import Booking
from models.member import Member
import repositories.member_repository as member_repository
from models.gymclass import GymClass
import repositories.gym_class_repository as gym_class_repository

def save(booking):
    sql = "INSERT INTO bookings (gym_class_id, member_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.gym_class.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id


def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for result in results:
        member = member_repository.select(result["member_id"])
        gym_class = gym_class_repository.select(result["gym_class_id"])
        booking = Booking(gym_class, member, result["id"])
        bookings.append(booking)
    return bookings


def select(id):
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    member = member_repository.select(result["member_id"])
    gym_class = gym_class_repository.select(result["gym_class_id"])
    booking = Booking(member, gym_class, result["id"])
    return booking


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(booking):
    sql = "UPDATE bookings SET (member_id, gym_class_id) = (%s, %s) WHERE id = %s"
    values = [booking.member.id, booking.gym_class.id, booking.id]
    run_sql(sql, values)

def delete_for_member_and_class_id(member_id, class_id):
    sql = "DELETE FROM bookings WHERE member_id = %s AND gym_class_id =%s"
    values = [member_id, class_id]
    run_sql(sql, values)