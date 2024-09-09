def majority_element_naive(elements):
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0

def majority_element(a, l, r):
    # Trường hợp cơ bản: nếu chỉ có một phần tử, nó là phần tử chiếm đa số
    if l == r - 1:
        return a[l]
    
    # Chia dãy số thành hai nửa
    m = (l+r)//2
    left_majority = majority_element(a,l,m)
    right_majority = majority_element(a,m,r)

    # Nếu hai nửa có cùng phần tử chiếm đa số, trả về nó
    c1, c2 = 0, 0
    for i in a[l:r]:
        if i == left_majority:
            c1 += 1
        elif i == right_majority:
            c2 += 1
    
    if c1 > (r - l)//2 and left_majority != -1:
        return left_majority
    elif c2 > (r - l)//2 and right_majority != -1:
        return right_majority
    else:
        return -1



if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(int(majority_element(input_elements, 0, input_n) != -1))