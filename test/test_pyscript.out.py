import time


box_a = document.querySelector("#box_a")
btn_b = document.querySelector("#btn_b")
btn_c = document.querySelector("#btn_c")

btn_b.onclick = lambda e: print('B is clicked!')
def click_c(e):
    print('C is clicked!')
btn_c.onclick = click_c
