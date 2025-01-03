# 🌟 Pre-Hackathon Project: Social Media Performance Analysis
Objective
This project was developed as part of a pre-hackathon assignment for the Level Supermind Hackathon. It focuses on creating a basic analytics module to analyze mock social media engagement data using Langflow and DataStax Astra DB.

The primary goal is to leverage AI-powered insights and cloud database operations to provide actionable feedback on social media post performance.

# Key feature
Fetch Engagement Data:

Created a simulated dataset of social media engagement, including metrics such as likes, shares, and comments for various post types (e.g., carousel, reels, static images).
Stored this dataset in DataStax Astra DB, a cloud-native NoSQL database for efficient querying and analytics.
Analyze Post Performance:

Built a Langflow workflow to query the Astra DB dataset.
Calculated average engagement metrics for each post type.
Generate Insights:

Integrated GPT-powered Langflow workflows to generate natural language insights based on the analyzed data.
Examples of insights include:
Carousel posts have 20% higher engagement than static posts.
Reels drive 2x more comments compared to other formats.
Tech Stack and Tools Used
Langflow

A no-code tool used to design workflows for integrating GPT-based insights.
Enabled the creation of automated analytics and insight generation pipelines.
DataStax Astra DB

A cloud-native NoSQL database is used to store and query the engagement dataset.
Provides scalable, high-performance database solutions suitable for analytics.
Streamlit

Used for creating an interactive front-end interface.
Displays insights in real-time with options to interact with the data.
Generative AI (GPT)

Leveraged GPT integration within Langflow to analyze trends and provide user-friendly insights.
How It Works
Data Simulation and Storage:
A small mock dataset was created to represent engagement metrics across post types. This data was uploaded to DataStax Astra DB.

Langflow Workflow:

Designed a workflow that accepts user input (post types) and queries the Astra DB dataset.
Langflow generates automated insights by processing the query results with GPT.
Insight Generation:

The insights provide valuable information on post-performance trends, helping users optimize their content strategy.
Demo Video
As part of the submission, a demo video showcases:

The Langflow workflow design.
DataStax Astra DB's role is to store and query the dataset.
How GPT integration generates actionable insights.
