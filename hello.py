from preswald import connect, get_df, table, query, plotly, text
import plotly.express as px

connect()
df = get_df("video_games")
text("## Top 10 Games by Global Sales\nThis bar chart shows the 10 best-selling video games globally, with hover info and legend filtering enabled.")

top10 = df.sort_values("Global_Sales", ascending=False).head(10)

fig = px.bar(
    top10,
    x="Name",
    y="Global_Sales",
    color="Platform",
    title="Top 10 Games by Global Sales",
    labels={"Global_Sales": "Global Sales (millions)", "Name": "Game"},
    hover_data={
        "Year": True,
        "Genre": True,
        "Publisher": True,
        "Global_Sales": ':.2f',
        "Name": False,  
        "Platform": False  
    },
)

fig.update_layout(
    xaxis_tickangle=45,
    template="plotly_white",
    legend_title_text="Platform", 
    hoverlabel=dict(bgcolor="white", font_size=12, font_family="Arial")
)

plotly(fig)


text("## Sales Distribution by Region\nThis stacked bar chart shows how game sales are distributed across regions for the top 10 best-selling games.")

fig = px.bar(
    top10,
    x="Name",
    y=["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"],
    title="Regional Sales Distribution (Top 10 Games)",
    labels={"value": "Sales (millions)", "variable": "Region"},
)
fig.update_layout(barmode="stack", xaxis_tickangle=45, template="plotly_white")
plotly(fig)

text("## Platform Popularity\nThis pie chart shows which platforms have the most games in the dataset.")

platform_count = df["Platform"].value_counts().reset_index()
platform_count.columns = ["Platform", "Count"]

fig = px.pie(
    platform_count,
    names="Platform",
    values="Count",
    title="Distribution of Games by Platform",
)
fig.update_layout(template="plotly_white")
plotly(fig)






