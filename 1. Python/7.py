class Figure:
    def __init__(self, x = 0, y = 0, x_scale = 0, y_scale = 0):
        self.x = x
        self.y = y
        self.x_scale = x_scale
        self.y_scale = y_scale
    def fransfer(self, x = 0, y = 0):  
        self.x += x
        self.y += y

    def rescale(self,x_scale = 0, y_scale = 0):
        self.x_scale += x_scale
        self.y_scale += y_scale


def merge(f1: Figure, f2:Figure):
    f3 = Figure()
    f3.x = min(f1.x,f2.x,f1.x+f1.x_scale,f2.x+f2.x_scale)
    f3.x_scale = max(f1.x, f2.x, f1.x + f1.x_scale, f2.x + f2.x_scale)-f3.x
    f3.y = min(f1.y,f2.y,f1.y+f1.y_scale,f2.y+f2.y_scale)
    f3.y_scale = max(f1.y, f2.y, f1.y + f1.y_scale, f2.y + f2.y_scale)-f3.y
    return f3


def inter(f1: Figure, f2:Figure):
    left = max(f1.x, f2.x)
    top = min(f1.y+f1.y_scale,f2.y+f2.y_scale)
    rigth =  min(f1.x+f1.x_scale,f2.x+f2.x_scale)
    bot = max(f1.y,f2.y)

    f3 = Figure()
    f3.x = left
    f3.x_scale = rigth - left
    f3.y = bot
    f3.y_scale = top - bot

    if ((f3.x_scale < 0) or (f3.y_scale < 0)): return None
    else: return f3

print("Hello! Write x0, y0, x-scale, y-scale of first figure: ")
answer = input().split(", ");
f1 = Figure(int(answer[0]), int(answer[1]), int(answer[2]), int(answer[3]))

print("Write x0, y0, x-scale, y-scale of second figure: ")
answer = input().split(", ");
f2 = Figure(int(answer[0]), int(answer[1]), int(answer[2]), int(answer[3]))

print("x0, y0, x-scale, y-scale")

f3 = merge(f1,f2)
print("Merge result: ", f3.x, ",", f3.y, ",", f3.x_scale, ",", f3.y_scale)

f4 = inter (f1,f2)
if f4 == None: print("No interence")
else:
    print("Inter result: ", f4.x, ",", f4.y, ",", f4.x_scale, ",", f4.y_scale)
