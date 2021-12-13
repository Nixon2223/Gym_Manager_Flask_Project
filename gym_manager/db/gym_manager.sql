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
    gym_class_coach_id INT REFERENCES coaches(id) ON DELETE CASCADE,
    date DATE,
    start_time VARCHAR(255),
    end_time VARCHAR(255)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    gym_class_id INT REFERENCES gym_classes(id) ON DELETE CASCADE,
    member_id INT REFERENCES members(id) ON DELETE CASCADE
);