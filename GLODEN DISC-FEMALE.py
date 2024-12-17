import requests
import csv
import time
import os

# 定义 URL
MY1PICK_URL = "https://cdn.fandomchart.com/web/rank/json/1.MO.2.json"
MUBEAT_URL = "https://cdn.fandomchart.com/web/rank/json/1.MB.2.json"
FANDOM_URL = "https://cdn.fandomchart.com/web/rank/json/1.FC.2.EN.json"

# 定义 CSV 文件名
CSV_FILE = 'GLODEN-DISC-female-vote_counts.csv'

# 初始化差值
last_my1pick_votes = {}
last_mubeat_votes = {}
last_fandom_votes = {}

# 标志位，指示是否为第一次检测
first_run = True

def fetch_my1pick_votes():
    try:
        response = requests.get(MY1PICK_URL)
        response.raise_for_status()
        data = response.json()
        vote_counts = {}
        for entry in data['body']['vote_count_list']:
            name = entry['name2']
            vote_counts[name] = int(entry['vote_count'])
        return vote_counts
    except (requests.RequestException, KeyError):
        print("Error fetching My1Pick votes. Returning empty data.")
        return {}

def fetch_mubeat_votes():
    try:
        response = requests.get(MUBEAT_URL)
        response.raise_for_status()
        data = response.json()
        vote_counts = {}
        for entry in data['body']['vote_count_list']:
            name = entry['name']
            vote_counts[name] = entry['count']
        return vote_counts
    except (requests.RequestException, KeyError):
        print("Error fetching Mubeat votes. Returning empty data.")
        return {}

def fetch_fandom_votes():
    try:
        response = requests.get(FANDOM_URL)
        response.raise_for_status()
        data = response.json()
        vote_counts = {}
        for entry in data['body']['candidate']:
            name = entry['subject']
            vote_counts[name] = entry['count']
        return vote_counts
    except (requests.RequestException, KeyError):
        print("Error fetching Fandom votes. Returning empty data.")
        return {}

def calculate_total_votes(my1pick_votes, mubeat_votes, fandom_votes):
    total_votes = {}
    for name in my1pick_votes:
        total_votes[name] = my1pick_votes[name]
        if name in mubeat_votes:
            total_votes[name] += mubeat_votes[name] * 2  # Mubeat 票数乘以 2
        if name in fandom_votes:
            total_votes[name] += fandom_votes[name]
    return total_votes

def write_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Name', 'Total Votes', 'My1Pick Votes', 'Mubeat Votes', 'Fandom Votes', 'Timestamp',
                             'My1Pick Diff', 'Mubeat Diff', 'Fandom Diff', 'Total Diff'])
        writer.writerows(data)

while True:
    my1pick_votes = fetch_my1pick_votes()
    mubeat_votes = fetch_mubeat_votes()
    fandom_votes = fetch_fandom_votes()

    # 检查是否有任何一个 URL 读取失败
    if not my1pick_votes or not mubeat_votes or not fandom_votes:
        print("One or more URLs failed to fetch data. Skipping this iteration.")
        time.sleep(60)  # 等待下一次尝试
        continue

    total_votes = calculate_total_votes(my1pick_votes, mubeat_votes, fandom_votes)

    # 计算每个渠道的总票数
    my1pick_count = sum(my1pick_votes.values())
    mubeat_count = sum(mubeat_votes.values())
    fandom_count = sum(fandom_votes.values())

    # 计算差值
    my1pick_diffs = {}
    mubeat_diffs = {}
    fandom_diffs = {}
    total_diffs = {}

    for name in set(my1pick_votes.keys()).union(mubeat_votes.keys()).union(fandom_votes.keys()):
        my1pick_current = my1pick_votes.get(name, 0)
        mubeat_current = mubeat_votes.get(name, 0)
        fandom_current = fandom_votes.get(name, 0)
        total_current = total_votes.get(name, 0)

        # 计算差值
        if first_run:
            my1pick_diffs[name] = 0
            mubeat_diffs[name] = 0
            fandom_diffs[name] = 0
            total_diffs[name] = 0
        else:
            my1pick_diffs[name] = my1pick_current - last_my1pick_votes.get(name, 0)
            mubeat_diffs[name] = mubeat_current - last_mubeat_votes.get(name, 0)
            fandom_diffs[name] = fandom_current - last_fandom_votes.get(name, 0)
            total_diffs[name] = total_current - (
                last_my1pick_votes.get(name, 0) + last_mubeat_votes.get(name, 0) * 2 + last_fandom_votes.get(name, 0)
            )

        # 更新上次的票数
        last_my1pick_votes[name] = my1pick_current
        last_mubeat_votes[name] = mubeat_current
        last_fandom_votes[name] = fandom_current

    # 如果是第一次运行，设置标志为 False
    if first_run:
        first_run = False

    # 准备写入数据
    data_to_write = []
    for name in set(my1pick_votes.keys()).union(mubeat_votes.keys()).union(fandom_votes.keys()):
        my1pick_vote = my1pick_votes.get(name, 0)
        mubeat_vote = mubeat_votes.get(name, 0)
        fandom_vote = fandom_votes.get(name, 0)
        total_vote = total_votes.get(name, 0)
        data_to_write.append((
            name,
            total_vote,
            my1pick_vote,
            mubeat_vote,
            fandom_vote,
            time.strftime('%Y-%m-%d %H:%M:%S'),
            my1pick_diffs.get(name, 0),
            mubeat_diffs.get(name, 0),
            fandom_diffs.get(name, 0),
            total_diffs.get(name, 0)
        ))

    # 按照总票数排序
    data_to_write.sort(key=lambda x: x[1], reverse=True)

    write_to_csv(data_to_write)

    # 输出结果以表格形式
    print("\nDetailed Votes:")
    print(
        f"{'Name':<30} {'Total Votes':<15} {'My1Pick Votes':<15} {'Mubeat Votes':<15} {'Fandom Votes':<15} {'Timestamp':<20} "
        f"{'My1Pick Diff':<15} {'Mubeat Diff':<15} {'Fandom Diff':<15} {'Total Diff':<15}")
    for name in data_to_write:
        print(f"{name[0]:<30} {name[1]:<15} {name[2]:<15} {name[3]*2:<15} {name[4]:<15} {name[5]:<20} "
              f"{name[6]:<15} {name[7]:<15} {name[8]:<15} {name[9]:<15}")

    # 每分钟循环一次
    time.sleep(60)
