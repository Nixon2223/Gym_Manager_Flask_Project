DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS gym_classes;
DROP TABLE IF EXISTS coaches;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    membership VARCHAR(255)
);

CREATE TABLE coaches (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE gym_classes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    sport VARCHAR(255),
    capacity INT,
    gym_class_coach_id INT REFERENCES coaches(id),
    date DATE,
    start_time VARCHAR(255),
    end_time VARCHAR(255)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    booking_class INT REFERENCES gym_classes(id),
    booking_member INT REFERENCES members(id)
);