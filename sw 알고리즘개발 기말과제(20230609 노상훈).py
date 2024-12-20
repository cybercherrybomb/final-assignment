import random

# 학생 정보 생성
def generate_students(num_students=30):
    students = []
    for _ in range(num_students):
        name = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2))
        age = random.randint(18, 22)
        score = random.randint(0, 100)
        students.append({"이름": name, "나이": age, "성적": score})
    return students

# 학생 정보를 파일에 저장
def save_students_to_file(filename, students):
    with open(filename, 'w', encoding='utf-8') as file:
        for student in students:
            file.write(f"{student}\n")

# 선택 정렬
def selection_sort(A, key, reverse=False):
    n = len(A)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if (A[j][key] < A[least][key]) if not reverse else (A[j][key] > A[least][key]):
                least = j
        A[i], A[least] = A[least], A[i]

        print(f"Step {i+1:2d} =", [{d[key] for d in A}])

# 삽입 정렬
def insertion_sort(A, key, reverse=False):
    n = len(A)
    for i in range(1, n, 1):
        key_item = A[i]
        j = i - 1
        while j >= 0 and ((A[j][key] > key_item[key]) if not reverse else (A[j][key] < key_item[key])):
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key_item
        print(f"Step {i+1:2d} =", [{d[key] for d in A}])

# 퀵 정렬
def quick_sort(A, left, right, key, reverse=False):
    global step

    if left < right:
        print(f"\nStep {step}: Sorting range A[{left}:{right+1}] -> {[d[key] for d in A[left:right + 1]]}")
        step += 1

        pivot = median_of_three(A, left, right, key, reverse)
        q = partition(A, left, right, pivot, key, reverse)  # 좌우로 분할
        print(f"Partitioned at index {q}, pivot placed at A[{q}] -> {A[q][key]}")
        print("Current list:", [{d[key] for d in A}])

        quick_sort(A, left, q - 1, key, reverse)  # 왼쪽 부분리스트를 퀵 정렬
        quick_sort(A, q + 1, right, key, reverse)  # 오른쪽 부분리스트를 퀵 정렬

def median_of_three(A, left, right, key, reverse):
    mid = (left + right) // 2
    values = [(A[left][key], left), (A[mid][key], mid), (A[right][key], right)]
    values.sort(reverse=reverse)
    return values[1][1]  # 중앙값의 인덱스 반환

def partition(A, left, right, pivot_index, key, reverse):
    pivot_value = A[pivot_index][key]
    A[pivot_index], A[right] = A[right], A[pivot_index]
    store_index = left

    for i in range(left, right):
        if (A[i][key] < pivot_value) if not reverse else (A[i][key] > pivot_value):
            A[i], A[store_index] = A[store_index], A[i]
            store_index += 1

    A[store_index], A[right] = A[right], A[store_index]
    return store_index

# 계수 정렬
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    # 빈도 계산
    for num in arr:
        count[num] += 1

    # 누적합 계산
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    output = [0] * len(arr)
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    return output

# 기수 정렬 (계수 정렬 활용)
def radix_sort(A):
    if not A or "성적" not in A[0]:
        print("기수 정렬은 성적을 기준으로만 사용할 수 있습니다.")
        return

    max_val = max(student["성적"] for student in A)
    factor = 1

    while max_val // factor > 0:
        # 각 자릿수 기준으로 계수 정렬 수행
        buckets = [[] for _ in range(10)]
        for student in A:
            digit = (student["성적"] // factor) % 10
            buckets[digit].append(student)

        A[:] = [student for bucket in buckets for student in bucket]
        factor *= 10

        print(f"Sorted by digit {factor // 10}: {A}")
    
# 정렬된 학생 정보를 보기 좋게 출력
def print_students(students):
    print("\n[정렬된 학생 목록]")
    print(f"{'이름':<10}{'나이':<10}{'성적':<10}")
    print("-" * 30)
    for student in students:
        print(f"{student['이름']:<10}{student['나이']:<10}{student['성적']:<10}")


# 사용자 인터페이스
def main():
    global step
    input_filename = 'C:\\Users\\User\\Desktop\\새 폴더\\students.txt'
    output_filename = 'C:\\Users\\User\\Desktop\\새 폴더\\sorted_students.txt'

    students = generate_students()
    save_students_to_file(input_filename, students)
    print("학생 정보가 생성되어 파일에 저장되었습니다:", input_filename)

    print("초기 학생 목록:")
    for student in students:
        print(student)

    while True:
        print("\n메뉴:")
        print("1. 이름을 기준으로 정렬")
        print("2. 나이를 기준으로 정렬")
        print("3. 성적을 기준으로 정렬")
        print("4. 프로그램 종료")
        choice = input("메뉴를 선택하세요: ")

        if choice == "4":
            print("프로그램을 종료합니다.")
            break

        key = "이름" if choice == "1" else "나이" if choice == "2" else "성적"
        reverse = input("오름차순(0) 또는 내림차순(1)을 선택하세요: ") == "1"

        print("\n정렬 알고리즘:")
        print("1. 선택 정렬")
        print("2. 삽입 정렬")
        print("3. 퀵 정렬")
        print("4. 기수 정렬 (성적 기준만)")
        algo_choice = input("알고리즘을 선택하세요: ")
        # 정렬 알고리즘
        if algo_choice == "1":
            selection_sort(students, key, reverse)
        elif algo_choice == "2":
            insertion_sort(students, key, reverse)
        elif algo_choice == "3":
            step = 1
            quick_sort(students, 0, len(students) - 1, key, reverse)
        elif algo_choice == "4" and key == "성적":
            radix_sort(students)
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")
            continue

        # 정렬된 학생 목록 출력
        print_students(students)

        save_students_to_file(output_filename, students)
        print("정렬된 학생 정보가 파일에 저장되었습니다:", output_filename)

if __name__ == "__main__":
    main()
