from Lab_7.utils import read_f, write_f


def get_lis(arr):
    n = len(arr)

    # Initialize dp array with 1
    dp = [1] * n

    # Initialize seq array with index values (to store previous indices in LIS)
    seq = list(range(n))

    # Compute dp and seq arrays
    for i in range(n):
        for prev in range(i):
            if arr[prev] < arr[i] and 1 + dp[prev] > dp[i]:
                dp[i] = 1 + dp[prev]
                seq[i] = prev

    # Find the index of the last element in the LIS
    ans = -1
    ans_ind = -1
    for i in range(n):
        if dp[i] > ans:
            ans = dp[i]
            ans_ind = i

    # Construct the result sequence using seq array
    res = []
    res.append(arr[ans_ind])
    while seq[ans_ind] != ans_ind:
        ans_ind = seq[ans_ind]
        res.append(arr[ans_ind])

    # Reverse the result to get the correct order
    res.reverse()
    return res


if __name__ == "__main__":
    n, data = read_f(6)
    seq = list(map(int, data.split()))
    res = get_lis(seq)
    ans_len = len(res)
    write_f(6, *[ans_len, res])
