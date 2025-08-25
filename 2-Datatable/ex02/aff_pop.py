import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker
from load_csv import load


def parse_population(val):
    """
    Converts a population string with optional suffixes ('M' for millions, 'k'
    for thousands) to an integer.

    Args:
        val (str): The population value as a string. It may end with 'M'
        (millions), 'k' (thousands), or have no suffix.

    Returns:
        int: The population value as an integer.

    Examples:
        >>> parse_population('2.5M')
        2500000
        >>> parse_population('800k')
        800000
        >>> parse_population('12345')
        12345
    """
    val = val.strip()
    if val.endswith('M'):
        return int(float(val[:-1]) * 1_000_000)
    elif val.endswith('k'):
        return int(float(val[:-1]) * 1_000)
    else:
        return int(val)


def millions_formatter(x, pos):
    """
    Formats a numeric value as a string representing millions with an 'M'
    suffix.

    Args:
        x (float or int): The numeric value to format.
        pos (int): The position of the tick (required for compatibility with
        matplotlib's formatter interface, but not used in the function).

    Returns:
        str: The formatted string with the value in millions followed by 'M'.
    """
    return f'{x/1_000_000:.0f}M'


def main():
    df = load("population_total.csv")
    try:
        assert df is not None, "failed to load the DataFrame"
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")
        exit(1)
    countries = df[df["country"].isin(["Brazil", "Argentina"])]
    countries = countries.melt(id_vars="country", var_name="year",
                               value_name="population")
    countries["year"] = countries["year"].astype(int)
    countries = countries[countries["year"] <= 2050]
    countries["population"] = countries["population"].apply(parse_population)
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=countries, x="year", y="population", hue="country")
    years = countries["year"].tolist()
    min_year, max_year = min(years), max(years)
    step = 40
    xticks = list(range(min_year, max_year + 1, step))
    plt.xticks(xticks)
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(title=None)
    plt.gca().yaxis.set_major_formatter(
        mticker.FuncFormatter(millions_formatter))
    plt.tight_layout()
    plt.savefig("brazil_vs_argentina_population.png")
    plt.close()


if __name__ == "__main__":
    main()
