-- CREATE DATABASE reddit_trend_analyzer;
USE reddit_trend_analyzer;

-- 1. How many Reddit posts are in our database?

-- SELECT COUNT(*) AS Total_Posts
-- FROM reddit_posts;

-- 2. What does our data look like?

-- SELECT *
-- FROM reddit_posts
-- LIMIT 10;

-- 3. Which subreddit has the highest average Reddit score?

-- SELECT
--    subreddit,
--    ROUND(AVG(score), 2) AS average_score
-- FROM reddit_posts
-- GROUP BY subreddit
-- ORDER BY average_score DESC;

-- 4. Which subreddit has the highest average number of comments?

-- SELECT
--   subreddit,
--    ROUND(AVG(num_comments),2) AS average_comments
-- FROM reddit_posts
-- GROUP BY subreddit
-- ORDER BY average_comments DESC;

-- 5. What is the best hour to post on Reddit?

-- SELECT
--    post_hour,
--    ROUND(AVG(score),2) AS average_score
-- FROM reddit_posts
-- GROUP BY post_hour
-- ORDER BY average_score DESC;

-- 6. Which day receives the highest average score?
-- SELECT
--    post_day,
--    ROUND(AVG(score),2) AS average_score
-- FROM reddit_posts
-- GROUP BY post_day
-- ORDER BY average_score DESC;

-- 7. Which are the Top 10 viral posts?

-- SELECT
--    subreddit,
--    title,
--    score,
--    num_comments
-- FROM reddit_posts
-- ORDER BY score DESC
-- LIMIT 10;

-- 8. Who are the most active Reddit authors?

-- SELECT
--    author,
--    COUNT(*) AS total_posts
-- FROM reddit_posts
-- GROUP BY author
-- ORDER BY total_posts DESC
-- LIMIT 10;

-- 9. Which subreddit has the most posts?

-- SELECT
--    subreddit,
--    COUNT(*) AS total_posts
-- FROM reddit_posts
-- GROUP BY subreddit
-- ORDER BY total_posts DESC;

-- 10. Which posts generated the most discussion?

SELECT
    subreddit,
    title,
    num_comments
FROM reddit_posts
ORDER BY num_comments DESC
LIMIT 10;

