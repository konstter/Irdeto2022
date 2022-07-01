import os


def read_files(d):
    result_dict = {}
    q = 0
    for fn in os.listdir("test_algorithm"):
        with open(os.path.join("test_algorithm", fn), 'r') as f:

            for str in f:
                str_list = str.split(",", 1)
                frame_id = int(str_list[0])

                if frame_id in result_dict:
                    result_dict[frame_id] += 1
                else:
                    result_dict[frame_id] = 1
        q += 1
    return result_dict, q


def analyze(d, pc):
    s = read_files(d)
    r_dict, q = s
    r_list = []
    for key in r_dict:
        part = (r_dict[key] / q) * 100
        if part >= pc:
            r_list.append(key)
    return r_list


if __name__ == '__main__':

    dir = "test_algorithm"
    p = 10
    print(analyze(dir, float(p)))
