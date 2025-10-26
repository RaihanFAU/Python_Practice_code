import mysql.connector
from contextlib import contextmanager


@contextmanager
def database_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='expense_manager'
        )
        if connection.is_connected():
            print("Connection is successful")
            yield connection
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        yield None
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Connection closed")


def fetch_all_record():
    with database_connection() as connection:
        if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM expenses")
            expenses = cursor.fetchall()

            for expense in expenses:
                print(expense)

            cursor.close()

def fetch_expense_for_data(expense_date):
    with database_connection() as connection:
        if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
            expenses = cursor.fetchall()

            for expense in expenses:
                print(expense)

            cursor.close()

def insert_expense(expense_date, amount, category, notes):
    with database_connection() as connection:
        if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(
                "INSERT INTO expenses(expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
                (expense_date, amount, category, notes)
            )
            connection.commit()
            cursor.close()
            print("Expense inserted successfully")

def delete_expense_for_data(expense_date):
    with database_connection() as connection:
        if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute('DELETE FROM expenses WHERE expense_date = %s', (expense_date,))
            connection.commit()
            cursor.close()
# Main execution
if __name__ == "__main__":
    # fetch_all_record()
    # insert_expense('2024-08-09', 100, 'Food', 'Fuska')
    print("**** expense for 8/9 *****")
    fetch_expense_for_data('2024-08-09')
    print("*** delete for 8/9 ***")
    delete_expense_for_data('2024-08-09')
    print("**** fetch again expense for 8/9 *****")
    fetch_expense_for_data('2024-08-09')