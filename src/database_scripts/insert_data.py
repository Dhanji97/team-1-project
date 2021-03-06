from psycopg2.extras import execute_values
from database_scripts.create_connection import create_db_connection

connection = create_db_connection()

def insert_customers(connection, data): 
    try:
        with connection.cursor() as cursor:
            for d in data:
                cursor.execute("""INSERT INTO customers (customer_hash) VALUES (%s)""", [d]) #We won't return any Pks
    except Exception as e:
        print(e)
        pass
    else:
        connection.commit()
        cursor.close()

def insert_payments(connection, data): 
    try:
        with connection.cursor() as cursor:
            for d in data:
                cursor.execute("""INSERT INTO payments (payment_type) VALUES (%s)""", [d])
    except Exception as e:
        print(e)
        pass
    else:
        connection.commit()
        cursor.close()
    
        
def insert_locations(connection, data): 
    try:
        with connection.cursor() as cursor:
            for d in data:
                cursor.execute("""INSERT INTO locations (location) VALUES (%s)""", [d])
    except Exception as e:
        print(e)
        pass
    else:
        connection.commit()
        cursor.close()

def insert_products(connection, data): 
    try:
        with connection.cursor() as cursor:
            execute_values(cursor, """INSERT INTO products (product_name, product_price) VALUES %s""", data)
    except Exception as e:
        print(e)
        pass
    else:
        connection.commit()
        cursor.close()

def insert_orders(connection, data): 
    try:
        with connection.cursor() as cursor:
            execute_values(cursor, """INSERT INTO orders (customer_id, date, payment_id, location_id, amount_paid)
            VALUES %s""", data)
    except Exception as e:
        print(e)
        pass
    else:
        connection.commit()
        cursor.close()   
        
def insert_order_product(connection, data): 
    try:
        with connection.cursor() as cursor:
            execute_values(cursor, """INSERT INTO order_products (order_id, product_id, quantity) VALUES %s""", data)
    except Exception as e:
        print(e)
        pass
    else:
        connection.commit()
        cursor.close()