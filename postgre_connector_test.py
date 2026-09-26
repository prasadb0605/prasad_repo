import psycopg2

try:
    # 1. Establish the connection
    connection = psycopg2.connect(
        dbname="dvdrental",       # The database name you created earlier
        user="postgres",          # Your PostgreSQL username (default is postgres)
        password="XXXXXX",  # REPLACE WITH YOUR ACTUAL PASSWORD
        host="localhost",         # Running locally
        port="5432"               # Default PostgreSQL port
    )

    # 2. Create a cursor object to execute queries
    cursor = connection.cursor()
    print("Successfully connected to the database!")

    # 3. Execute a sample query (Top 5 rented movies)
    query = """
    SELECT f.title, COUNT(r.rental_id) AS rental_count
    FROM film f
    JOIN inventory i ON f.film_id = i.film_id
    JOIN rental r ON i.inventory_id = r.inventory_id
    GROUP BY f.title
    ORDER BY rental_count DESC
    LIMIT 5;
    """
    cursor.execute(query)

    # 4. Fetch and print the results
    records = cursor.fetchall()
    print("\n--- Top 5 Rented Movies ---")
    for row in records:
        print(f"Film: {row[0]} | Rentals: {row[1]}")


except Exception as error:
    print(f"Error connecting to database: {error}")

finally:
    # 5. Always close the cursor and connection when done
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
    print("\nDatabase connection closed.")