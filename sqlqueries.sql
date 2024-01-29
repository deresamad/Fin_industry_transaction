-- How many card events was generated

SELECT COUNT(event_id)
FROM events.cards;

--How many user events was generated

SELECT COUNT(event_id)
FROM events.users;

--How many card events where created with no user id?

SELECT COUNT(event_id)
FROM events.cards
WHERE user_id IS NULL;

--How many card events where active and how many was inactive?

SELECT 
    COUNT(CASE WHEN active = true THEN 1 END) AS number_of_active_events,
    COUNT(CASE WHEN active = false THEN 1 END) AS number_of_inactive_events
FROM events.cards;

-- Which staff created the most event?

SELECT created_by_name, COUNT(event_id) AS number_of_events_created
FROM events.cards
GROUP BY created_by_name
ORDER BY number_of_events_created DESC
LIMIT 5;

-- Which users has the highest score

 SELECT name, score AS highest_score
 FROM events.users
 GROUP BY name,score
 ORDER BY highest_score DESC
 LIMIT 5;
 
-- Which users has the lowest score

 SELECT name, min(score) AS lowest_score
 FROM events.users
 GROUP BY name
 ORDER BY lowest_score
 LIMIT 5;

-- What is the average score of users?

SELECT AVG(score) AS average_user_score
FROM events.users;

-- What is the number of card events per user

SELECT
    u.id AS user_id,
    u.name AS user_name,
    COUNT(c.id) AS total_card_events
FROM events.users u
LEFT JOIN events.cards c ON u.id = c.user_id
GROUP BY u.id, u.name
ORDER BY total_card_events DESC;


-- How many staff created card events?

SELECT COUNT(DISTINCT created_by_name)
FROM events.cards

-- What is the maximum and minimum card events created and at what time?

SELECT created_at,COUNT(event_id) AS count_of_events
FROM events.cards
GROUP BY created_at
ORDER BY count_of_events ASC

