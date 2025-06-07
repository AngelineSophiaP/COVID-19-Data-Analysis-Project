import pandas as pd


df = pd.read_csv("covid_19_clean_complete.csv")


print(df.head())
print(df.info())


df['Date'] = pd.to_datetime(df['Date'])


df.fillna(0, inplace=True)


country_summary = df.groupby('Country/Region')[['Confirmed', 'Deaths', 'Recovered']].sum()
country_summary = country_summary.sort_values(by='Confirmed', ascending=False)
print(country_summary.head(10))


df_sorted = df.sort_values(['Country/Region', 'Date'])


df_sorted['NewCases'] = df_sorted.groupby('Country/Region')['Confirmed'].diff().fillna(0)


df_latest = df[df['Date'] == df['Date'].max()]


df_latest_grouped = df_latest.groupby('Country/Region')[['Confirmed', 'Deaths', 'Recovered']].sum()


df_latest_grouped['CFR'] = (df_latest_grouped['Deaths'] / df_latest_grouped['Confirmed']) * 100
df_latest_grouped['RecoveryRate'] = (df_latest_grouped['Recovered'] / df_latest_grouped['Confirmed']) * 100


print(df_latest_grouped.sort_values(by='CFR', ascending=False).head(10))


zero_deaths = df_latest_grouped[df_latest_grouped['Deaths'] == 0]
print(zero_deaths)


daily_global = df.groupby('Date')[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()
daily_global['NewConfirmed'] = daily_global['Confirmed'].diff().fillna(0)


max_day = daily_global.loc[daily_global['NewConfirmed'].idxmax()]
print("Date with max new cases:\n", max_day)
