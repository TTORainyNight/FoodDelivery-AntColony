%全局变量
global Inmeal; Inmeal = struct();  %送餐信息输入

global A1;A1 = [];
global A3;A3 = [];
global A4;A4 = [];
global S;S = [];  %点位距离矩阵

global points;points = struct(); %蚁群算法输入
global best_path;best_path = [];
global best_length;best_length = inf;%蚁群算法输出

global Start_City;Start_City = '';%点位定位

Start();%启动程序