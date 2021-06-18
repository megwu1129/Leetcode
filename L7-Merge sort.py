    def mergeSort(self, arr, start, end):
        if start >= end:
            return
        mid = (start+end)//2
        # Divide
        self.mergeSort(arr, start, mid)
        self.mergeSort(arr, mid+1, end)

        # Merge
        i = start
        j = mid+1
        temp = []
        while i <= mid and j <= end:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= end:
            temp.append(arr[j])
            j += 1

        arr[start:end+1] = temp
