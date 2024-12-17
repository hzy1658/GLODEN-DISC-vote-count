import requests
import csv
import re
from datetime import datetime
import time
import pandas as pd
import matplotlib.pyplot as plt
import urllib3
import os
import argparse
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['Malgun Gothic']
plt.rcParams['axes.unicode_minus'] = False    # 解决负号 '-' 显示为方块的问题
# 禁用 InsecureRequestWarning 警告

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 定义伪装的 User-Agent
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

singer_urls = {
}



def plot_views_graph(file_name, title):
   if not os.path.exists(file_name):
       print(f"File {file_name} does not exist, cannot plot graph.")
       return

   # 读取 CSV 文件
   data = pd.read_csv(file_name)

   plt.figure(figsize=(10, 6))

   # 使用 seaborn 提供的调色板
   colors = sns.color_palette("husl", 15)  # 生成15种颜色

   for i, (singer, group) in enumerate(data.groupby('Name')):
       plt.plot(pd.to_datetime(group['Timestamp']), group['Total Votes'],
                marker='o', label=f'{singer}', color=colors[i % len(colors)])  # 使用颜色

   plt.title(f'{title} vote count Over Time')
   plt.xlabel('Time')
   plt.ylabel('Views')
   plt.xticks(rotation=45)
   plt.legend()
   plt.tight_layout()
   plt.figtext(0.1, 0.02, 'developer：weibo:AAAwatchingA,bilibili:AAAwatching', fontsize=10, ha='left', va='bottom')

   plt.savefig(fr'{title} vote count_plot.png')
   print(f"Views plot saved as '{title}-vote count_plot.png'.")

   plt.show()


def main():
   parser = argparse.ArgumentParser(description="Plot vote counts from CSV.")
   parser.add_argument("--gender", type=str, choices=['male', 'female'], default='male',
                       help="Specify gender for the CSV file (male or female).")
   args = parser.parse_args()

   gender = args.gender

   if gender == 'male':
       csv_file = fr'GLODEN-DISC-male-vote_counts.csv'
       title = "GOLDEN-DISC-MALE-VOTE"
   elif gender == 'female':
       csv_file = fr'GLODEN-DISC-female-vote_counts.csv'
       title = "GOLDEN-DISC-FEMALE-VOTE"
   else:
       print("Invalid gender specified.")
       return

   plot_views_graph(csv_file, title)



if __name__ == '__main__':
   main()
