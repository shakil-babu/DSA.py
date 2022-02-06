# def insertionSort(arr):
#     for i in range(1, len(arr)):
#         item = arr[i]

#         j = i - 1
#         while j >= 0 and arr[j] > item:
#             arr[j+1] = arr[j]
#             j = j - 1
#         arr[j+1] = item
#     return arr


def insertionSort(arr):
    # i এর মান 1 থেকে len(arr) এর আগ পর্যন্ত 1 করে বাড়াই
    for i in range(1, len(arr)):
        # arr[i] কে currentValue রে এসাইন করি
        currentValue = arr[i]

        # currentValue এর জন্য উপযুক্ত স্থান খুঁজে বের করি
        j = i - 1

        # যদি j, 0 থেকে সমান বা বড় হয় এবং  arr[j] থেকে currentValue ছোট হয়
        while j >= 0 and arr[j] > currentValue:

            # arr[j] কে তার পরের ঘরে রেখে দিই
            arr[j+1] = arr[j]

            # j এর মান 1 করে কমাই
            j -= 1

        # এখন খালি জায়গায় currentValue কে বসাই
        arr[j+1] = currentValue

    return arr


ans = insertionSort([500, 200, 100, 400])
print(ans)
