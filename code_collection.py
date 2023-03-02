print("Hello world")

input = "MyNameisAnthony"


def vowelRemover(houses):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    houses = [x for x in houses if x not in vowels]
    return "".join(houses)


print(vowelRemover(input))


size = 3
page_requests = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0]


def calMiss(page_requests, max_cache_size):
    cur_cache = []
    miss_count = 0
    for x in page_requests:
        if x not in cur_cache:
            if len(cur_cache) == max_cache_size:
                cur_cache.pop(0)
            cur_cache.append(x)
            miss_count += 1
        print(cur_cache, miss_count)
    return miss_count


print(calMiss(page_requests, size))
