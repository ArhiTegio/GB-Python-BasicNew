def ZipTwoList(arr1, arr2):
    min_len = min(len(arr1), len(arr2))
    return list(zip(arr1[:min_len], arr2[:min_len]))