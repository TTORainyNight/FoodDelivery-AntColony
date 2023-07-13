function MA4()
    global Inmeal
    global points
    global Start_City
    global best_path
    global best_length
    global S
    
    %初始化
    car(1).A4=1;
    car(2).A4=1;
    car(3).A4=1;
    car(4).A4=1;
    car(5).A4=1;
    i=1;
    meals=0;

    %送餐上车
    Ready = Inmeal;
    while true
        %检测L1有没有送餐需求
        Value=Ready.L1;
        if (Value ~=0)
            %小车装路径，装货
            car(i).L1 = 2;
            meals=meals + Value;
            Ready.L1 = 0;
            %判断小车超载
            if (meals>=30)
                Ready.L1 = meals - 30;
                i=i+1;
                meals=0;
                continue;
            end
        end

        Value=Ready.L2;
        if (Value ~=0)
            car(i).L2 = 3;
            meals=meals + Value;
            Ready.L2 = 0;
            if (meals>=30)
                Ready.L2 = meals - 30;
                i=i+1;
                meals=0;
                continue;
            end
        end

        Value=Ready.L3;
        if (Value ~=0)
            car(i).L3 = 4;
            meals=meals + Value;
            Ready.L3 = 0;
            if (meals>=30)
                Ready.L3 = meals - 30;
                i=i+1;
                meals=0;
                continue;
            end
        end

        Value=Ready.L4;
        if (Value ~=0)
            car(i).L4 = 5;
            meals=meals + Value;
            Ready.L4 = 0;
            if (meals>=30)
                Ready.L4 = meals - 30;
                i=i+1;
                meals=0;
                continue;
            end
        end

        all_meals = 0;
        if ~isempty(Ready)
            fields = fieldnames(Ready);
            for i = 1:numel(fields)
                fieldName = fields{i};
                Value = Ready.(fieldName);
                all_meals = all_meals + Value;
            end
        end
        if (all_meals<=0) || (i>=6)
            break;
        end
    end

    %小车路径
    Start_City = "A4";
    i = 1;
    Value = 0;
    while (i<=5)
        fields = fieldnames(car(i));
        nonEmptyFields = fields(~cellfun(@isempty, struct2cell(car(i))));
        Value = numel(nonEmptyFields);
        if Value > 1
            points={};
            points=(car(i));
            Start_City = 'A4';
            AntColony();
            best_path = [0, best_path];
            best_path = [best_path, 0];
            letter_mapping = {'S', 'A4', 'L1', 'L2', 'L3', 'L4'};
            best_path = letter_mapping(best_path + 1);
            Start_city="S";
            best_length=best_length + 2*S(1,4);
            disp(['     理科群小车', num2str(i), '已规划完毕，其最优路径如下：']);
            disp(best_path);
            disp(['     本小车最短距离：', num2str(best_length), '米']);
        end
        %数据初始化
        points =struct();
        best_length = 0;
        best_path = [];
        Start_city = '';
        i = i + 1;
    end
end