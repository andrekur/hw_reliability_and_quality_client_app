import requests
import random
import time

BASE_URL = 'http://gr-team.ru/api/v1/{method}/'


def generate_str(len_s: int) -> str:
    s = ''

    for i in range(0, int(len_s)):

        a = random.randint(
            ord('A'),
            ord('Z')
        )

        b = random.randint(
            ord('a'),
            ord('z')
        )

        if bool(random.randint(0, 1)):
            s += chr(a)
            continue
        s += chr(b)

    return s


def generate_test_file(
        file_name: str,
        count_str: int,
        max_len_str: int) -> None:
    with open(f'{file_name}.txt', 'w') as file:

        for i in range(count_str):
            s = generate_str(random.randint(1, max_len_str))

            file.write(f'{s}\n')


def get_levin_len(s1: str, s2: str, func: str):
    params = {
        's1': s1,
        's2': s2,
        'func': func
    }

    result = requests.get(
        url=BASE_URL.format(method='get_levin_len'),
        params=params
    )

    return result.json()


def test_levin_len(
        file_name1: str,
        file_name2: str,
        func_name: str,
        count_str: int) -> None:
    with open(f'{file_name1}.txt', 'r') as f1, \
            open(f'{file_name2}.txt', 'r') as f2, \
            open('result.json', 'w') as file_w:
        for i in range(1, count_str + 1):
            print(f'request №{i}')
            result = get_levin_len(
                f1.readline(i).strip(),
                f2.readline(i).strip(),
                func_name
            )

            file_w.write(f'{result}\n')


if __name__ == '__main__':
    file_name1 = 'test1'
    file_name2 = 'test2'
    func = 'wiki'
    cout_str = 200
    max_len_str = 1000

    generate_test_file(file_name1, cout_str, max_len_str)
    generate_test_file(file_name2, cout_str, max_len_str)

    start_time = time.time()

    test_levin_len(
        file_name1,
        file_name2,
        func,
        cout_str
    )

    print(f'time: {time.time() - start_time}')
