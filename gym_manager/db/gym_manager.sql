DROP TABLE IF EXISTS booking;
DROP TABLE IF EXISTS class;
DROP TABLE IF EXISTS coach;
DROP TABLE IF EXISTS member;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    membership VARCHAR(255)
);

CREATE TABLE coaches (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    sport VARCHAR(255),
    capacity INT,
    date DATE,
    start_time VARCHAR(255),
    end_time VARCHAR(255)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    booking_class INT REFERENCES class_(id),
    booking_member INT REFERENCES member_(id)
);