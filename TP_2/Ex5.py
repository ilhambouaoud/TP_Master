class Animal:
    def faire_du_bruit(self):
        print("Cet animal fait un bruit")

class Chien(Animal):
    def faire_du_bruit(self):
        print("Bruit du chien : haou haou !")

class Chat(Animal):
    def faire_du_bruit(self):
        print("Bruit du chat :Miaou Miaou !")

chien = Chien()
chien.faire_du_bruit()

chat = Chat()
chat.faire_du_bruit()

