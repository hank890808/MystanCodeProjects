"""
File: my_drawing.py
Name: Hank 蕭承瀚
----------------------
This file is a drawing of an alpaca.
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel, GPolygon
from campy.graphics.gwindow import GWindow
from campy.graphics.gimage import GImage

# The image I want to draw
img = GImage("請截圖my_drawing作品及創作理念並放到此資料夾/蕭承瀚_原圖.jpg")
# The window is as large as the origin image
window = GWindow(width=img.width, height=img.height)


def main():
    """
    Title: りしれ畫さ小？

    這隻羊駝(應該)是最近在玩的遊戲中的一隻寵物，
    很ㄎㄧㄤ很可愛，所以就將一張別人做的梗圖作為原圖來做此次作品～
    """
    # window.add(img)
    background()
    alpaca()
    text()
    # reference_line()


def background():
    background_color()
    # table()
    # table_base()


def alpaca():
    head()
    ear()
    eye()
    nose_mouth()
    body()


def text():
    label = GLabel("り し れ 畫 さ 小 ？", x=100, y=380)
    label.color = "white"
    label.font = "-35-bold"
    window.add(label)


def reference_line():
    n = 50
    for i in range(window.width//n):
        vertical_line((i+1)*n)
        horizontal_line((i+1)*n)


def background_color():
    bg = GRect(window.width, window.height)
    color_bg = "black"
    bg.color = color_bg
    bg.filled = True
    bg.fill_color = color_bg
    window.add(bg)


def table():
    table1 = GPolygon()
    table1.add_vertex((0, 17))
    table1.add_vertex((141, 17))
    table1.add_vertex((503, 0))
    table1.add_vertex((window.width, 0))
    table1.add_vertex((window.width, 50))
    table1.add_vertex((250, 66))
    table1.add_vertex((0, 70))
    color = "sandybrown"
    table1.color = color
    table1.filled = True
    table1.fill_color = color
    window.add(table1)
    table2 = GPolygon()
    table2.add_vertex((window.width, 50))
    table2.add_vertex((250, 66))
    table2.add_vertex((0, 70))
    table2.add_vertex((0, 121))
    table2.add_vertex((window.width, 98))
    color = "sienna"
    table2.color = color
    table2.filled = True
    table2.fill_color = color
    window.add(table2)


def table_base():
    base = GRect(50, 400, x=50, y=100)
    color = "sienna"
    base.color = color
    base.filled = True
    base.fill_color = color
    window.add(base)


def head():
    head = GPolygon()
    head.add_vertex((221, 75))
    head.add_vertex((330, 55))
    head.add_vertex((400, 128)) # r_ear
    head.add_vertex((406, 190))
    head.add_vertex((392, 210))
    head.add_vertex((215, 230)) # neck
    head.add_vertex((185, 200))
    head.add_vertex((180, 163)) # l_ear
    head.add_vertex((195, 120))
    color = "cadetblue"
    head.color = color
    head.filled = True
    head.fill_color = color
    window.add(head)

    shadow_dark = GPolygon()
    shadow_dark.add_vertex((221, 75))
    shadow_dark.add_vertex((330, 55))
    shadow_dark.add_vertex((400, 128))
    shadow_dark.add_vertex((406, 190))
    shadow_dark.add_vertex((392, 210))
    shadow_dark.add_vertex((375, 226))
    shadow_dark.add_vertex((392, 193))
    shadow_dark.add_vertex((382, 176))
    shadow_dark.add_vertex((395, 154))
    shadow_dark.add_vertex((383, 136))
    shadow_dark.add_vertex((363, 122))
    shadow_dark.add_vertex((330, 74))
    shadow_dark.add_vertex((273, 66))
    color_shadow_dark = "lightslategrey"
    shadow_dark.color = color_shadow_dark
    shadow_dark.filled = True
    shadow_dark.fill_color = color_shadow_dark
    window.add(shadow_dark)

    shadow_bright = GPolygon()
    shadow_bright.add_vertex((286, 63))
    shadow_bright.add_vertex((221, 75))
    shadow_bright.add_vertex((195, 120))
    shadow_bright.add_vertex((180, 163))
    shadow_bright.add_vertex((185, 200))
    shadow_bright.add_vertex((215, 230))
    shadow_bright.add_vertex((232, 231))
    shadow_bright.add_vertex((197, 204))
    shadow_bright.add_vertex((181, 169))
    shadow_bright.add_vertex((203, 110))
    shadow_bright.add_vertex((226, 86))
    color_shadow_bright = "powderblue"
    shadow_bright.color = color_shadow_bright
    shadow_bright.filled = True
    shadow_bright.fill_color = color_shadow_bright
    window.add(shadow_bright)


def ear():
    l_ear = GPolygon()
    l_ear.add_vertex((180, 163))
    l_ear.add_vertex((174, 166))
    l_ear.add_vertex((163, 171))
    l_ear.add_vertex((145, 167))
    l_ear.add_vertex((107, 153))
    l_ear.add_vertex((110, 192))
    l_ear.add_vertex((139, 196))
    l_ear.add_vertex((168, 187))
    l_ear.add_vertex((181, 183))
    color = "powderblue"
    l_ear.color = color
    l_ear.filled = True
    l_ear.fill_color = color
    window.add(l_ear)

    r_ear = GPolygon()
    r_ear.add_vertex((400, 128))
    r_ear.add_vertex((425, 145))
    r_ear.add_vertex((457, 139))
    r_ear.add_vertex((491, 146))
    r_ear.add_vertex((481, 155))
    r_ear.add_vertex((458, 157))
    r_ear.add_vertex((438, 173))
    r_ear.add_vertex((413, 166))
    r_ear.add_vertex((405, 151))
    r_ear.color = color
    r_ear.filled = True
    r_ear.fill_color = color
    window.add(r_ear)

    shadow = GPolygon()
    shadow.add_vertex((400, 128))
    shadow.add_vertex((425, 145))
    shadow.add_vertex((422, 149))
    shadow.add_vertex((410, 144))
    shadow.add_vertex((407, 147))
    shadow.add_vertex((432, 163))
    shadow.add_vertex((458, 157))
    shadow.add_vertex((438, 173))
    shadow.add_vertex((413, 166))
    shadow.add_vertex((403, 151))
    color_shadow = "lightslategrey"
    shadow.color = color_shadow
    shadow.filled = True
    shadow.fill_color = color_shadow
    window.add(shadow)


def eye():
    l_eye = GPolygon()
    l_eye.add_vertex((246, 154))
    l_eye.add_vertex((198, 147))
    l_eye.add_vertex((191, 152))
    l_eye.add_vertex((190, 168))
    l_eye.add_vertex((242, 164))
    color_eye = "light_cyan"
    l_eye.color = color_eye
    l_eye.filled = True
    l_eye.fill_color = color_eye
    window.add(l_eye)
    r_eye = GPolygon()
    r_eye.add_vertex((292, 153))
    r_eye.add_vertex((347, 139))
    r_eye.add_vertex((386, 147))
    r_eye.add_vertex((385, 152))
    r_eye.add_vertex((316, 160))
    r_eye.add_vertex((291, 159))
    r_eye.color = color_eye
    r_eye.filled = True
    r_eye.fill_color = color_eye
    window.add(r_eye)
    l_eyeball = GOval(21, 23, x=202, y=145)
    color_eyeball = "black"
    l_eyeball.color = color_eyeball
    l_eyeball.filled = True
    l_eyeball.fill_color = color_eyeball
    window.add(l_eyeball)
    r_eyeball = GOval(28, 28, x=315, y=131)
    r_eyeball.color = color_eyeball
    r_eyeball.filled = True
    r_eyeball.fill_color = color_eyeball
    window.add(r_eyeball)
    l_block1 = GPolygon()
    l_block1.add_vertex((246, 154))
    l_block1.add_vertex((198, 147))
    l_block1.add_vertex((219, 133))
    color_block= "cadetblue"
    l_block1.color = color_block
    l_block1.filled = True
    l_block1.fill_color = color_block
    window.add(l_block1)
    l_block2 = GPolygon()
    l_block2.add_vertex((190, 168))
    l_block2.add_vertex((242, 164))
    l_block2.add_vertex((215, 179))
    l_block2.color = color_block
    l_block2.filled = True
    l_block2.fill_color = color_block
    window.add(l_block2)
    r_block1 = GPolygon()
    r_block1.add_vertex((292, 153))
    r_block1.add_vertex((347, 139))
    r_block1.add_vertex((335, 119))
    r_block1.color = color_block
    r_block1.filled = True
    r_block1.fill_color = color_block
    window.add(r_block1)
    r_block2 = GPolygon()
    r_block2.add_vertex((385, 152))
    r_block2.add_vertex((316, 160))
    r_block2.add_vertex((335, 168))
    r_block2.color = color_block
    r_block2.filled = True
    r_block2.fill_color = color_block
    window.add(r_block2)


def nose_mouth():
    nose_base = GPolygon()
    nose_base.add_vertex((253, 147))
    nose_base.add_vertex((246, 178))
    nose_base.add_vertex((273, 211))
    nose_base.add_vertex((288, 187))
    nose_base.add_vertex((286, 164))
    nose_base.add_vertex((277, 143))
    color = "white"
    nose_base.color = color
    nose_base.filled = True
    nose_base.fill_color = color
    window.add(nose_base)

    nose_shadow = GPolygon()
    nose_shadow.add_vertex((246, 178))
    nose_shadow.add_vertex((273, 211))
    nose_shadow.add_vertex((288, 187))
    nose_shadow.add_vertex((287, 176))
    color_nose_shadow = "lightgrey"
    nose_shadow.color = color_nose_shadow
    nose_shadow.filled = True
    nose_shadow.fill_color = color_nose_shadow
    window.add(nose_shadow)

    nose = GOval(11, 6, x=256, y=167)
    nose.color = "thistle"
    nose.filled = True
    nose.fill_color = "thistle"
    window.add(nose)

    mouth1 = GLine(262, 174, 264, 187)
    mouth_color = "grey"
    mouth1.color = mouth_color
    window.add(mouth1)

    mouth2 = GPolygon()
    mouth2.add_vertex((252, 183))
    mouth2.add_vertex((265, 189))
    mouth2.add_vertex((287, 176))
    mouth2.add_vertex((265, 188))
    mouth2.color = mouth_color
    mouth2.filled = True
    mouth2.fill_color = mouth_color
    window.add(mouth2)


def body():
    body = GPolygon()
    body.add_vertex((392, 210))
    body.add_vertex((215, 230))
    body.add_vertex((225, 375))
    body.add_vertex((205, 450))
    body.add_vertex((428, 450))
    body.add_vertex((411, 436))
    body.add_vertex((375, 429))
    body.add_vertex((365, 384))
    color = "cadetblue"
    body.color = color
    body.filled = True
    body.fill_color = color
    window.add(body)

    shadow_dark = GPolygon()
    shadow_dark.add_vertex((392, 210))
    shadow_dark.add_vertex((385, 210))
    shadow_dark.add_vertex((368, 241))
    shadow_dark.add_vertex((344, 345))
    shadow_dark.add_vertex((344, 401))
    shadow_dark.add_vertex((360, 450))
    shadow_dark.add_vertex((428, 450))
    shadow_dark.add_vertex((411, 436))
    shadow_dark.add_vertex((375, 429))
    shadow_dark.add_vertex((365, 384))
    color_shadow_dark = "lightslategrey"
    shadow_dark.color = color_shadow_dark
    shadow_dark.filled = True
    shadow_dark.fill_color = color_shadow_dark
    window.add(shadow_dark)

    shadow_bright = GPolygon()
    shadow_bright.add_vertex((215, 230))
    shadow_bright.add_vertex((230, 228))
    shadow_bright.add_vertex((230, 323))
    shadow_bright.add_vertex((225, 369))
    shadow_bright.add_vertex((225, 375))
    color_shadow_bright = "powderblue"
    shadow_bright.color = color_shadow_bright
    shadow_bright.filled = True
    shadow_bright.fill_color = color_shadow_bright
    window.add(shadow_bright)

    hair(259, 305, 293, 313, 296, 269, 271, 256)
    hair(299, 308, 318, 304, 311, 284, 291, 281)
    hair(337, 294, 356, 285, 329, 255, 312, 259)
    hair(222, 281, 239, 296, 269, 272, 249, 257)
    hair(196, 266, 208, 276, 232, 267, 236, 258)
    hair(223, 271, 242, 282, 264, 250, 250, 247)
    hair(253, 279, 295, 276, 292, 240, 266, 247)
    hair(293, 294, 333, 280, 312, 243, 287, 250)
    hair(246, 234, 230, 257, 282, 257, 286, 236)
    hair(300, 243, 318, 272, 349, 264, 331, 236)
    hair(231, 231, 219, 241, 233, 246, 242, 235)
    hair(366, 266, 379, 257, 367, 236, 358, 243)
    hair(343, 235, 353, 247, 366, 239, 364, 231)
    hair(353, 229, 381, 241, 388, 232, 369, 225)
    hair(270, 345, 282, 389, 315, 385, 314, 349)
    hair(258, 341, 258, 379, 270, 381, 277, 347)
    hair(334, 398, 369, 393, 358, 373, 334, 376)
    hair(359, 373, 376, 394, 388, 381, 366, 368)
    hair(317, 373, 339, 361, 337, 341, 307, 351)
    hair(224, 370, 229, 369, 240, 343, 225, 341)
    hair(221, 384, 202, 394, 202, 404, 218, 405)
    hair(250, 390, 247, 421, 258, 421, 260, 392)
    hair(231, 381, 226, 409, 233, 413, 241, 384)
    hair(236, 409, 245, 412, 248, 386, 238, 385)
    hair(260, 401, 250, 425, 287, 433, 292, 408)
    hair(287, 407, 294, 427, 310, 419, 306, 408)


def hair(x1, y1, x2, y2, x3, y3, x4, y4):
    hair = GPolygon()
    hair.add_vertex((x1, y1))
    hair.add_vertex((x2, y2))
    hair.add_vertex((x3, y3))
    hair.add_vertex((x4, y4))
    color_hair = "powderblue"
    color_body = "cadetblue"
    hair.color = color_body
    hair.filled = True
    hair.fill_color = color_hair
    window.add(hair)


def vertical_line(x):
    line = GLine(x, 0, x, window.height)
    window.add(line)


def horizontal_line(y):
    line = GLine(0, y, window.width, y)
    window.add(line)


if __name__ == '__main__':
    main()
