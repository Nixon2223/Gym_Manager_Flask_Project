import pdb
from db.run_sql import run_sql
from models.booking import Booking
import repositories.booking_repository as booking_repository
from models.gymclass import GymClass
import repositories.gym_class_repository as gym_class_repository
from models.coach import Coach
import repositories.coach_repository as coach_repository
from models.member import Member
import repositories.member_repository as member_repository

# gym_class_repository.delete_all()
# member_repository.delete_all()
# coach_repository.delete_all()


# member1 = Member("John", "Standard")
# member_repository.save(member1)

# coach1 = Coach("Jack")
# coach_repository.save(coach1)

# class1= GymClass("Yoga", "yoga", 20, coach1)
# gym_class_repository.save(class1)

# booking1 = Booking(class1, member1)
# booking_repository.save(booking1)

# for member in member_repository.select_all():
#     print(member.__dict__)
# for coach in coach_repository.select_all():
#     print(coach.__dict__)
# for gym_class in gym_class_repository.select_all():
#     print(gym_class.__dict__)

# print(gym_class_repository.select(class1.id).__dict__)
# print(booking_repository.select(booking1.id).__dict__)

# print(gym_class_repository.select_members_of_gym_class(3))
# print(member_repository.select_all())

# booked_in = []
# for member in gym_class_repository.select_members_of_gym_class(3):
#     booked_in.append(member.id)
# print(booked_in)
# members = member_repository.select_all()

# not_booked_in = []
# for member in members:
#     if member.id not in booked_in:
#         not_booked_in.append(member.id)

# print(not_booked_in)

# members = []
# sql = "SELECT * FROM members WHERE membership = %s"
# values = ["standard"]
# results = run_sql(sql, values)
# for result in results:
#     member = Member(result["name"], result["membership"], result["id"])
#     members.append(member)
# print(len(members)) 

# members = []
# sql = "SELECT * FROM members WHERE membership = %s"
# values = ["deactivated"]
# results = run_sql(sql, values)
# for result in results:
#     member = Member(result["name"], result["membership"], result["id"])
#     members.append(member)

# print(len(members)) 


# sql = "SELECT * FROM bookings WHERE id = %s"
# values = [65]
# result = run_sql(sql, values)[0]

# print(result)


pdb.set_trace()