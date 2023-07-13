from calendar import c
from xml.etree.ElementTree import C14NWriterTarget
import pandas as pd
import numpy as np

#全局变量
points = {}  #蚁群处理目标坐标
best_path=[]  #最佳路径
best_length=0  #最佳长度
INF=999999  #无穷大
Start_city=''  #起点位置
Inmeal = {}  #送餐信息输入
OutPut = ""  #信息输出
A1=[]
A2=[]
S=[]
#点位距离矩阵

#程序启动函数
def Start():
    #数据导入
    print("Start()运行……")
    global Inmeal
    global OutPut
    DateB()
    df = pd.read_excel('Inmeal.xlsx')
    q1=int(df.iloc[0, 0])
    q2=int(df.iloc[1, 0])
    q3=int(df.iloc[2, 0])
    q4=int(df.iloc[3, 0])
    q5=int(df.iloc[4, 0])
    q6=int(df.iloc[5, 0])
    l1=int(df.iloc[6, 0])
    l2=int(df.iloc[7, 0])
    l3=int(df.iloc[8, 0])
    l4=int(df.iloc[9, 0])
    c1=int(df.iloc[0, 1])
    c2=int(df.iloc[1, 1])
    c3=int(df.iloc[2, 1])
    c4=int(df.iloc[3, 1])
    p1=int(df.iloc[4, 1])
    p2=int(df.iloc[5, 1])
    p3=int(df.iloc[6, 1])
    p4=int(df.iloc[7, 1])

    #诚朴+崇实园
    if True:
        Inmeal={'P1':p1,'P2':p2,'P3':p3,'P4':p4,'C1':c1,'C2':c2,'C3':c3,'C4':c4}
        num=sum(Inmeal.values())
        if (num == 0):
            OutPut += "诚朴+崇实园没有检测到送餐需求。\n\n"
        elif num <= 300:
            MA2()
        else:
            OutPut += "诚朴+崇实园的车车不够用了，所以一份也没送，罢工！\n\n"

    #启智+理科群
    if True:
        Inmeal={'Q1':q1,'Q2':q2,'Q3':q3,'Q4':q4,'Q5':q5,'Q6':q6,'L1':l1,'L2':l2,'L3':l3,'L4':l4}
        num=sum(Inmeal.values())
        if (num == 0):
            OutPut += "启智+理科群没有检测到送餐需求。\n\n"
        elif num <= 300:
            MA1()
        else:
            OutPut += "启智+理科群的车车不够用了，所以一份也没送，罢工！\n\n"

    #结果输出
    with open('OutPut.txt', 'w', encoding='utf-8') as f:
        f.write(OutPut)

#点位距离数据函数
def DateB():
    print("DateB()运行……")
    global INF
    global A1
    global A2
    global S

    A1 = [[INF, 200, 208, 137, 60, 133, 351, 672, 662, 651, 541],
    [200, INF, 170, 40, 170, 220, 380, 711, 685, 751, 579],
    [208, 170, INF, 150, 60, 250, 500, 874, 809, 871, 703],
    [137, 40, 150, INF, 140, 200, 376, 686, 624, 696, 519],
    [60, 170, 60, 140, INF, 230, 490, 780, 716, 777, 611],
    [133, 220, 250, 200, 230, INF, 320, 561, 459, 557, 389],
    [351, 380, 500, 376, 490, 320, INF, 316, 265, 324, 158],
    [672, 711, 874, 686, 780, 561, 316, INF, 450, 540, 460],
    [662, 685, 809, 624, 716, 459, 265, 450, INF, 210, 250],
    [651, 751, 871, 696, 777, 557, 324, 540, 210, INF, 160],
    [541, 579, 703, 519, 611, 389, 158, 460, 250, 260, INF]]

    A2 = [[INF, 152, 152, 245, 245, 594, 642, 594, 642],
    [152, INF, 60, 100, 160, 435, 527, 435, 527],
    [152, 60, INF, 160, 100, 435, 527, 435, 527],
    [245, 100, 160, INF, 170, 526, 512, 526, 512],
    [245, 160, 100, 170, INF, 526, 512, 526, 512],
    [594, 435, 435, 526, 526, INF, 60, 100, 160],
    [642, 435, 527, 512, 512, INF, 160, 100, 170],
    [594, 526, 435, 526, 526, 100, 160, INF, 170],
    [642, 526, 527, 512, 512, 160, 100, 170, INF]]

    S=[[INF,0,318],
       [0,INF,318],
       [318,318,INF]]

#两点距离计算函数
def Distance(point1, point2):
    global points
    global A1
    global A2
    global S
    global Start_city

    point1=int(point1[0])
    point2=int(point2[0])

    if Start_city == "A1":
        arr=A1[point1][point2]
    if Start_city == "A2":
        arr=A2[point1][point2]
    if Start_city == "S":
        arr=S[point1][point2]

    return (int(arr))

#蚁群算法主函数
def AntColony():
    print("AntColony()运行……")
    global points
    global best_path
    global best_length
    global Start_city

    alpha = 1      #信息素重要程度因子
    beta = 2       #启发式因子
    rho = 0.5      #信息素挥发因子
    Q = 100        #每只蚂蚁携带信息素总量
    num_ants = 32  #蚂蚁数量
    num_iterations = 190 #迭代次数

    # 初始化信息素矩阵
    pheromone = np.ones((len(points), len(points)))

    # 迭代优化
    for iter in range(num_iterations):
        paths = []
        path_lengths = []

        for ant in range(num_ants):
            #初始化
            current_city = Start_city
            visited_cities = set()
            visited_cities.add(current_city)
            path = [current_city]
            path_length = 0
        
            #探索下一个城市
            while len(visited_cities) < len(points):
                #计算当前城市到其他未访问城市的信息素和启发值
                unvisited_cities = list(set(points.keys()) - visited_cities)
                pheromone_vals = [pheromone[list(points.keys()).index(current_city)][list(points.keys()).index(city)] for city in unvisited_cities]
                heuristic_vals = [1 / Distance(points[current_city], points[city]) for city in unvisited_cities]
                probabilities = np.array(pheromone_vals)**alpha * np.array(heuristic_vals)**beta
                probabilities /= sum(probabilities)

                #选择下一个城市
                next_city = np.random.choice(unvisited_cities, p=probabilities)
                #将这个城市加入已访问集合中
                visited_cities.add(next_city)
                #更新路径和长度
                path.append(next_city)
                path_length += Distance(points[current_city], points[next_city])
                #更新当前城市
                current_city = next_city

            #回到起点
            path.append(Start_city)
            path_length += Distance(points[current_city], points[Start_city])

            #将路径和长度保存
            paths.append(path)
            path_lengths.append(path_length)

        #更新信息素矩阵
        delta_pheromone = np.zeros((len(points), len(points)))
        for i in range(num_ants):
            for j in range(len(paths[i])-1):
                start_city_index = list(points.keys()).index(paths[i][j])
                end_city_index = list(points.keys()).index(paths[i][j+1])
                delta_pheromone[start_city_index][end_city_index] += Q/path_lengths[i]
        pheromone = (1-rho)*pheromone + delta_pheromone

    #输出最佳路径和长度
    best_path = paths[np.argmin(path_lengths)]
    best_length = min(path_lengths)

#送餐任务诚朴园A2分配函数
def MA2():
    print("MA2()运行……")
    global Inmeal
    global points
    global Start_city
    global best_path
    global best_length
    global OutPut
    
    #参数准备
    car=[{'car_0'},{},{},{},{},{},{},{},{},{},{}]
    A2=Inmeal
    i=1
    meals=0

    #送餐上车
    while True:
        if (A2['P1'] !=0):
            #小车装路径，装货
            car[i]["P1"]=[1]
            meals=meals + A2['P1']
            A2['P1']=0
            #判断小车超载
            if (meals>=30):
                A2['P1'] = (meals-30)
                i=i+1
                meals=0
                continue
        if (A2['P2'] !=0):
            car[i]["P2"]=[2]
            meals=meals + A2['P2']
            A2['P2']=0
            if (meals>=30):
                A2['P2'] = (meals-30)
                i=i+1
                meals=0
                continue
        if (A2['P3'] !=0):
            car[i]["P3"]=[3]
            meals=meals + A2['P3']
            A2['P3']=0
            if (meals>=30):
                A2['P3'] = (meals-30)
                i=i+1
                meals=0
                continue
        if (A2['P4'] !=0):
            car[i]["P4"]=[4]
            meals=meals + A2['P4']
            A2['P4']=0
            if (meals>=30):
                A2['P4'] = (meals-30)
                i=i+1
                meals=0
                continue
        if (A2['C1'] !=0):
            car[i]["C1"]=[5]
            meals=meals + A2['C1']
            A2['C1']=0
            if (meals>=30):
                A2['C1'] = (meals-30)
                i=i+1
                meals=0
                continue
        if (A2['C2'] !=0):
            car[i]["C2"]=[6]
            meals=meals + A2['C2']
            A2['C2']=0
            if (meals>=30):
                A2['C2'] = (meals-30)
                i=i+1
                meals=0
                continue
        if (A2['C3'] !=0):
            car[i]["C3"]=[7]
            meals=meals + A2['C3']
            A2['C3']=0
            if (meals>=30):
                A2['C3'] = (meals-30)
                i=i+1
                meals=0
                continue
        if (A2['C4'] !=0):
            car[i]["C4"]=[8]
            meals=meals + A2['C4']
            A2['C4']=0
            if (meals>=30):
                A2['C4'] = (meals-30)
                i=i+1
                meals=0
                continue
        all_meals=sum(A2.values())
        if ((all_meals<=0)or(i>=11)):
            break

    #小车路径
    Start_city="A2"
    i=1
    while (i<=10):
        if (car[i]):
            points={}
            points=car[i]
            points["A2"]=[0]
            Start_city='A2'
            AntColony()
            #添加附加路径
            best_path.insert(0,'S')
            best_path.append('S')
            Start_city="S"
            best_length=best_length + ( 2 * Distance([0],[2]))
            OutPut += "诚朴+崇实园小车%d已规划完毕，其最优路径如下：\n"%i
            OutPut += "     " + str(best_path) +"\n"
            OutPut += "     本小车最短距离：%d米\n"%best_length
        #数据初始化
        points={}
        best_length=0
        best_path.clear()
        Start_city=''
        i=i+1

#送餐任务启智园A1分配函数
def MA1():
    print("MA1()运行……")
    global Inmeal
    global points
    global Start_city
    global best_path
    global best_length
    global OutPut
    
    #参数准备
    car=[{'car_0'},{},{},{},{},{},{},{},{},{},{}]
    A1=Inmeal
    i=1
    meals=0

    #送餐上车
    while True:
        if (A1['Q1'] !=0):
            #小车装路径，装货
            car[i]["Q1"]=[1]
            meals=meals + A1['Q1']
            A1['Q1']=0
            #判断小车超载
            if (meals>=30):
                A1['Q1'] = (meals-30)
                i=i+1
                meals=0
                continue
        if (A1['Q2'] !=0):
            car[i]["Q2"]=[2]
            meals=meals + A1['Q2']
            A1['Q2']=0
            if (meals>=30):
                A1['Q2'] = (meals-30)
                i=i+1
                meals=0
                continue
        if (A1['Q3'] !=0):
            car[i]["Q3"]=[3]
            meals=meals + A1['Q3']
            A1['Q3']=0
            if (meals>=30):
                A1['Q3'] = (meals-30)
                i=i+1
                meals=0
                continue
        if (A1['Q4'] !=0):
            car[i]["Q4"]=[4]
            meals=meals + A1['Q4']
            A1['Q4']=0
            if (meals>=30):
                A1['Q4'] = (meals-30)
                i=i+1
                meals=0
                continue
        if (A1['Q5'] !=0):
            car[i]["Q5"]=[5]
            meals=meals + A1['Q5']
            A1['Q5']=0
            if (meals>=30):
                A1['Q5'] = (meals-30)
                i=i+1
                meals=0
                continue
        if (A1['Q6'] !=0):
            car[i]["Q6"]=[6]
            meals=meals + A1['Q6']
            A1['Q6']=0
            if (meals>=30):
                A1['Q6'] = (meals-30)
                i=i+1
                meals=0
                continue
        if (A1['L1'] !=0):
            car[i]["L1"]=[7]
            meals=meals + A1['L1']
            A1['L1']=0
            if (meals>=30):
                A1['L1'] = (meals-30)
                i=i+1
                meals=0
                continue
        if (A1['L2'] !=0):
            car[i]["L2"]=[8]
            meals=meals + A1['L2']
            A1['L2']=0
            if (meals>=30):
                A1['L2'] = (meals-30)
                i=i+1
                meals=0
                continue
        if (A1['L3'] !=0):
            car[i]["L3"]=[9]
            meals=meals + A1['L3']
            A1['L3']=0
            if (meals>=30):
                A1['L3'] = (meals-30)
                i=i+1
                meals=0
                continue
        if (A1['L4'] !=0):
            car[i]["L4"]=[10]
            meals=meals + A1['L4']
            A1['L4']=0
            if (meals>=30):
                A1['L4'] = (meals-30)
                i=i+1
                meals=0
                continue
        all_meals=sum(A1.values())
        if ((all_meals<=0)or(i>=11)):
            break

    #小车路径
    Start_city="A1"
    i=1
    while (i<=10):
        if (car[i]):
            points={}
            points=car[i]
            points["A1"]=[0]
            Start_city='A1'
            AntColony()
            #添加附加路径
            best_path.insert(0,'S')
            best_path.append('S')
            Start_city="S"
            best_length=best_length + ( 2 * Distance([0],[1]))
            OutPut += "启智+理科群小车%d已规划完毕，其最优路径如下：\n"%i
            OutPut += "     " + str(best_path) + "\n"
            OutPut += "     本小车最短距离：%d米\n"%best_length
        #数据初始化
        points={}
        best_length=0
        best_path.clear()
        Start_city=''
        i=i+1

#启动主程序
if __name__=="__main__":
    Start()