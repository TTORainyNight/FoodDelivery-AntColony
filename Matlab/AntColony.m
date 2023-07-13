%蚁群算法主函数
function AntColony()
    global points;
    global Start_City;
    global A1;
    global A3;
    global A4;
    global best_path;
    global best_length;

    %数据输入
    disp('单次蚁群算法已启动，正在规划小车路径…………');
    if Start_City == 'A1'
        Distance = A1;
    elseif Start_City == 'A3'
        Distance = A3;
    elseif Start_City == 'A4'
        Distance = A4;
    else
        disp('不正确的定位点位，不能获取到正确的点位距离');
    end

    %蚁群参数
    num_ants = 100; %蚂蚁数量
    num_iterations = 200; %迭代次数
    alphan = 1;
    beta = 2;
    rho = 0.5;
    Q = 1;
    paths = cell(1, 0);
    path_lengths = [];
    points = struct2array(points);
    pheromone = ones(length(points));
    
    %迭代优化
    for iter = 1 : num_iterations
        %初始化
        paths = [];
        path_lengths = [];
        for ant = 1 : num_ants
            current_city = points(1);
            visited_cities = [];
            visited_cities = [visited_cities, current_city];
            path = [];
            path = [path , current_city];
            path_length = 0;
            %探索下一个城市
            while length(visited_cities) < length(points)
                unvisited_cities = setdiff(points, visited_cities);
                pheromone_vals = [];
                heuristic_vals = [];
                for i = 1:length(unvisited_cities)
                    current_city_index = find(points == current_city);
                    city_index = find(points == unvisited_cities(i));
                    pheromone_val = pheromone(current_city_index, city_index);
                    pheromone_vals = [pheromone_vals, pheromone_val];
                end

                %计算未访问启发式值
                for i = 1:length(unvisited_cities)
                    city = unvisited_cities(i);
                    distance = Distance(current_city, city);
                    heuristic_val = 1 / distance;
                    heuristic_vals = [heuristic_vals, heuristic_val];
                end
                pheromone_vals = double(pheromone_vals);
                heuristic_vals = double(heuristic_vals);
                
                %处理并储存结果
                probabilities = pheromone_vals.^alphan .* heuristic_vals.^beta;
                prob_sum = sum(probabilities);
                probabilities = probabilities / prob_sum;
                next_city = roulette_wheel_selection(probabilities, unvisited_cities);
                visited_cities = [visited_cities , next_city];
                path = [path , next_city];
                path_length = path_length + Distance(current_city , next_city);
                current_city = next_city;
            end

            %返回起点，保存全局
            path = [path , 1];
            path_length = path_length + Distance(current_city , 1);
            paths{end+1} = path;
            path_lengths = [path_lengths , path_length];
        end
        %信息素增量矩阵更新
        delta_pheromone = zeros(length(points));
        for i = 1:num_ants
            for j = 1:length(paths{i})-1
                start_city_index = find(points == paths{i}(j), 1);
                next_city_index = find(points == paths{i}(j+1), 1); 
                delta_pheromone(start_city_index, next_city_index) = delta_pheromone(start_city_index, next_city_index) + Q/path_lengths(i); % 更新信息素增量矩阵
            end
        end
        pheromone = (1-rho)*pheromone + delta_pheromone;
    end
    
    %输出接口
    [max_length, index] = max(path_lengths);
    best_path = paths{index};
    best_length = max_length;

end