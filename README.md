🌍 GDP per Capita Analysis Dashboard
  A comprehensive Streamlit web application for analyzing global GDP per capita data with interactive visualizations and insights.
  
📊 Features

  1.Interactive Data Exploration: Browse and filter GDP data by year and country
  
  2.Dynamic Visualizations:

    ->Line charts showing GDP trends over time
    ->Correlation heatmaps for economic indicators
    ->Country comparison bar charts
    
  3.Multi-metric Analysis: Analyze various economic indicators including:

    ->GDP per capita
    ->Global merchandise exports as share of GDP
    ->Government expenditure percentage
    ->Trade as share of GDP
    ->Inflation rates
    
  4.User-friendly Interface: Intuitive sidebar controls and responsive design

  📁 Project Structure:

          gdp_streamlit_app/
          ├── app.py                 # Main Streamlit application
          ├── gdp_per_capita.csv     # GDP dataset
          ├── requirements.txt       # Python dependencies
          └── README.md             # Project documentation

🛠️ Installation & Setup:

    Prerequisites:

      Python 3.7 or higher
      pip package manager

    Local Development

      1.Clone the repository
          ->bashgit clone https://github.com/yourusername/gdp-streamlit-app.git
          ->cd gdp-streamlit-app
      2.Install dependencies
      
          ->pip install -r requirements.txt
      3.Run the application
          ->streamlit run app.py
          
  📈 Dataset Information:
      The application uses a comprehensive GDP per capita dataset containing:

        ->147,615 records across multiple countries and years
        ->Time span: Historical data spanning multiple decades
        ->Key metrics:
            GDP per capita (PPP adjusted)
            Merchandise exports as % of GDP
            Government expenditure as % of GDP
            Trade as % of GDP
            Annual inflation rates        

🛠️ Technology Stack:

    ->Frontend: Streamlit
    ->Data Processing: Pandas
    ->Visualizations: Matplotlib, Seaborn
    ->Deployment: Streamlit Community Cloud

📊 Key Insights:
      This dashboard enables users to discover:

      ->Economic Growth Patterns: Track GDP growth trajectories across different nations
      ->Trade Relationships: Understand how international trade impacts GDP
      ->Government Spending Impact: Analyze correlation between public expenditure and economic performance  
      ->Inflation Trends: Monitor price stability across different economies

      
















          
