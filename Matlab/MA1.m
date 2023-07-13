function MA1()
    global Inmeal
    global points
    global Start_City
    global best_path
    global best_length
    global S
    
    %初始化
    car(1).A1=1;
    car(2).A1=1;
    car(3).A1=1;
    car(4).A1=1;
    car(5).A1=1;
    i=1;
    meals=0;

    %送餐上车
    Ready = Inmeal;
    while true
        %检测Q1有没有送餐需求
        Value=Ready.Q1;
        if (Value ~=0)
            %小车装路径，装货
            car(i).Q1 = 2;
            meals=meals + Value;
            Ready.Q1 = 0;
            %判断小车超载
            if (meals>=30)
                Ready.Q1 = meals - 30;
                i=i+1;
                meals=0;
                continue;
            end
        end

        Value=Ready.Q2;
        if (Value ~=0)
            car(i).Q2 = 3;
            meals=meals + Value;
            Ready.Q2 = 0;
            if (meals>=30)
                Ready.Q2 = meals - 30;
                i=i+1;
                meals=0;
                continue;
            end
        end

        Value=Ready.Q3;
        if (Value ~=0)
            car(i).Q3 = 4;
            meals=meals + Value;
            Ready.Q3 = 0;
            if (meals>=30)
                Ready.Q3 = meals - 30;
                i=i+1;
                meals=0;
                continue;
            end
        end

        Value=Ready.Q4;
        if (Value ~=0)
            car(i).Q4 = 5;
            meals=meals + Value;
            Ready.Q4 = 0;
            if (meals>=30)
                Ready.Q4 = meals - 30;
                i=i+1;
                meals=0;
                continue;
            end
        end

        Value=Ready.Q5;
        if (Value ~=0)
            car(i).Q5 = 6;
            meals=meals + Value;
            Ready.Q5 = 0;
            if (meals>=30)
                Ready.Q5 = meals - 30;
                i=i+1;
                meals=0;
                continue;
            end
        end

        Value=Ready.Q6;
        if (Value ~=0)
            car(i).Q6 = 7;
            meals=meals + Value;
            Ready.Q6 = 0;
            if (meals>=30)
                Ready.Q6 = meals - 30;
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
    Start_City = "A1";
    i = 1;
    Value = 0;
    while (i<=5)
        fields = fieldnames(car(i));
        nonEmptyFields = fields(~cellfun(@isempty, struct2cell(car(i))));
        Value = numel(nonEmptyFields);
        if Value > 1
            points={};
            points=(car(i));
            Start_City = 'A1';
            AntColony();
            best_path = [0, best_path];
            best_path = [best_path, 0];
            letter_mapping = {'S', 'A1', 'Q1', 'Q2', 'Q3', 'Q4','Q5','Q6'};
            best_path = letter_mapping(best_path + 1);
            Start_city="S";
            best_length=best_length + 2*S(1,2);
            disp(['     启智园小车', num2str(i), '已规划完毕，其最优路径如下：']);
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