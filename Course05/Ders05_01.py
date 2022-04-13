def genereate_seed(seed):
    i = seed.count('[')
    if i == 0: return [seed]
    last_pos = 0
    temp_list = [seed]
    for j in range(i):
        list_seeds = []
        for the_temp in temp_list:
            start_p, end_p = the_temp.find('['), the_temp.find(']')
            if start_p != -1 and end_p != -1:
                start_seed, end_seed = the_temp[:start_p], the_temp[end_p + 1:]
                params = the_temp[start_p + 1:end_p]
                params_list = params.split(',')
                for theparam in params_list:
                    list_seeds.append(start_seed + theparam + end_seed)  
            else:
                return [seed]
        temp_list = list_seeds
    return temp_list

print(genereate_seed('[com,net].[uk,tr].[1,2,3]'))