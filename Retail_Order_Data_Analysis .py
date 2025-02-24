import streamlit as st

import pandas as pd


st.title("Retail_anlysis")
st.write("------------------------------------------------------------------------")
st.subheader("1.Main file")

#main file
df = pd.read_csv("C:/Users/ragu/SA.csv")
st.dataframe(df)
st.markdown("""**Note:**
This file have additional column that is *'cost_quantity'* that is for calculating the profit of the product cost into quantity
""")


#import and connet mysql workbench
import pymysql
mysqlcn = pymysql.connect(host="127.0.0.1",user="root",passwd="Ragu@2000",database="retail_sale_analysis")


st.write("------------------------------------------------------------------------")

st.subheader("2.Business Insights for primary required questions")

set1=st.selectbox("**Given questions**",("Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8","Q9","Q10"))

#1.Top 10 highest revenue generating products
if set1 == "Q1":
    query1 = """SELECT sub_category, SUM(list_price * quantity) AS total_revenue 
                FROM SA
                GROUP BY sub_category
                ORDER BY total_revenue DESC
                LIMIT 10;"""
    df1 = pd.read_sql_query(query1, mysqlcn)
    st.write("Top 10 highest revenue generating products")
    st.dataframe(df1)
    st.write("This analysis identifies the top 10 highest revenue-generating sub-categories, helping businesses optimize inventory, marketing, and pricing strategies. It also reveals customer preferences, seasonal trends, and profitability insights for better decision-making. 🚀")

#2.Top 5 cities with the highest profit margins   
elif set1 == "Q2":
    query2="""SELECT city, SUM((list_price - cost_price) * quantity) / SUM(list_price * quantity) AS profit_margin
              FROM SA
              GROUP BY city
              ORDER BY profit_margin DESC
              LIMIT 5;"""
    df2 = pd.read_sql_query(query2, mysqlcn)
    st.write("Top 5 cities with the highest profit margins")
    st.dataframe(df2)
    st.write("This indicates that these locations have effective pricing strategies, lower costs, or high-margin products. Businesses should focus on expanding sales efforts, optimizing inventory, and reinforcing marketing strategies in these cities to maximize profitability.")

#3.Calculate the total discount given for each category
elif set1 == "Q3":
    query3="""SELECT category, SUM((discount_percent / 100) * list_price * quantity) AS total_discount
              FROM SA
              GROUP BY category;"""
    df3 = pd.read_sql_query(query3, mysqlcn)
    st.write("Calculate the total discount given for each category")
    st.dataframe(df3)
    st.write ("This suggests that the Technology category has the highest discount allocation, possibly to drive sales volume. Businesses should analyze if these discounts are effectively boosting revenue or if pricing strategies need optimization to maintain profitability.")

#4.Average sale price per product category
elif set1 == "Q4":
    query4="""SELECT category, AVG(list_price) AS avg_sale_price
              FROM SA
              GROUP BY category;"""
    df4 = pd.read_sql_query(query4, mysqlcn)
    st.write("Average sale price per product category")
    st.dataframe(df4)
    st.write("The average sale prices per category are Furniture ($298.70), Office Supplies ($137.39), and Technology ($422.12). Technology products have the highest average sale price, indicating premium pricing or high-value items. Businesses can leverage this by promoting high-margin technology products while optimizing pricing strategies for Furniture and Office Supplies to enhance sales and profitability.")

#5.Region with the highest average sale price
elif set1 == "Q5":
    query5="""SELECT region, AVG(list_price) AS avg_sale_price
              FROM SA
              GROUP BY region
              ORDER BY avg_sale_price DESC
              LIMIT 1;"""
    df5 = pd.read_sql_query(query5, mysqlcn)
    st.write("Region with the highest average sale price")
    st.dataframe(df5)
    st.write("The East region ($241.72) leads in average sale price, indicating strong demand for premium products. Businesses should focus on high-value offerings and targeted marketing here.")

#6.Total profit per category
elif set1 == "Q6":
    query6="""SELECT category, SUM((list_price - cost_price) * quantity) AS total_profit
              FROM SA
              GROUP BY category;"""
    df6 = pd.read_sql_query(query6, mysqlcn)
    st.write("Total profit per category")
    st.dataframe(df6)
    st.write("Office Supplies (133,570) leads in total profit, followed by Technology (121,880) and Furniture (55,430). Businesses should focus on sustaining profitability in Office Supplies while exploring growth opportunities in Technology and Furniture.")

#7.Top 3 segments with the highest quantity of orders
elif set1 == "Q7":
    query7="""SELECT segment, SUM(quantity) AS total_quantity
              FROM SA
              GROUP BY segment
              ORDER BY total_quantity DESC
              LIMIT 3;"""
    df7 = pd.read_sql_query(query7, mysqlcn)
    st.write("Top 3 segments with the highest quantity of orders")
    st.dataframe(df7)
    st.write("The Consumer segment (4,130 orders) leads in quantity, followed by Corporate (2,655) and Home Office (1,507). Businesses should prioritize marketing and promotions for Consumers while identifying growth opportunities in Corporate and Home Office segments.")

#8.Average discount percentage given per region
elif set1 == "Q8":
    query8="""SELECT category, SUM((discount_percent / 100) * list_price * quantity) AS total_discount
              FROM SA
              GROUP BY category;"""
    df8 = pd.read_sql_query(query8, mysqlcn)
    st.write("Average discount percentage given per region")
    st.dataframe(df8)
    st.write("Technology ($32,280) has the highest total discount, followed by Office Supplies ($30,131.70) and Furniture ($25,002.10). Businesses should evaluate if these discounts effectively drive sales or if pricing adjustments are needed to optimize profitability.")

#9.Product category with the highest total profit
elif set1 == "Q9":
    query9="""SELECT category, SUM((list_price - cost_price) * quantity) AS total_profit
              FROM SA
              GROUP BY category
              ORDER BY total_profit DESC
              LIMIT 1;"""   
    df9 = pd.read_sql_query(query9, mysqlcn)
    st.write("Product category with the highest total profit")
    st.dataframe(df9)
    st.write("Office Supplies ($133,570) is the most profitable category, indicating strong demand and efficient cost management. Businesses should focus on sustaining this growth while exploring ways to boost profitability in other categories.")

#10.Calculate the total revenue generated per year
elif set1 == "Q10":
    query10="""SELECT YEAR(order_date) AS year, SUM(list_price * quantity) AS total_revenue
               FROM SA
               GROUP BY YEAR(order_date)
               ORDER BY year;"""
    df10 = pd.read_sql_query(query10, mysqlcn)
    st.write("Calculate the total revenue generated per year")
    st.dataframe(df10)
    st.write("Revenue was 1,303,650 in 2022 and 1,186,060 in 2023, showing a decline. Businesses should analyze market trends, optimize pricing, and enhance marketing strategies to drive revenue growth.")



st.write("------------------------------------------------------------------------")

#two data frames for 

df1=pd.read_csv("C:/Users/ragu/SA1.csv")
df2=pd.read_csv("C:/Users/ragu/SA2.csv")

st.subheader("3.1 Orders table and Sales Transactions table")
st.write("Orders table (Dataframe 1)")
st.dataframe(df1)
st.info("INFO: Data Frame 1 already contains the given content and spans from order_id to sub_category. The sub_category acts as the primary key in the table.")

st.write("------------------------------------------------------------------------")

st.write("Sales Transactions table (Dataframe 2)")
st.dataframe(df2)
st.info("INFO: In Data Frame 2, the sub_category serves as a foreign key in the table. It consists of 10 columns, including discount, sale price, and profit, similar to the main DataFrame. Additionally, this DataFrame contains the cost_quantity column for profit calculations.")


st.write("------------------------------------------------------------------------")


st.subheader("3.2 Additional information improve sales performance ")
set2=st.selectbox("**10 new questions**",("Q11","Q12","Q13","Q14","Q15","Q16","Q17","Q18","Q19","Q20"))

#11. Total number of orders placed per segment
if set2 == "Q11":
    query11="""SELECT segment, COUNT(order_id) AS total_orders
               FROM SA1
               GROUP BY segment;"""
    df11= pd.read_sql_query(query11,mysqlcn)
    st.write("Total number of orders placed per segment")
    st.dataframe(df11)
    

#12. Identify High-Profit Margin Products
elif set2 == "Q12":
     query="""SELECT product_id, sub_category,
        (SUM((sales_price - cost_price) * quantity) / SUM(sales_price * quantity)) * 100 AS profit_margin
        FROM SA2
        GROUP BY product_id, sub_category
        HAVING profit_margin > 30
        ORDER BY profit_margin DESC
        LIMIT 10;"""
     df12=pd.read_sql_query(query,mysqlcn)
     st.write("Identify High-Profit Margin Products")
     st.dataframe(df12)
     

#13. Total discount given per region
elif set2=="Q13":
     query13="""SELECT region, SUM(discount) AS total_discount 
          FROM SA1
          JOIN SA2 ON SA1.sub_category = SA2.sub_category
          GROUP BY region;"""
     df13=pd.read_sql_query(query13,mysqlcn)
     st.write("Total discount given per region")
     st.dataframe(df13)


#14. Rank Products by Total Revenue Using
elif set2 == "Q14":
     query14="""SELECT product_id, sub_category, SUM(sales_price * quantity) AS total_revenue,
            ROW_NUMBER() OVER (ORDER BY SUM(sales_price * quantity) DESC) AS rank_product
            FROM SA2
            GROUP BY product_id, sub_category
            limit 10;"""
     df14=pd.read_sql_query(query14,mysqlcn)
     st.write("Rank Products by Total Revenue Using")
     st.dataframe(df14)


#15. Calculate the total number of products sold per year
elif set2 == "Q15": 
     query15= """SELECT YEAR(order_date) AS year, SUM(quantity) AS total_quantity
            FROM SA1
            JOIN SA2 ON SA1.sub_category = SA2.sub_category
            GROUP BY year;"""
     df15=pd.read_sql_query(query15,mysqlcn)
     st.write("Calculate the total number of products sold per year")
     st.dataframe(df15)

#16. Most frequently ordered product category
elif set2 =="Q16":
     query16="""SELECT category, COUNT(order_id) AS order_count
              FROM SA1 
              GROUP BY category
              ORDER BY order_count DESC
              LIMIT 1;"""
     df16=pd.read_sql_query(query16,mysqlcn)
     st.write("Most frequently ordered product category")
     st.dataframe(df16)

#17. Average order value per region
elif set2 == "Q17":
     query17="""SELECT region, AVG(sales_price) AS avg_order_value
             FROM SA1 
             JOIN SA2 ON SA1.sub_category = SA2.sub_category
             GROUP BY region;"""
     df17=pd.read_sql_query(query17,mysqlcn)
     st.write("Average order value per region")
     st.dataframe(df17)


#18. Categorize Products by Performance Level
elif set2 == "Q18":
     query18="""SELECT product_id, sub_category, SUM(sales_price * quantity) AS total_revenue,
      CASE 
           WHEN SUM(sales_price * quantity) > 50000 THEN 'High Revenue'
           WHEN SUM(sales_price * quantity) BETWEEN 20000 AND 50000 THEN 'Medium Revenue'
           ELSE 'Low Revenue'
       END AS revenue_category
       FROM SA2
       GROUP BY product_id, sub_category
       LIMIT 10;"""
     df18=pd.read_sql_query(query18,mysqlcn)
     st.write("Categorize Products by Performance Level")
     st.dataframe(df18)


#19. Month with the highest total sales revenue
elif set2 == "Q19":
     query19="""SELECT MONTH(order_date) AS month, SUM(sales_price) AS total_revenue
            FROM SA1
            JOIN SA2 ON SA1.sub_category = SA2.sub_category
            GROUP BY month
            ORDER BY total_revenue DESC
            LIMIT 1;"""
     df19=pd.read_sql_query(query19,mysqlcn)
     st.write("Month with the highest total sales revenue")
     st.dataframe(df19)


#20. Calculate the total profit earned per year
elif set2 == "Q20":
     query20="""SELECT YEAR(order_date) AS year, SUM(profit) AS total_profit
             FROM SA1
             JOIN SA2 ON SA1.sub_category = SA2.sub_category
             GROUP BY year;"""
     df20=pd.read_sql_query(query20,mysqlcn)
     st.write("Calculate the total profit earned per year")
     st.dataframe(df20)


st.write("------------------------------------------------------------------------")

st.markdown("**:rainbow[Thank you] for taking the time to review my analytics report.**")

















