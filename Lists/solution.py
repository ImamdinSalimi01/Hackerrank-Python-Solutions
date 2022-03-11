if __name__ == '__main__':
    N = int(input())
    Output = []
    for i in range(0,N):
        command = input().split();
        if command[0] == "print":
            print(Output)
        elif command[0] == "insert":
            Output.insert(int(command[1]),int(command[2]))
        elif command[0] == "remove":
            Output.remove(int(command[1]))
        elif command[0] == "pop":
            Output.pop();
        elif command[0] == "append":
            Output.append(int(command[1]))
        elif command[0] == "sort":
            Output.sort()
        else:
            Output.reverse()