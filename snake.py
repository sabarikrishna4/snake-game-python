from typing import Tuple
import customtkinter
import time
from threading import Thread
import keyboard
import random
from PIL import Image, ImageTk
import math


# print(keyboard.is_pressed("down arrow"))

customtkinter.set_appearance_mode("dark")


class SNAKE_GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x480")
        self.size = 25
        self.move_x = 35
        self.move_y = 0
        self.up_key = False
        self.down_key = False
        self.right_key = False
        self.left_key = False
        self.apple_x = random.randint(0,800)
        self.apple_y = random.randint(0,480)
        print(self.apple_x, self.apple_y)
        self.score = 0

        #apple
        self.apple_image = customtkinter.CTkImage(Image.open("apple.png"), size=(50,50))
        self.green_apple_image = customtkinter.CTkImage(Image.open("green_apple.png"), size=(60,60))
        self.apple_pts = customtkinter.CTkButton(self, text="",image=self.green_apple_image,width=0,height=0, fg_color="#242424",
                                                  hover_color="#242424")
        self.apple_pts.place(x=self.apple_x, y=self.apple_y)

        #snake
        self.snake = customtkinter.CTkButton(self, text=":",corner_radius=25, width=self.size, font=("bold",20))
        self.snake.place(x=self.move_x,y=self.move_y)
        





        self.t1 = Thread(target=self.loop)
        self.t1.start()
        self.t2 = Thread(target=self.press_key)
        self.t2.start()
        self.t3 = Thread(target=self.apple_postion)
        self.t3.start()

    def apple_postion(self):
        while True:
            # print(self.move_x, self.move_y)
            if math.isclose(self.move_x,self.apple_x,abs_tol=20) and math.isclose(self.move_y,self.apple_y,abs_tol=20):
                print("scored")
                self.size +=20
                self.score += 1
                self.snake.configure(width=self.size)
                
                self.apple_x = random.randint(0,800)
                self.apple_y = random.randint(0,480)
                self.apple_pts.destroy()
                time.sleep(1)
                if self.score>=5:
                    apple_img = self.green_apple_image
                else:
                    apple_img = self.apple_image
                self.apple_pts = customtkinter.CTkButton(self, text="",image=apple_img,width=0,height=0, fg_color="#242424",
                                                  hover_color="#242424")
                self.apple_pts.place(x=self.apple_x, y=self.apple_y)

            else:
                time.sleep(0.1)
            
    def press_key(self):
        while True:
            if self.down_key is True:
                if self.move_y >= 490:
                    self.move_y = 0
                time.sleep(0.01)
                self.move_y +=1
                self.snake.place(x=self.move_x,y=self.move_y)

            elif self.up_key is True:
                if self.move_y <= 0:
                    self.move_y = 490
                time.sleep(0.01)
                self.move_y -=1
                self.snake.place(x=self.move_x,y=self.move_y)
                
            elif self.right_key is True:
                if self.move_x >= 800:
                    self.move_x = 0
                time.sleep(0.01)
                self.move_x +=1
                self.snake.place(x=self.move_x,y=self.move_y)
            
            elif self.left_key is True:
                if self.move_x <= 0:
                    self.move_x = 800
                time.sleep(0.01)
                self.move_x -=1
                self.snake.place(x=self.move_x,y=self.move_y)

            else:
                time.sleep(0.1)

    def loop(self):
        while True:
            if keyboard.is_pressed("down arrow") and not self.down_key:
                # print("pressed down arrow")
                self.down_key =True
                self.up_key = False
                self.left_key = False
                self.right_key = False
            elif keyboard.is_pressed("up arrow") and not self.up_key:
                # print("pressed up arrow")
                self.up_key = True
                self.down_key = False
                self.right_key = False
                self.left_key = False
            elif keyboard.is_pressed("right arrow") and not self.right_key:
                # print("pressed right arrow")
                self.right_key = True
                self.down_key = False
                self.up_key = False
                self.left_key = False
            elif keyboard.is_pressed("left arrow") and not self.left_key:
                # print("pressed left arrow")
                self.left_key = True
                self.right_key = False
                self.down_key = False
                self.up_key = False

            else:
                time.sleep(0.1)

if __name__ == "__main__":
    OBJ = SNAKE_GUI()
    OBJ.mainloop()
