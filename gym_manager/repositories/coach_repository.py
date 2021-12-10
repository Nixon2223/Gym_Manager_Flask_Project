from db.run_sql import run_sql
from models.coach import Coach

def save(coach):
    sql = "INSERT INTO coaches (name) VALUES (%s) RETURNING id"
    values = [coach.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    coach.id = id


def select_all():
    coaches = []
    sql = "SELECT * FROM coaches"
    results = run_sql(sql)
    for result in results:
        coach = Coach(result["name"], result["id"])
        coaches.append(coach)
    return coaches


def select(id):
    sql = "SELECT * FROM coaches WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    coach = Coach(result["name"], result["id"])
    return coach


def delete_all():
    sql = "DELETE FROM coaches"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM coaches WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(coach):
    sql = "UPDATE coaches SET name = %s WHERE id = %s"
    values = [coach.name, coach.id]
    run_sql(sql, values)