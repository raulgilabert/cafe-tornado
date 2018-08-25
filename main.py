import os
import sqlite3
import pprint

import tornado.ioloop
import tornado.web

base = sqlite3.connect("datos.db")

cursor = base.cursor()


class MainWeb(tornado.web.RequestHandler):
    def redirect_to_main(self):
        txt = ""

        for character in self.request.uri:
            if character != "?":
                txt += character

            else:
                break

        self.redirect(txt)


    def get(self):
        name = self.get_argument("name", True)
        quantity = self.get_argument("quantity", True)

        if isinstance(name, str):
            quantity = int(quantity)

            cursor.execute("SELECT Cantidad FROM datos WHERE Nombre=?", (name,))

            quantity_2 = cursor.fetchall()

            quantity = quantity + int(quantity_2[0][0])

            cursor.execute("UPDATE datos SET Cantidad=? WHERE Nombre=?", (quantity, name))

            base.commit()

            self.redirect_to_main()

        else:
            cursor.execute("SELECT * FROM datos")

            data = cursor.fetchall()

            dictionary = {}

            for element in data:
                num = element[2] - element[1]

                if num < 0:
                    num = 0

                dictionary[element[0]] = {
                    "cantidad": element[1],
                    "minimo": element[2],
                    "faltante": num
                }


            self.render("main.html", dict=dictionary)

    def post(self):
        name = self.get_argument("name")
        minimum = self.get_argument("minimum")
        quantity = self.get_argument("quantity")

        print(quantity, minimum)

        try:
            cursor.execute("INSERT INTO datos(Nombre, Cantidad, Minimo) VALUES(?, ?, ?)", (name, quantity, minimum))

        except:
            cursor.execute("UPDATE datos SET Cantidad=?, Minimo=? WHERE Nombre=?", (quantity, minimum, name))

        base.commit()

        cursor.execute("SELECT * FROM datos")

        print(cursor.fetchall())

        self.redirect_to_main()


class Application(tornado.web.Application):
    def __init__(self):
        base_dir = os.path.dirname(__file__)
        settings = {
            "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
            'template_path': os.path.join(base_dir, "templates"),
            'static_path': os.path.join(base_dir, "static"),
            'debug': True,
            "xsrf_cookies": False,
        }

        tornado.web.Application.__init__(self, [
            tornado.web.url(r"/", MainWeb),
        ], **settings)


if __name__ == "__main__":
    global V
    V = 0

    Application().listen(8001)
    tornado.ioloop.IOLoop.instance().start()
