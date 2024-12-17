
# 金唱片流行艺人投票数据爬取及可视化脚本

**开发者:** 
* 微博: [@AAAwatchingA](https://weibo.com/u/2411424231) 
* B站: [@AAAwatching](https://space.bilibili.com/503440358?spm_id_from=333.1296.0.0) 

**项目简介:**

本项目提供了一套 Python 脚本，用于爬取金唱片流行艺人投票数据，并将数据进行可视化展示。该项目包括数据爬取、数据处理和可视化三个部分，旨在帮助用户实时了解投票情况。

## 文件结构

```
├── GLODEN DISC-FEMALE.py   # 每分钟爬取女性艺人投票数据并保存为 CSV 文件
├── GLODEN DISC-MALE.py     # 每分钟爬取男性艺人投票数据并保存为 CSV 文件
├── GD-PIC.py              # 将爬取的数据生成图表
└── GD-html.py             # 将数据可视化为可交互的静态网页
```

## 环境依赖

请确保你的 Python 环境中已安装以下依赖包：

* **`GLODEN DISC-FEMALE.py` 和 `GLODEN DISC-MALE.py`:**
    * `requests`
* **`GD-PIC.py`:**
    * `requests`
    * `urllib3`
    * `seaborn`
* **`GD-html.py`:**
    * `pyecharts`

你可以使用 `pip` 安装这些依赖：

```bash
pip install requests urllib3 seaborn pyecharts
```

## 快速开始

1. **克隆项目:** 将项目克隆到本地。
2. **进入项目目录:** 在终端中进入项目所在的文件夹。

### 数据爬取

* **爬取女性艺人投票数据:**
  ```bash
  python GLODEN-DISC-FEMALE.py
  ```
* **爬取男性艺人投票数据:**
  ```bash
  python GLODEN-DISC-MALE.py
  ```

   *运行以上命令后，脚本将每分钟自动爬取数据并保存为 CSV 文件。（也可自行修改爬取频率）*

### 数据可视化

* **导出图表:**

  *   **女性艺人:**
        ```bash
        python GD-PIC.py --gender female
        ```
  *   **男性艺人:**
        ```bash
        python GD-PIC.py --gender male
        ```

    *运行以上命令后，脚本将生成图表并保存为图片文件。*

* **导出可交互 HTML 页面:**

  *   **女性艺人:**
        ```bash
        python GD-html.py --gender female
        ```
  *   **男性艺人:**
        ```bash
        python GD-html.py --gender male
        ```

    *运行以上命令后，脚本将生成一个包含可交互图表的 HTML 文件。*

## 注意事项

*   如果安装出现pysocks相关问题，请在不挂梯子的情况下`pip install pysocks`,再挂梯子即可正常安装
*   请确保你的网络连接正常，梯子正常连接，以便脚本可以正常爬取数据。
*   如果爬取过程中出现问题，请检查依赖包是否正确安装，并检查网络连接。
*   请尊重网站的 robots.txt 协议，合理使用爬虫。
*   本项目仅用于学习和交流，请勿用于商业用途。

## 贡献

欢迎大家提交 issue 和 pull request，共同完善本项目。


