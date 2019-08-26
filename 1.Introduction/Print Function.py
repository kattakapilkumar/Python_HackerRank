>>>print(range(1,n))
range(1,5)

>>>print(*range(1,n))
1 2 3 4
>>>print(*range(1,n),sep='')
1234

'''
Check Tutorial tab to know how to to solve.

Read an integer .

Without using any string methods, try to print the following:


Note that "" represents the values in between.

Input Format

The first line contains an integer .

Output Format

Output the answer as explained in the task.

Sample Input 0

3
Sample Output 0

123

'''


if __name__ == '__main__':
    n = int(input())

    print(*range(1,n+1),sep='') 