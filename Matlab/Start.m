%启动函数
function Start()
    figure('Name', 'Matlab小战队', 'NumberTitle', 'off');
    text(0.5, 0.9, 'Matlab小战队出发！', 'HorizontalAlignment', 'center', 'VerticalAlignment', 'middle', 'FontSize', 20);
    text(0.5, 0.2, '送餐信息输入请在Start()函数中修改。', 'HorizontalAlignment', 'center', 'VerticalAlignment', 'middle', 'FontSize', 14);
    %数据导入
    global Inmeal;
    DateB();

    %送餐输入，每辆送餐小车最多30份，最多5辆小车
    %崇实诚朴园
    Inmeal = struct('C1', 0, 'C2', 0, 'C3',0, 'C4', 0);
    num = sum(struct2array(Inmeal));
    if num == 0
        disp("崇实园和诚朴园没有检测到送餐需求。");
    elseif num <= 150
        MA3();
    else
        disp("每个园区最多送150份，崇实园和诚朴园的车车不够用了，所以一份也没送，罢工！");
    end

    %理科群
    Inmeal = struct('L1', 0, 'L2', 0, 'L3', 0, 'L4', 0);
    num = sum(struct2array(Inmeal));
    if num == 0
        disp("理科群没有检测到送餐需求。");
    elseif num <= 150
        MA4();
    else
        disp("每个园区最多送150份，理科群的车车不够用了，所以一份也没送，罢工！");
    end

    %启智园
    Inmeal = struct('Q1', 20, 'Q2', 15, 'Q3', 35, 'Q4', 5, 'Q5', 16, 'Q6', 21);
    num = sum(struct2array(Inmeal));
    if num == 0
        disp("启智园没有检测到送餐需求。");
    elseif num <= 150
        MA1();
    else
        disp("每个园区最多送150份，启智园的车车不够用了，所以一份也没送，罢工！");
    end
