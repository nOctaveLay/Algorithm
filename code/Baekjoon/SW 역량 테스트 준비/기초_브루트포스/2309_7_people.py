tall_list = [int(input()) for _ in range(9)]
list_sum = 0
sorted_list = []
for i in range(9):
    list_sum += tall_list[i]
    for j in range(i+1,9):
        list_sum += tall_list[j]
        for k in range(j+1,9):
            list_sum += tall_list[k]
            for q in range(k+1,9):
                list_sum += tall_list[q]
                for w in range(q+1,9):
                    list_sum += tall_list[w]
                    for e in range(w+1,9):
                        list_sum += tall_list[e]
                        for r in range(e+1,9):
                            list_sum += tall_list[r]
                            if list_sum == 100:
                                sorted_list.append(tall_list[i])
                                sorted_list.append(tall_list[j])
                                sorted_list.append(tall_list[k])
                                sorted_list.append(tall_list[q])
                                sorted_list.append(tall_list[w])
                                sorted_list.append(tall_list[e])
                                sorted_list.append(tall_list[r])
                                break
                            list_sum -= tall_list[r]
                        list_sum -= tall_list[e]
                    list_sum -= tall_list[w]
                list_sum -= tall_list[q]
            list_sum -= tall_list[k]
        list_sum -= tall_list[j]
    list_sum -= tall_list[i]
    
    
sorted_list = sorted(sorted_list)
for x in sorted_list:
    print(x)