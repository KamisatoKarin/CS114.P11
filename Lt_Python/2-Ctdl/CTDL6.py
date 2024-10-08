def is_valid(segment):
    return len(segment) == 1 or (segment[0] != '0' and int(segment) <= 255)

def restore_ip_addresses(s):
    def backtrack(start=0, path=[]):
        if len(path) == 4 and start == len(s):
            result.append('.'.join(path))
            return
        if len(path) == 4:
            return
        for end in range(start + 1, min(start + 4, len(s) + 1)):
            segment = s[start:end]
            if is_valid(segment):
                backtrack(end, path + [segment])
    result = []
    backtrack()
    return result

s = input().strip()
valid_ips = restore_ip_addresses(s)
for ip in valid_ips:
    print(ip)