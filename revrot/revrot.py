'''DESCRIPTION:
The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of
the initial string) of size sz (ignore the last chunk if its size is less than sz).

If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2,
reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks
and return the result as a string.

If

sz is <= 0 or if str is empty return ""
sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".'''


def revrot(data, sz):
    sects = []
    new_sects = []
    output = ''
    n = 0

    if sz <= 0 or sz > len(data):
        return ''

    while n < len(data):
        sects.append(data[n:n + sz])
        n += sz


    for chunk in sects:
        # determine if sum of each digit cubed is divisible by 2
        cubed_total = 0

        if len(chunk) == sz:
            for i in chunk:
                cubed_total += int(i)**3

            if cubed_total % 2 == 0:
                # reverse chunk
                reversed_chunk = reverse(chunk)
                new_sects.append(reversed_chunk)
            else:
                # rotate left by one position
                rotated_chunk = rotate(chunk)
                new_sects.append(rotated_chunk)

    for section in new_sects:

        output += section
    return output

def reverse(chunk):
    backward = ''

    for digit in chunk:
        backward = digit + backward

        if len(backward) == len(chunk):
            return backward


def rotate(chunk):
    rotate_sect = chunk[1:] + chunk[0]

    return rotate_sect


print(revrot("123456", 3))
print(revrot("123456", 5))
print(revrot("123456", 0))
print(revrot("", 3))
# reverse('1234')
# rotate('1234')
# --> "234561876549"
