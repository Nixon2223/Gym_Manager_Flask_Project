from db.run_sql import run_sql
from models.coach import Coach
from models.gymclass import GymClass
from models.member import Member
import repositories.coach_repository as coach_repository


def save(gym_class):
    sql = "INSERT INTO gym_classes (title, sport, capacity, coach, date, start_time, end_time) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [gym_class.title, gym_class.sport, gym_class.capacity, gym_class.coach.id, gym_class.date, gym_class.start_time, gym_class.end_time]
    results = run_sql(sql, values)
    id = results[0]['id']
    gym_class.id = id


def select_all():
    classes = []
    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)
    for result in results:
        coach = coach_repository.select(result["gym_class_coach_id"])
        gym_class = GymClass(result["title"], result['sport'], result['capacity'], coach, result['date'], result['start_time'], result['end_time'], result["id"])
        classes.append(gym_class)
    return classes


def select(id):
    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    coach = coach_repository.select(result["gym_class_coach_id"])
    gym_class = GymClass(result["title"], result['sport'], result['capacity'], coach, result['date'], result['start_time'], result['end_time'], result["id"])
    return gym_class


def delete_all():
    sql = "DELETE FROM gym_classes"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM gym_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(gym_class):
    sql = "UPDATE classes SET (title, sport, capacity, coach, date, start_time, end_time) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [gym_class.title, gym_class.sport, gym_class.capacity, gym_class.coach.id, gym_class.date, gym_class.start_time, gym_class.end_time]
    run_sql(sql, values)


def select_member_of_gym_class(id):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = member.id WHERE booking.gym_class_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        member = Member(result["name"], result["membership"])
        members.append(member)
    return members