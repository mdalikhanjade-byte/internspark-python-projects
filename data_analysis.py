def run_data_analysis():
    print("--- Data Analysis & Visualization Tool (Task 4) ---")
    
    # 1. Sample Data Input: Monthly Sales Performance Data
    sales_data = {
        "January": 1200,
        "February": 1500,
        "March": 800,
        "April": 1900,
        "May": 2200,
        "June": 1400
    }
    
    try:
        # 2. Data Aggregation / Statistics Calculation
        total_sales = sum(sales_data.values())
        highest_month = max(sales_data, key=sales_data.get)
        lowest_month = min(sales_data, key=sales_data.get)
        average_sales = total_sales / len(sales_data)
        
        # Displaying Calculated Summary Metrics
        print("\n=== Data Summary Statistics ===")
        print(f"Total Sales Performance : ${total_sales:,}")
        print(f"Average Monthly Sales    : ${average_sales:,.2f}")
        print(f"Highest Performing Month : {highest_month} (${sales_data[highest_month]:,})")
        print(f"Lowest Performing Month  : {lowest_month} (${sales_data[lowest_month]:,})")
        print("===============================\n")
        
        # 3. Data Visualization: Text-Based Bar Chart
        print("=== Visualized Sales Bar Chart ===")
        print(f"{'Month':<10} | {'Sales Visual Graph'}")
        print("-" * 45)
        
        for month, value in sales_data.items():
            # Generate a bar using block characters scale down (1 block per $100)
            bar_scale = value // 100
            bar_visual = "█" * bar_scale
            print(f"{month:<10} | {bar_visual} (${value:,})")
            
        print("-" * 45)
        print("Scale Layout: Each '█' represents $100 in sales.")
        
    except ZeroDivisionError:
        print("Analysis Error: The data dataset provided is empty.")
    except Exception as e:
        print(f"An unexpected analysis calculation error occurred: {e}")

if __name__ == "__main__":
    run_data_analysis()