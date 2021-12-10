import pdb
from models.booking import Booking
import repositories.booking_repository as booking_repository
from models.class_ import Class
import repositories.class_repository as class_repository
from models.coach import Coach
import repositories.coach_repository as coach_repository
from models.member import Member
import repositories.member_repository as member_repository

member_repository.delete_all()
coach_repository.delete_all()

member1 = Member("John", "Standard")
member_repository.save(member1)

coach1 = Coach("Jack")
coach_repository.save(coach1)


pdb.set_trace()