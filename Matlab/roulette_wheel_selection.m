%轮盘赌选择算法函数
function next_city = roulette_wheel_selection(probabilities, unvisited_cities)
    r = rand();
    c = cumsum(probabilities);
    selected_index = find(r <= c, 1, 'first');
    next_city = unvisited_cities(selected_index);
end