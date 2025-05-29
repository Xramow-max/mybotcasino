import sqlite3
from datetime import datetime, timedelta

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()  # Добавьте скобки здесь

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    def add_user(self, first_name, username, user_id):
        with self.connection:
            return self.cursor.execute("""
            INSERT INTO users (first_name, username, user_id) 
            VALUES (?, ?, ?)""", 
            (first_name, username, user_id,))
        
    def get_games(self, user_id):
        with self.connection:
            self.cursor.execute("SELECT `bet` FROM `users` WHERE `user_id` = ?", (user_id,))
            user_nickname = self.cursor.fetchone()[0]
            return user_nickname
        
    def get_turnover(self, user_id):
        with self.connection:
            self.cursor.execute("SELECT `turnover` FROM `users` WHERE `user_id` = ?", (user_id,))
            balance = self.cursor.fetchone()[0]
            balance = round(balance, 2)

            # Если результат -0.0, привести его к обычному 0.0
            if balance == 0:
                balance = 0.0

            return balance
        
    def get_balance(self, user_id):
        with self.connection:
            self.cursor.execute("SELECT `balance` FROM `users` WHERE `user_id` = ?", (user_id,))
            balance = self.cursor.fetchone()[0]
            balance = round(balance, 2)

            # Если результат -0.0, привести его к обычному 0.0
            if balance == 0:
                balance = 0.0

            return balance
        
    def plus_balance(self, amount, user_id):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `balance` = `balance` + ? WHERE `user_id` = ?", (amount, user_id,))
        
    def minus_balance(self, amount, user_id):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `balance` = `balance` - ? WHERE `user_id` = ?", (amount, user_id,))
        
    def plus_turnover(self, amount, user_id):
        with self.connection:
            return self.cursor.execute("UPDATE users SET turnover = turnover + ? WHERE user_id = ?", (amount, user_id,))
        
    def plus_games(self, user_id):
        with self.connection:
            return self.cursor.execute("UPDATE users SET bet = bet + 1 WHERE user_id = ?", (user_id,))
        
    
        
    # STATISTIK

    def count_user(self):
        with self.connection:
            return self.cursor.execute("SELECT COUNT('id') as count FROM users").fetchone()[0]
        
    def count_turnover(self):
        with self.connection:
            return self.cursor.execute("SELECT SUM(turnover) as count FROM users").fetchone()[0]

    def count_games(self):
        with self.connection:
            return self.cursor.execute("SELECT SUM(bet) as count FROM users").fetchone()[0]
        

    # REFERAL PROGRAM

    def add_user_ref(self, user_id, ref_id=None):
        with self.connection:
            if ref_id != None:
                return self.cursor.execute("INSERT INTO users_referal ('user_id', 'referal_id') VALUES(?,?)", (user_id, ref_id,))
            else:
                return self.cursor.execute("INSERT INTO users_referal (user_id) VALUES (?)", (user_id,))
            
    def count_referals(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT COUNT('id') as count FROM users_referal WHERE referal_id = ?", (user_id,)).fetchone()[0]
        
    def get_ref_balance(self, user_id):
        with self.connection:
            self.cursor.execute("SELECT ref_balance FROM users_referal WHERE user_id = ? ", (user_id,))
            user_nickname = self.cursor.fetchone()[0]
            return user_nickname
        
    def get_ref_id(self, user_id):
        with self.connection:
            self.cursor.execute("SELECT referal_id FROM users_referal WHERE user_id = ? ", (user_id,))
            user_nickname = self.cursor.fetchone()[0]
            return user_nickname
        
    def plus_ref_balance(self, amount, user_id):
        with self.connection:
            return self.cursor.execute("UPDATE `users_referal` SET `ref_balance` = `ref_balance` + ? WHERE `user_id` = ?", (amount, user_id,))
        
    def minus_ref_balance(self, amount, user_id):
        with self.connection:
            return self.cursor.execute("UPDATE `users_referal` SET `ref_balance` = `ref_balance` - ? WHERE `user_id` = ?", (amount, user_id,))