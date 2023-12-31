def count_item_and_sort(items):
    result = {}
    for element in items:
        if element in result:
            result[element] += 1
        else:
            result[element] = 1
    sorted_elements = sorted(result.items(), key=lambda x: x[1])
    return sorted_elements
    
if __name__ == "__main__":
    print(count_item_and_sort(["js", "js", "golang", "ruby", "ruby", "js", "js"]))
    # "golang->1 ruby->2 js->4"
    print(count_item_and_sort(["A", "B", "B", "C", "A", "A", "B", "A", "D", "D"]))
    # "C->1 D->2 B->3 A->4"
    print(count_item_and_sort(["football", "basketball", "tenis"]))
    # "basketball->1 football->1 tenis->1"