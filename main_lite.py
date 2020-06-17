from tkinter import Button, Frame, LabelFrame, Menu, Tk, Checkbutton, BooleanVar
import tkinter.messagebox
import os
# from matplotlib import image as imgplt
# from matplotlib import pyplot as plt
# import ctypes

def showImg(path, flag = 0, bakpath = ''):
   if flag:
      os.startfile(bakpath)
   else:
      os.startfile(path)
      # x = imgplt.imread(path)
      # plt.imshow(x)
      # plt.axis('off')
      # plt.show()
      # plt.waitforbuttonpress(0)
      
      # img=Image.open(path)
      # img.show()

def setGrid(root, minsize):
   col_count, row_count = root.grid_size()
 
   for col in range(col_count):
      root.grid_columnconfigure(col, minsize=minsize)
   for row in range(row_count):
      root.grid_rowconfigure(row, minsize=minsize)

def showWindow(tag):
   subWindow = Tk()
   if tag == 'map':
      subWindow.title('地图')
      subWindow.geometry('450x400')
      rootpath = os.getcwd()+os.sep+'archive'+os.sep+'map'

      leftBg = Frame(subWindow)
      var = BooleanVar(leftBg)
      check = Checkbutton(leftBg, text = "生成HTML文件而非图片", variable=var).grid(row=0, column=1, columnspan=3)

      hit1 = Button(leftBg, text = "全国各地疫情关注情况热力图1", command = lambda: showImg(rootpath+os.sep+'png'+os.sep+'全国各地疫情关注情况热力图1.png', var.get(), rootpath+os.sep+'html'+os.sep+'全国各地疫情关注情况热力图1.html')).grid(row=2, column=1)
      hit2 = Button(leftBg, text = "全国各地疫情关注情况热力图2", command = lambda: showImg(rootpath+os.sep+'png'+os.sep+'全国各地疫情关注情况热力图2.png', var.get(), rootpath+os.sep+'html'+os.sep+'全国各地疫情关注情况热力图2.html')).grid(row=4, column=1)
      hit3 = Button(leftBg, text = "全国各地疫情关注情况热力图3", command = lambda: showImg(rootpath+os.sep+'png'+os.sep+'全国各地疫情关注情况热力图3.png', var.get(), rootpath+os.sep+'html'+os.sep+'全国各地疫情关注情况热力图3.html')).grid(row=6, column=1)
      fill1 = Button(leftBg, text = "全国各地疫情关注情况填充图1", command = lambda: showImg(rootpath+os.sep+'png'+os.sep+'全国各地疫情关注情况填充图1.png', var.get(), rootpath+os.sep+'html'+os.sep+'全国各地疫情关注情况填充图1.html')).grid(row=8 , column=1)
      fill2 = Button(leftBg, text = "全国各地疫情关注情况填充图2", command = lambda: showImg(rootpath+os.sep+'png'+os.sep+'全国各地疫情关注情况填充图2.png', var.get(), rootpath+os.sep+'html'+os.sep+'全国各地疫情关注情况填充图2.html')).grid(row=10, column=1)
      fill3 = Button(leftBg, text = "全国各地疫情关注情况填充图3", command = lambda: showImg(rootpath+os.sep+'png'+os.sep+'全国各地疫情关注情况填充图3.png', var.get(), rootpath+os.sep+'html'+os.sep+'全国各地疫情关注情况填充图3.html')).grid(row=12, column=1)
      hbHit = Button(leftBg, text = "疫情期间湖北各市受关注度分布", command = lambda: showImg(rootpath+os.sep+'png'+os.sep+'疫情期间湖北各市受关注度分布.png', var.get(), rootpath+os.sep+'html'+os.sep+'疫情期间湖北各市受关注度分布.html')).grid(row=2, column=3)
      nationalHit = Button(leftBg, text = "疫情期间全国各地受关注度分布", command = lambda: showImg(rootpath+os.sep+'png'+os.sep+'疫情期间全国各地受关注度分布.png', var.get(), rootpath+os.sep+'html'+os.sep+'疫情期间全国各地受关注度分布.html')).grid(row=4, column=3)
      pst = Button(leftBg, text = "疫情期间全国各地积极度", command = lambda: showImg(rootpath+os.sep+'png'+os.sep+'疫情期间全国各地积极度.png', var.get(), rootpath+os.sep+'html'+os.sep+'疫情期间全国各地积极度.html')).grid(row=6, column=3)
      ngt = Button(leftBg, text = "疫情期间全国各地消极度", command = lambda: showImg(rootpath+os.sep+'png'+os.sep+'疫情期间全国各地消极度.png', var.get(), rootpath+os.sep+'html'+os.sep+'疫情期间全国各地消极度.html')).grid(row=8, column=3)
      stm = Button(leftBg, text = "疫情期间全国各地情绪分布", command = lambda: showImg(rootpath+os.sep+'png'+os.sep+'疫情期间全国各地情绪分布.png', var.get(), rootpath+os.sep+'html'+os.sep+'疫情期间全国各地情绪分布.html')).grid(row=10, column=3)

      emptyBottom = Frame(leftBg).grid(row=11, column = 4)

      setGrid(leftBg, 20)
      leftBg.pack()

   elif tag == 'wordcloud':
      subWindow.title('词云图')
      subWindow.geometry('400x300')
      rootpath = os.getcwd()+os.sep+'archive'+os.sep+'wordcloud'

      bg = Frame(subWindow)
      botton1 = Button(bg, text = "疫情", command = lambda: showImg(rootpath+os.sep+'武汉 疫情 口罩 医院 战疫 钟南山 肺炎.jpg')).grid(row=1)
      botton2 = Button(bg, text = "作息", command = lambda: showImg(rootpath+os.sep+'熬夜 吃饭 早饭 午饭 晚饭 夜宵 睡觉 起床.jpg')).grid(row=3)
      botton3 = Button(bg, text = "复工复产", command = lambda: showImg(rootpath+os.sep+'上班 办公室 复工 复产 工作.jpg')).grid(row=5)
      botton4 = Button(bg, text = "复学", command = lambda: showImg(rootpath+os.sep+'开学 返校 复学.jpg')).grid(row=7)

      emptyBottom = Frame(bg).grid(row=8)
      setGrid(bg, 20)
      bg.pack()

   elif tag == 'chart':
      subWindow.title('折线图')
      subWindow.geometry('400x300')
      rootpath = os.getcwd()+os.sep+'archive'+os.sep+'chart'
      # 博客数
      leftBg = Frame(subWindow)
      leftLabelFrame = LabelFrame(subWindow, text = "媒体博客数", labelanchor="nw")
      leftLabelFrame.place(relx=0.02, rely=0.02, relwidth=0.47, relheight=0.96)
      leftBg = Frame(leftLabelFrame)
      mapBotton1 = Button(leftBg, text = "疫情", command = lambda: showImg(rootpath+os.sep+'media武汉 疫情 口罩 医院 战疫 钟南山 肺炎.png')).grid(row=1)
      wordBotton1 = Button(leftBg, text = "作息", command = lambda: showImg(rootpath+os.sep+'media熬夜 吃饭 早饭 午饭 晚饭 夜宵 睡觉 起床.png')).grid(row=3)
      chartBotton1 = Button(leftBg, text = "复工复产", command = lambda: showImg(rootpath+os.sep+'media上班 办公室 复工 复产 工作.png')).grid(row=5)
      betaBotton1 = Button(leftBg, text = "复学", command = lambda: showImg(rootpath+os.sep+'media开学 返校 复学.png')).grid(row=7)

      emptyBottom1 = Frame(leftBg).grid(row=8)

      setGrid(leftBg, 20)
      leftBg.pack()

      # 评论&转发
      rightLabelFrame = LabelFrame(subWindow, text = "评论数与转发数", labelanchor="nw")
      rightLabelFrame.place(relx=0.51, rely=0.02, relwidth=0.47, relheight=0.96)
      rightBg = Frame(rightLabelFrame)
      mapBotton2 = Button(rightBg, text = "疫情", command = lambda: showImg(rootpath+os.sep+'武汉 疫情 口罩 医院 战疫 钟南山 肺炎.png')).grid(row=1)
      wordBotton2 = Button(rightBg, text = "作息", command = lambda: showImg(rootpath+os.sep+'熬夜 吃饭 早饭 午饭 晚饭 夜宵 睡觉 起床.png')).grid(row=3)
      chartBotton2 = Button(rightBg, text = "复工复产", command = lambda: showImg(rootpath+os.sep+'上班 办公室 复工 复产 工作.png')).grid(row=5)
      betaBotton2 = Button(rightBg, text = "复学", command = lambda: showImg(rootpath+os.sep+'开学 返校 复学.png')).grid(row=7)

      emptyBottom2 = Frame(rightBg).grid(row=8)

      setGrid(rightBg, 20)
      rightBg.pack()

   elif tag == 'sentiment':
      subWindow.title('NLP情绪分析(Beta)')
      subWindow.geometry('400x450')
      rootpath = os.getcwd()+os.sep+'archive'+os.sep+'sentimentchart (Beta)'

      bg = Frame(subWindow)
      botton1 = Button(bg, text = "分组1-数量图", command = lambda: showImg(rootpath+os.sep+'bar result1.png')).grid(row=1)
      botton2 = Button(bg, text = "分组2-数量图", command = lambda: showImg(rootpath+os.sep+'bar result1.png')).grid(row=3)
      botton3 = Button(bg, text = "分组3-数量图", command = lambda: showImg(rootpath+os.sep+'bar result1.png')).grid(row=5)
      botton4 = Button(bg, text = "箱型图", command = lambda: showImg(rootpath+os.sep+'box.png')).grid(row=7)
      botton4 = Button(bg, text = "密度图", command = lambda: showImg(rootpath+os.sep+'density.png')).grid(row=9)

      emptyBottom = Frame(bg).grid(row=10)
      setGrid(bg, 20)
      bg.pack()

   subWindow.mainloop()

# ctypes.windll.shcore.SetProcessDpiAwareness(1)
# ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
# root.tk.call('tk', 'scaling', ScaleFactor/75)

mainWindow = Tk()
mainWindow.title('DataVisualization')
mainWindow.geometry('400x300')

# menubar
'''
menubar = Menu(mainWindow)
crawlerMenu = Menu(menubar, tearoff=0)
betaMenu = Menu(menubar, tearoff=0)
aboutMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='爬虫', menu=crawlerMenu)
menubar.add_cascade(label='Beta', menu=betaMenu)
menubar.add_cascade(label='关于', menu=aboutMenu)

aboutMenu.add_command(label='小组', command=lambda: tkinter.messagebox.showinfo("测试中", "测试中"))
crawlerMenu.add_command(label='修改uidlist', command = lambda: os.startfile('source'+os.sep+'uidlist.txt'))
crawlerMenu.add_separator()
crawlerMenu.add_command(label='运行', command=lambda: tkinter.messagebox.showinfo("测试中", "测试中"))
betaMenu.add_command(label='导入语料库', command=lambda: tkinter.messagebox.showinfo("测试中", "测试中"))
betaMenu.add_command(label='训练模型', command=lambda: tkinter.messagebox.showinfo("测试中", "测试中"))
betaMenu.add_separator()
betaMenu.add_command(label='分析', command=lambda: tkinter.messagebox.showinfo("测试中", "测试中"))
'''

# left label frame
leftLabelFrame = LabelFrame(mainWindow, text = "选择要查看的类别", labelanchor="nw")
leftLabelFrame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
leftBg = Frame(leftLabelFrame)
mapBotton1 = Button(leftBg, text = "地图", command = lambda: showWindow('map')).grid(row=1)
wordBotton1 = Button(leftBg, text = "词云", command = lambda: showWindow('wordcloud')).grid(row=3)
chartBotton1 = Button(leftBg, text = "图表", command = lambda: showWindow('chart')).grid(row=5)
betaBotton1 = Button(leftBg, text = "NLP情绪分析(Beta)", command = lambda: showWindow('sentiment')).grid(row=7)

emptyBottom1 = Frame(leftBg).grid(row=8)

setGrid(leftBg, 20)
leftBg.pack()

# Right label frame
'''
rightLabelFrame = LabelFrame(mainWindow, text = "查看现有示例", labelanchor="nw")
rightLabelFrame.place(relx=0.51, rely=0.02, relwidth=0.47, relheight=0.96)
rightBg = Frame(rightLabelFrame)
mapBotton2 = Button(rightBg, text = "地图", command = lambda: os.startfile('archive'+os.sep+'map')).grid(row=1)
wordBotton2 = Button(rightBg, text = "词云", command = lambda: os.startfile('archive'+os.sep+'wordcloud')).grid(row=3)
chartBotton2 = Button(rightBg, text = "图表", command = lambda: os.startfile('archive'+os.sep+'chart')).grid(row=5)
betaBotton2 = Button(rightBg, text = "NLP情绪分析(Beta)", command = lambda: os.startfile('archive'+os.sep+'sentimentchart (Beta)')).grid(row=7)

emptyBottom2 = Frame(rightBg).grid(row=8)

setGrid(rightBg, 20)
rightBg.pack()
'''

# mainWindow.config(menu=menubar)
mainWindow.mainloop()

# def helloCallBack():
#    tkMessageBox.showinfo( "Hello Python", "Hello Runoob")
 
