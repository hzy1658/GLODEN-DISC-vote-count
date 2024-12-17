import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Scatter, Page
import os
import argparse
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Scatter, Page
import os


# 绘制浏览量图
from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.commons.utils import JsCode
import pandas as pd

# 绘制浏览量图


# 绘制浏览量图
def plot_TotalVotes_graph(data, title_prefix):
   scatter = Scatter()

   # Create a consistent x-axis with all unique timestamps
   all_timestamps = pd.to_datetime(data['Timestamp']).dt.floor('min').dt.strftime('%Y-%m-%d %H:%M').unique().tolist()
   scatter.add_xaxis(all_timestamps)

   for singer in data['Name'].unique():
       singer_data = data[data['Name'] == singer]
       if not singer_data.empty:
           # Create a dictionary of views with timestamps as keys
           views_dict = dict(zip(
               pd.to_datetime(singer_data['Timestamp']).dt.floor('min').dt.strftime('%Y-%m-%d %H:%M'),
               singer_data['Total Votes']
           ))

           # Align views with the global x-axis
           views_aligned = [views_dict.get(ts, None) for ts in all_timestamps]

           scatter.add_yaxis(
               singer,
               views_aligned,
               symbol="circle",
               symbol_size=6,
               label_opts=opts.LabelOpts(is_show=False)  # 不显示数字
           )

   # Set global options
   scatter.set_global_opts(
       title_opts=opts.TitleOpts(title=f'{title_prefix} Total Votes Over Time'),
       xaxis_opts=opts.AxisOpts(type_='category', name="Time"),
       yaxis_opts=opts.AxisOpts(name="Total Votes"),
       tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross")
   )
   return scatter

def plot_My1PickVotes_graph(data, title_prefix):
   scatter = Scatter()

   # Create a consistent x-axis with all unique timestamps
   all_timestamps = pd.to_datetime(data['Timestamp']).dt.floor('min').dt.strftime('%Y-%m-%d %H:%M').unique().tolist()
   scatter.add_xaxis(all_timestamps)

   for singer in data['Name'].unique():
       singer_data = data[data['Name'] == singer]
       if not singer_data.empty:
           # Create a dictionary of views with timestamps as keys
           views_dict = dict(zip(
               pd.to_datetime(singer_data['Timestamp']).dt.floor('min').dt.strftime('%Y-%m-%d %H:%M'),
               singer_data['My1Pick Votes']
           ))

           # Align views with the global x-axis
           views_aligned = [views_dict.get(ts, None) for ts in all_timestamps]

           scatter.add_yaxis(
               singer,
               views_aligned,
               symbol="circle",
               symbol_size=6,
               label_opts=opts.LabelOpts(is_show=False)  # 不显示数字
           )

   # Set global options
   scatter.set_global_opts(
       title_opts=opts.TitleOpts(title=f'{title_prefix} My1Pick Votes Over Time'),
       xaxis_opts=opts.AxisOpts(type_='category', name="Time"),
       yaxis_opts=opts.AxisOpts(name="My1Pick Votes"),
       tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross")
   )
   return scatter

def plot_MubeatVotes_graph(data, title_prefix):
   scatter = Scatter()

   # Create a consistent x-axis with all unique timestamps
   all_timestamps = pd.to_datetime(data['Timestamp']).dt.floor('min').dt.strftime('%Y-%m-%d %H:%M').unique().tolist()
   scatter.add_xaxis(all_timestamps)

   for singer in data['Name'].unique():
       singer_data = data[data['Name'] == singer]
       if not singer_data.empty:
           # Create a dictionary of views with timestamps as keys
           views_dict = dict(zip(
               pd.to_datetime(singer_data['Timestamp']).dt.floor('min').dt.strftime('%Y-%m-%d %H:%M'),
               singer_data['Mubeat Votes']*2
           ))

           # Align views with the global x-axis
           views_aligned = [views_dict.get(ts, None) for ts in all_timestamps]

           scatter.add_yaxis(
               singer,
               views_aligned,
               symbol="circle",
               symbol_size=6,
               label_opts=opts.LabelOpts(is_show=False)  # 不显示数字
           )

   # Set global options
   scatter.set_global_opts(
       title_opts=opts.TitleOpts(title=f'{title_prefix} Mubeat Votes Over Time'),
       xaxis_opts=opts.AxisOpts(type_='category', name="Time"),
       yaxis_opts=opts.AxisOpts(name="Mubeat Votes"),
       tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross")
   )
   return scatter

def plot_FandomVotes_graph(data, title_prefix):
   scatter = Scatter()

   # Create a consistent x-axis with all unique timestamps
   all_timestamps = pd.to_datetime(data['Timestamp']).dt.floor('min').dt.strftime('%Y-%m-%d %H:%M').unique().tolist()
   scatter.add_xaxis(all_timestamps)

   for singer in data['Name'].unique():
       singer_data = data[data['Name'] == singer]
       if not singer_data.empty:
           # Create a dictionary of views with timestamps as keys
           views_dict = dict(zip(
               pd.to_datetime(singer_data['Timestamp']).dt.floor('min').dt.strftime('%Y-%m-%d %H:%M'),
               singer_data['Fandom Votes']
           ))

           # Align views with the global x-axis
           views_aligned = [views_dict.get(ts, None) for ts in all_timestamps]

           scatter.add_yaxis(
               singer,
               views_aligned,
               symbol="circle",
               symbol_size=6,
               label_opts=opts.LabelOpts(is_show=False)  # 不显示数字
           )

   # Set global options
   scatter.set_global_opts(
       title_opts=opts.TitleOpts(title=f'{title_prefix} Fandom Votes Over Time'),
       xaxis_opts=opts.AxisOpts(type_='category', name="Time"),
       yaxis_opts=opts.AxisOpts(name="Fandom Votes Votes"),
       tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross")
   )
   return scatter


# 在HTML文件中加入静态斜着的水印
def add_watermark_to_html(html_file):
   with open(html_file, 'r', encoding='utf-8') as file:
       html_content = file.read()
   with open(html_file, 'w', encoding='utf-8') as file:
       file.write(html_content)

def main():
   parser = argparse.ArgumentParser(description="Plot vote counts from CSV.")
   parser.add_argument("--gender", type=str, choices=['male', 'female'], default='female',
                       help="Specify gender for the CSV file (male or female).")
   args = parser.parse_args()

   gender = args.gender

   if gender == 'male':
       csv_file = r'.\GLODEN-DISC-male-vote_counts.csv'
       title_prefix = "GOLDEN-DISC-MALE-"
   elif gender == 'female':
       csv_file = r'.\GLODEN-DISC-female-vote_counts.csv'
       title_prefix = "GOLDEN-DISC-FEMALE-"
   else:
       print("Invalid gender specified.")
       return

   if os.path.exists(csv_file):
       data = pd.read_csv(csv_file)
       # 确保数据中存在 'timestamp' 列
       if 'Timestamp' not in data.columns:
           print("错误：数据中缺少 'timestamp' 列。")
           return

       page = Page(layout=Page.DraggablePageLayout)
       page.add(
           plot_TotalVotes_graph(data, title_prefix),
           plot_My1PickVotes_graph(data, title_prefix),
           plot_MubeatVotes_graph(data, title_prefix),
           plot_FandomVotes_graph(data, title_prefix)
       )
       output_file = rf"{title_prefix}_plots.html"
       page.render(output_file)
       print(f"图表已保存到 '{output_file}'。")

       # 添加水印
       add_watermark_to_html(output_file)
       print(f"水印已添加到 '{output_file}'。")

if __name__ == "__main__":
   main()
