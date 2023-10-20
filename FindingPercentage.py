# Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    sum = 0.0
    
    for i in range(3):
        sum += student_marks[query_name][i]

    print("%.2f" % (sum/3))