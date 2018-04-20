from math import floor


def Insert(queue, item):
    queue.append(item)
    pos = len(queue)
    while pos != 1 and item > queue[floor(pos/2) - 1]:
        queue[pos - 1] = queue[floor(pos/2) - 1]
        queue[floor(pos/2) - 1] = item
        pos = floor(pos/2)


def ExtractMax(queue):
    queue[0] = queue[-1]
    queue.pop()
    pos = 1
    while pos < len(queue):
        if pos*2 <= len(queue):
            if pos*2 + 1 <= len(queue):
                if queue[pos - 1] < queue[pos*2 - 1] or queue[pos - 1] < queue[pos*2]:
                    if queue[pos*2 - 1] >= queue[pos*2]:
                        tmp = queue[pos - 1]
                        queue[pos - 1] = queue[pos*2 - 1]
                        queue[pos*2 - 1] = tmp
                        pos = pos*2
                    else:
                        tmp = queue[pos - 1]
                        queue[pos - 1] = queue[pos*2]
                        queue[pos*2] = tmp
                        pos = pos*2 + 1
                else:
                    break    
            else:
                if queue[pos - 1] < queue[pos*2 - 1]:
                    tmp = queue[pos - 1]
                    queue[pos - 1] = queue[pos*2 - 1]
                    queue[pos*2 - 1] = tmp
                    pos = pos*2
                break
        else:
            break            


def main():
    n = int(input())
    queue = []
    output = []
    for i in range(n):
        command = input().split()
        if len(command) == 1:
            output.append(queue[0])
            ExtractMax(queue)
        else:
            Insert(queue, int(command[1]))
    print('\n'.join(str(x) for x in output))


if __name__ == "__main__":
    main()
