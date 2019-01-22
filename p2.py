def product_list(lst):
    product = 1
    for num in lst:
        product *= num
    for i in range(len(lst)):
        lst[i] = product / lst[i]
    return lst


lst = [1, 2, 3, 4, 5]
print(product_list(lst))

lst = [3, 2, 1]
print(product_list(lst))


def product_list_without_div_naive(lst):
    ans = [1] * len(lst)
    for i in range(len(ans)):
        for j in range(len(lst)):
            ans[i] *= lst[j] if i != j else 1
    return ans


lst = [1, 2, 3, 4, 5]
print(product_list_without_div_naive(lst))

lst = [3, 2, 1]
print(product_list_without_div_naive(lst))


# Another Sol: could convert numbers to base at index and drop the last digit


# rotate the array
def product_list_with_rotation(lst):
    ans = [1] * len(lst)
    for _ in range(len(lst) - 1):
        lst = lst[-1:] + lst[:-1]
        ans = [a * b for a, b in zip(ans, lst)]
    return ans


lst = [1, 2, 3, 4, 5]
print(product_list_with_rotation(lst))

lst = [3, 2, 1]
print(product_list_with_rotation(lst))


def product_list_optimal(lst):
    pre_products = [1] * len(lst)
    suf_products = [1] * len(lst)

    running_product = 1
    for i in range(len(lst)):
        pre_products[i] = running_product
        running_product *= lst[i]

    running_product = 1
    for i in reversed(range(len(lst))):
        suf_products[i] = running_product
        running_product *= lst[i]
    
    return [a * b for a, b in zip(pre_products, suf_products)]
    

lst = [1, 2, 3, 4, 5]
print(product_list_optimal(lst))

lst = [3, 2, 1]
print(product_list_optimal(lst))

def product_list_optimal_golf(lst):
    pre_products = [1] * len(lst)
    suf_products = [1] * len(lst)

    for i in range(1, len(lst)):
        pre_products[i] = pre_products[i - 1] * lst[i - 1]

    for i in reversed(range(len(lst) - 1)):
        suf_products[i] = suf_products[i + 1] * lst[i + 1]
    
    return [a * b for a, b in zip(pre_products, suf_products)]
    

lst = [1, 2, 3, 4, 5]
print(product_list_optimal(lst))

lst = [3, 2, 1]
print(product_list_optimal(lst))