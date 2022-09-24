def solution(commands):
    answer = []
    map = [["" for _ in range(50)] for _ in range(50)]
    merge_list = []

    for i in commands:
        command = i.split(" ")
        if command[0] == "UPDATE":
            if command[1].isdigit():
                x = int(command[1])-1
                y = int(command[2])-1
                if [x,y] in merge_list:
                    for j in merge_list:
                        map[j[0]][j[1]] = command[3]
                map[x][y] = command[3]
            else:
                for j in range(50):
                    for k in range(50):
                        if map[j][k] == command[1]:
                           map[j][k] = command[2]
        elif command[0] == "MERGE":
            r1, c1 = int(command[1])-1, int(command[2])-1
            r2, c2 = int(command[3])-1, int(command[4])-1
            if [r1,c1] not in merge_list:
                merge_list.append([r1,c1])
            if [r2,c2] not in merge_list:
                merge_list.append([r2,c2])
            first = map[r1][c1]
            second = map[r2][c2]

            if (first and second == "") or (first and second):
                map[r2][c2] = map[r1][c1]
            elif second and first == "":
                map[r1][c1] = map[r2][c2]
            print(merge_list)
        elif command[0] == "UNMERGE":
            r, c = int(command[1])-1, int(command[2])-1

            if [r,c] in merge_list:
                merge_list.remove([r,c])

            for i in merge_list:
                map[i[0]][i[1]] = ""
        elif command[0] == "PRINT":
            r, c = int(command[1])-1, int(command[2])-1

            if map[r][c]:
                answer.append(map[r][c])
            else:
                answer.append("EMPTY")


    for i in range(50):
        for j in range(50):
            print(map[i][j], end=' ')
        print()
    return answer


print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon",
                "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle",
                "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))