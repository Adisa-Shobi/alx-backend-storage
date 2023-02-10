--  SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.


DELIMITER $$;
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT) 
