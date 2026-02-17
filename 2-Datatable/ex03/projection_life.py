import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker
import pandas as pd
from load_csv import load
matplotlib.use("Agg")


def thousands_formatter(x, pos):
    return f'{x/1_000:.0f}k'


def main():
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_exp = load("life_expectancy_years.csv")
    try:
        assert income is not None, (
            "failed to load "
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )
        assert life_exp is not None, "failed to load life_expectancy_years.csv"
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")
        exit(1)
    income = income.set_index("country")["1900"]
    life_exp = life_exp.set_index("country")["1900"]
    df = pd.DataFrame({
        "income": income,
        "life_exp": life_exp
    })
    df = df.dropna()
    df["income"] = df["income"].astype(float)
    df["life_exp"] = df["life_exp"].astype(float)
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=df, x="income", y="life_exp", s=80)
    plt.xscale("log")
    plt.xlim(left=300)
    ax = plt.gca()
    formatter = mticker.FuncFormatter(thousands_formatter)
    ax.xaxis.set_major_formatter(formatter)
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.tight_layout()
    plt.savefig("life_expectancy_income_1900.png")
    plt.close()


if __name__ == "__main__":
    main()
