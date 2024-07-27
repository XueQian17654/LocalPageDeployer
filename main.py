#            -*- coding:utf-8 -*-             #
#     Copyright (c) 2019 - 2039 XueQian       #
import time
import threading
import pyperclip
import os
import socket
import random

from tkinter import font, ttk, filedialog, messagebox
from tkinter import Tk, Button, Toplevel, VERTICAL, RIGHT, Y
# import logging as log
from flask import Flask, request, send_file

app = Flask(__name__)
pages = {}
log = {}



def mima(num=6, bm='zn') -> str:
    if not isinstance(num, int):
        raise TypeError('The num is not int')

    t = [
        '△', '▽', '○', '◇', '□', '☆', '▷', '◁', '♤', '♡', '♢', '♧', '▲', '▼', '●', '◆', '■', '★', '▶', '◀', '♠',
        '♥', '♦', '♣', '☼', '☽', '♀', '☺', '◐', '☑', '√', '✔', '☜', '☝', '☞', '㏂', '☀', '☾', '♂', '☹', '◑', '×',
        '☒', '✘', '☚', '☟', '☛', '㏘', '▪', '•', '‥', '…', '▁', '▂', '▃', '▅', '▆', '▇', '█', '∷', '※', '░', '▒',
        '▓', '▏', '▎', '▌', '▋', '▊', '▉', '♩', '♪', '♫', '♬', '§''〼', '◎', '¤', '۞', '℗', '®', '©', '♭', '♯', '♮',
        '‖', '¶', '卍', '卐', '▬', '〓', '℡', '™', '㏇', '☌', '☍', '☋', '☊', '㉿', '◮', '◪', '◔', '◕', '@', '㈱', '№',
        '♈', '♉', '♊', '♋', '♌', '♎', '♏', '♐', '♑', '♓', '♒', '♍', '↖', '↑', '↗', '▨', '▤', '▧', '◤', '㊤', '◥',
        '☴', '☲', '☷', '☱', '☯', '☳', '㊨', '㊥', '㊧', '▥', '▦', '▩', '→', '㊣', '←', '↙', '↓', '↘', '▫', '◈', '▣',
        '◣', '㊦', '◢', '☶', '☵', '☰', '‡', '†', '▔', '￢', '¬', '⊰', '⋚', '⋌', '⋛', '⊱', '↔', '↕', '*', '＊', '✲',
        '❈', '❉', '✿', '❀', '❃', '❁', '☸', '✖', '✚', '✪', '❤', 'ღ', '❧', 'ி', '₪', '✎', '✍', '✌', '✁', '✄', '☁',
        '☂', '☃', '☄', '♨', '☇', '☈', '☡', '➷', '⊹', '✉', '☏', '✙', '✟', '☤', '☥', '☦', '☧', '☨', '☫', '☬', '♟',
        '♙', '♜', '♖', '♞', '♘', '♝', '♗', '♛', '♕', '♚', '♔', '☥'
    ]
    z = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z'
    ]
    d = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
        'V', 'W', 'X', 'Y', 'Z'
    ]
    n = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
    ]
    _bin = [
        'a', 'b', 'c', 'd', 'e', 'f'
    ]

    a = []
    if bm == '':
        print(
            'Welcome to Xueqian random number. You have not entered the character type (t: special character; z: lowercase letter; d: capital letter; n: number. Can be superimposed.).')
        a = []
    for i in list(bm):
        try:
            [a.append(i) for i in eval(i.replace('i', '_bin'))]
        except:
            raise NameError('The bm is not in it')

    mm = ''
    try:
        for i in range(num):
            mm = mm + str(a[random.randint(0, len(a) - 1)])
    except:
        pass
    return mm



def t():
    def refresh():
        tree.delete(*tree.get_children())
        for i in pages:
            temp = tree.insert('', index=0)  # 新建行
            tree.set(temp, column='key', value=i)
            tree.set(temp, column='road', value=pages[i])
        return 0
    
    def d():
        [pages.pop(tree.item(i)['values'][0]) for i in tree.selection()]
        return refresh()
    
    def c():
        try:
            pyperclip.copy(tree.item(tree.selection()[0])['values'][0])
            return 0
        except:
            return -1
    
    def a():
        pa = filedialog.askdirectory()
        if pa == '':
            return -1
        pages[mima(10, 'zdn')] = pa.replace('/', '\\')
        return refresh()
    
    def look():
        loge.config(state="disabled")

        r1 = Toplevel()
        r1.title('Flask部署日志查看器（不会自动刷新）')
        r1.geometry("700x392")
        r1.resizable(False, False)
        r1.protocol('WM_DELETE_WINDOW', lambda: [loge.config(state="normal"), r1.destroy()])

        tree1 = ttk.Treeview(r1, columns=[], height=19, show="tree")
        tree1.column('#0', width=669)

        vbar1 = ttk.Scrollbar(r1, orient=VERTICAL, command=tree1.yview)
        tree1.config(yscrollcommand=vbar1.set)
        vbar1.pack(side=RIGHT, fill=Y)

        inu = 0
        for i in log:
            x = tree1.insert('', inu, i, text=i, values=('',))
            lol = log[i][::-1]
            for ii in range(len(lol)):
                tree1.insert(x, ii, text=lol[ii], values=('',))
            inu += 1

        tree1.place(x=5, y=5)

        r1.mainloop()

    r = Tk()
    r.title(f'Flask部署路由配置器 (Host&Ip: {ip}; Port: 1880)')
    r.geometry("600x500")
    r.resizable(False, False)
    r.protocol('WM_DELETE_WINDOW', lambda: (os._exit(-1) if messagebox.askyesno('确认...', '确定要关闭程序吗？') else ''))

    custom_font = font.Font(family="等线", size=15)

    tree = ttk.Treeview(r, columns=['key', 'road'], height=19, show='headings')

    tree.column('key', width=90, anchor='center')
    tree.heading('key', text='代码')
    tree.column('road', width=498, anchor='w')
    tree.heading('road', text='现实路径')

    # vbar1 = ttk.Scrollbar(tree, orient=tkinter.VERTICAL, command=tree.yview)
    # tree.configure(yscrollcommand=vbar1.set)
    # vbar1.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    
    refresh()

    tree.place(x=5, y=5)

    adde = Button(r, text="添加", command=a, font=custom_font)
    adde.place(x=20, y=430)
    cope = Button(r, text="复制", command=c, font=custom_font)
    cope.place(x=90, y=430)
    dele = Button(r, text="删除", command=d, font=custom_font)
    dele.place(x=160, y=430)
    loge = Button(r, text="日志", command=look, font=custom_font)
    loge.place(x=300, y=430)

    r.mainloop()


def addlog(t, c):
    if t not in log:
        log[t] = []
    log[t].append(c)
    return


@app.after_request
def HARt(response):
    ti = time.strftime('%Y-%m-%d, %H:%M:%S', time.localtime(time.time()))
    y = request.url[len(request.url_root):]
    bas = f'[{ti}] [{request.remote_addr}] <{response.status_code}> <{request.method}> "{y}"'
    if '/' not in y:
        addlog('RouteError', bas)
        return response
    key = y.split('/')[0]
    road = y[len(key):].replace('/', '\\')
    if key not in pages:
        addlog('KeyError', bas)
        return response

    os.path.isfile(pages[key] + road)
    if os.path.isfile(pages[key] + road):
        addlog(key, f'Successful -> {bas}')
        return response
    
    addlog(key, f'RoadError --> {bas}')

    return response


@app.errorhandler(404)
def zy(e):
    y = request.url[len(request.url_root):]
    if '/' not in y:
        return f'<title>Hello!</title><h2>No page here...</h2><h3>Route: &lt;<span style="color:red;">{y}</span>&gt;</h3><h3 style="color:#f60;">Copyright (c) 2019 - 2039 XueQian</h3>'
    key = y.split('/')[0]
    road = y[len(key):].replace('/', '\\')
    if key not in pages:
        return f'<title>Hello!</title><h2>No page here...</h2><h3>Key: &lt;<span style="color:red;">{key}</span>&gt;</h3><h3 style="color:#f60;">Copyright (c) 2019 - 2039 XueQian</h3>'
    if os.path.isfile(pages[key] + road):
        return send_file(pages[key] + road)
    return f'<title>Hello!</title><h2>No file here...</h2><h3>Key: &lt;<span style="color:green;">{key}</span>&gt;</h3><h3>Road: &lt;<span style="color:red;">{road}</span>&gt;</h3><h3 style="color:#f60;">Copyright (c) 2019 - 2039 XueQian</h3>'



if __name__ == '__main__':
    # log.basicConfig(filename=".\\log.txt", format='%(asctime)s :: %(message)s')
    ip = '0.0.0.0'
    try: 
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
        s.connect(('8.8.8.8',80)) 
        ip = s.getsockname()[0] 
    finally:
        s.close()

    print(" * Run's time: " + time.strftime('%Y-%m-%d, %H:%M:%S', time.localtime(time.time())))

    threading.Thread(target=t).start()
    app.run(host=ip, port=1880, debug=False)

# host='21.0.16.240'
