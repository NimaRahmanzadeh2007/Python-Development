import sqlite3


class Songify:

    def __init__(self):

        with sqlite3.connect("music_database/songs.db") as conn:

            c = conn.cursor()

            c.execute("""CREATE TABLE IF NOT EXISTS songs (
                      name TEXT NOT NULL,
                      artist TEXT NOT NULL,
                      year INTEGER NOT NULL,
                      type TEXT NOT NULL)""")

            conn.commit()

    def show_songs(self):

        with sqlite3.connect("music_database/my_try_5/songs.db") as conn:

            c = conn.cursor()

            c.execute("SELECT * FROM songs")

            items = c.fetchall()

            print("--------------------")

            for item in items:

                print(
                    f"name: {item[0]} / artist: {item[1]} / year: {item[2]} / type: {item[3]}")

            print("--------------------")

    def search_by_name(self):

        user_input = input("enter the name of the song: ").strip()

        with sqlite3.connect("my_try_5/songs.db") as conn:

            c = conn.cursor()

            c.execute("SELECT * FROM songs WHERE name LIKE ?",
                      ('%'+user_input+'%',))

            founds = c.fetchall()

            if len(founds) > 0:

                print("--------------------")

                for item in founds:

                    print(
                        f"name: {item[0]} / artist: {item[1]} / year: {item[2]} / type: {item[3]}")

                print("--------------------")

            else:

                print("nothing found")

    def search_by_type(self):

        user_input = input("enter the type of the song: ").strip()

        with sqlite3.connect("my_try_5/songs.db") as conn:

            c = conn.cursor()

            c.execute("SELECT * FROM songs WHERE type LIKE ?",
                      ('%'+user_input+'%',))

            founds = c.fetchall()

            if len(founds) > 0:

                print("--------------------")

                for item in founds:

                    print(
                        f"name: {item[0]} / artist: {item[1]} / year: {item[2]} / type: {item[3]}")

                print("--------------------")

            else:

                print("nothing found")

    def search_by_artist(self):

        user_input = input("enter the artist of the song: ").strip()

        with sqlite3.connect("my_try_5/songs.db") as conn:

            c = conn.cursor()

            c.execute("SELECT * FROM songs WHERE artist LIKE ?",
                      ('%'+user_input+'%',))

            founds = c.fetchall()

            if len(founds) > 0:

                print("--------------------")

                for item in founds:

                    print(
                        f"name: {item[0]} / artist: {item[1]} / year: {item[2]} / type: {item[3]}")

                print("--------------------")

            else:

                print("nothing found")
