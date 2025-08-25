import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from load_csv import load


def main():
    df = load("life_expectancy_years.csv")
    try:
        assert df is not None, "failed to load the DataFrame"
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")
        exit(1)
    brazil = df[df["country"] == "Brazil"]
    brazil = brazil.melt(id_vars="country", var_name="year",
                         value_name="life_expectancy")
    brazil["year"] = brazil["year"].astype(int)
    g = sns.relplot(data=brazil, x="year", y="life_expectancy",
                    kind="line", height=5, aspect=2)
    years = brazil["year"].tolist()
    min_year, max_year = min(years), max(years)
    step = 40
    xticks = list(range(min_year, max_year + 1, step))
    g.ax.set_xticks(xticks)
    plt.title("Brazil Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.tight_layout()
    plt.savefig("life_expectancy_brazil.png")
    plt.close()

if __name__ == "__main__":
    main()
