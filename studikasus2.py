import mysql.connector as mysql
from mysql.connector import Error
import sqlalchemy
from urllib.parse import quote_plus as urlquote
import matplotlib.pyplot as plt
import pandas as pd
import os

class studikasus2:

    def __init__(self, host, port, user, password):
        """

        :param host: The host name or IP address of the MySQL server
        :param port: The TCP/IP port of the MySQL server. Must be an integer
        :param user: The user name used to authenticate with the MySQL server
        :param password: The password to authenticate the user with the MySQL server
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def create_db(self, db_name):
        """

        :param db_name:for create database name
        """
        conn = mysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password
        )
        try:
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute("CREATE DATABASE {}".format(db_name))
        except Error as e:
            print("Error while connecting to MySQL", e)
        # preparing a cursor object
        # creating database

    def create_table(self, db_name, table_name, df):
            """

            :param self:
            :param db_name: for database name
            :param table_name: for table name
            :param df: data frame For insert column and data table
            """

            conn = mysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                passwd=self.password
            )
            try:
                if conn.is_connected():
                    cursor = conn.cursor()
                    cursor.execute("USE {}".format(db_name))
                    cursor.execute("CREATE TABLE {}".format(table_name))
            except Error as e:
                print("Error while connecting to MySQL", e)

            engine_stmt = 'mysql+mysqldb://%s:%s@%s:%s/%s' % (self.user, urlquote(self.password),
                                                              self.host, self.port, db_name)
            engine = sqlalchemy.create_engine(engine_stmt)

            df.to_sql(name=table_name, con=engine,
                      if_exists='append', index=False, chunksize=1000)

    def load_data(self, db_name, table_name):
            """

            :param self:
            :param db_name:for database name
            :param table_name:for table name
            """
            conn = mysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                passwd=self.password
            )
            try:
                if conn.is_connected():
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM {}.{}".format(db_name, table_name))
                    result = cursor.fetchall()
                    return result
            except Error as e:
                print("Error while connecting to MySQL", e)

    def import_csv(self, path):
                """

                :param path: show csv in console
                :return: read csv file aka addresses.csv
                """
                return pd.read_csv(path, index_col=False, delimiter=',')

    def save_result_to_csv(self, df, csv_path):
                """

                :param self:
                :param df: our data frame
                :param csv_path: path file csv
                """
                df.to_csv(csv_path)