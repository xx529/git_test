"""
Pandas Demo — 展示常用 pandas 操作的示例代码
"""

import os

import pandas as pd

TAX_RATE = 0.8


def main():
    # 1. 创建 DataFrame
    print("=" * 50)
    print("1. 创建 DataFrame")
    print("=" * 50)
    df = pd.DataFrame({
        "姓名": ["张三", "李四", "王五", "赵六", "孙七"],
        "年龄": [28, 35, 42, 29, 31],
        "城市": ["北京", "上海", "广州", "深圳", "杭州"],
        "薪资": [15000, 22000, 28000, 18000, 20000],
    })
    print(df)

    # 2. 基本信息查看
    print("\n" + "=" * 50)
    print("2. 基本信息")
    print("=" * 50)
    print(f"形状: {df.shape}")
    print(f"列名: {df.columns.tolist()}")
    print(f"数据类型:\n{df.dtypes}")

    # 3. 描述性统计
    print("\n" + "=" * 50)
    print("3. 描述性统计")
    print("=" * 50)
    print(df.describe())

    # 4. 筛选数据
    print("\n" + "=" * 50)
    print("4. 筛选：薪资 > 18000")
    print("=" * 50)
    high_salary = df[df["薪资"] > 18000]
    print(high_salary)

    # 5. 排序
    print("\n" + "=" * 50)
    print("5. 按薪资降序排列")
    print("=" * 50)
    sorted_df = df.sort_values("薪资", ascending=False)
    print(sorted_df)

    # 6. 分组聚合
    print("\n" + "=" * 50)
    print("6. 按城市分组，计算平均薪资")
    print("=" * 50)
    group_stats = df.groupby("城市")["薪资"].agg(["mean", "min", "max", "count"])
    print(group_stats)

    # 7. 添加新列
    print("\n" + "=" * 50)
    print("7. 添加'税后薪资'列 (按80%计算)")
    print("=" * 50)
    df["税后薪资"] = (df["薪资"] * TAX_RATE).astype(int)
    print(df)

    # 8. 合并 DataFrame
    print("\n" + "=" * 50)
    print("8. 合并 DataFrame")
    print("=" * 50)
    dept_df = pd.DataFrame({
        "姓名": ["张三", "李四", "王五", "赵六", "孙七"],
        "部门": ["研发", "产品", "研发", "设计", "运营"],
    })
    merged = df.merge(dept_df, on="姓名", how="left")
    print(merged)

    # 9. 读取/写入 CSV（示例）
    print("\n" + "=" * 50)
    print("9. CSV 读写")
    print("=" * 50)
    csv_path = "employees_demo.csv"
    merged.to_csv(csv_path, index=False, encoding="utf-8-sig")
    read_back = pd.read_csv(csv_path)
    print(f"已写入 {csv_path}，重新读取验证：")
    print(read_back)

    # 清理临时文件
    if os.path.exists(csv_path):
        os.remove(csv_path)

    print("\n✅ Pandas Demo 运行完成！")


if __name__ == "__main__":
    main()
