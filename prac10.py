print("D21CE178, Nisarg Shah");

def intersection(A, B, C):
    s1 = set(A)
    s2 = set(B)
    s3 = set(C)
    print("List =", A)
    print("Tuple =", B)
    print("Dictionary =", C)
    set1 = s1.intersection(s2)
    result_set = set1.intersection(s3)
    final_list = list(result_set)

    print("Common of members of list, tuple and dictionary:", final_list)

if __name__== "__main__":
    list1 = [1, 2, "ABC", 3.4]
    tuple1 = (12, 20, "ABC", 3.4)
    dictionary1 = {"ABC", 1, 3.4, "PQR"}
    intersection(list1, tuple1, dictionary1)
