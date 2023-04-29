def dutch_flag_sort(balls):
    start = 0
    end = len(balls)-1

    while balls[start] =="R" and start < end:
        start += 1
    while balls[end] == "B" and start < end:
        end -= 1
    ## now the bounds of the problem begin at start and end at end inclusively.
    i = start
    while i <= end:
        if balls[i] == "R" and start <= i:
            balls[i], balls[start] = balls[start], balls[i]
            start += 1
        elif balls[i] == "B" and i <= end:
            balls[i], balls[end] = balls[end], balls[i]
            end -=1
        else:
            i += 1
    return balls