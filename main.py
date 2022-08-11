# -- Exersise 1
# SELECT city.city, customer.customer_id
# FROM city
# JOIN customer
# ON city.city_id = customer.customer_id
# WHERE city = 'Texas';
# -- Answer 0 people live in Texas.
#
#
# --Exersise 2
# SELECT customer.first_name, customer.last_name, payment.amount
# FROM customer
# JOIN payment
# ON customer.customer_id = payment.customer_id
# WHERE amount > 6.99;
#
#
#
# --Exersise 3
# SELECT customer_id, sum(amount)
# FROM payment
# GROUP BY customer_id
# HAVING sum(amount) > 175;
#
# SELECT first_name, last_name
# FROM customer
# WHERE customer_id IN (
# 	SELECT customer_id
# 	FROM payment
# 	GROUP BY customer_id
# 	HAVING sum(amount) > 175
# );
#
# --Exersise 4
# SELECT city_id, city, customer_id
# FROM city
# JOIN customer
# ON city.city_id = customer.customer_id
# WHERE city LIKE 'Argentina';
#
# --Exersise 5
# SELECT COUNT(film.film_id), category_id, name
# FROM film
# JOIN category
# ON film.film_id = category.category_id
# GROUP BY category_id
# ORDER BY COUNT(film.film_id);
#
#
# --Exersise 6
# SELECT category_id , count(film.film_id)
# FROM film
# JOIN film_category
# ON film.film_id = film_category.film_id
# GROUP BY category_id
# ORDER BY count(film.film_id);
# --Answer sports
#
# --Exersise 7
#
# SELECT actor.first_name, actor.last_name, COUNT(film_id)
# FROM actor
# JOIN film_actor
# ON actor.actor_id = film_actor.actor_id
# GROUP BY actor.first_name, actor.last_name
# ORDER BY COUNT(film_id);
# --Answer Emily Dee
#


