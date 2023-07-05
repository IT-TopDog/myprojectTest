import sqlite3 

class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None


    def connect(self):
        self.conn = sqlite3.connect('mydd.db')
        self.cursor = self.conn.cursor()


    def create_user_table(self):
        self.cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS telegramusers(
                id INTEGER PRIMARY KEY,
                first_name VARCHAR (30),
                user_id INTEGER UNIQUE,
                phone_numer VARCHAR(50)
                )
        
        ''') 

        self.conn.commit()


    def create_categories_table(self):
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS categories(
                id INTEGER PRIMARY KEY,
                name VARCHAR (50) UNIQUE
                )
        ''')

        self.conn.commit()



    def create_products_table(self):
        self.cursor.execute ('''
                CREATE TABLE IF NOT EXISTS pruducts(
                id INTEGER PRIMARY KEY,
                name VARCHAR(100),
                description TEXT,
                price INTEGER,
                photo TEXT,
                category_name VARCHAR(50),
                FOREIGN KEY(category_name) REFERENCES categories(name)
                )
        
        ''')    

        self.conn.commit()


    def create_cart_table(self):
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS cart(
                id INTEGER PRIMARY KEY,
                user INTEGER UNIQUE,
                product INTEGER,
                FOREIGN KEY (user) REFERENCES user_id),
                FOREIGN KEY (product) REFERENCES products(id)
                )
        ''')
        self.conn.commit()

    def add_user(self,first_name,user_id,phone_number):
        self.cursor.execute('''
                INSERT INTO telegramusers(first_name,user_id,phone_numer)
                VALUES (?,?,?)
        ''',(first_name,user_id,phone_number))

        self.conn.commit()


    def check_user(self,user_id):
        self.cursor.execute("SELECT user_id FROM telegramusers WHERE user_id = ?",(user_id,))
        result = self.cursor.fetchone()
        if result is not None:
            return True
        else:
            return False 

        



    def close (self):
        self.conn.close()




