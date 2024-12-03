# 🚀 Student Innovations Lab with GitHub Copilot
![image](https://github.com/user-attachments/assets/80940b23-aa74-4ec5-a256-905ec75998e6)


Welcome to **Student Innovations Lab**! This repository is a hands-on workspace where students can explore, create, and innovate using **GitHub Copilot**. Here, you’ll find a variety of issues and projects designed to help you practice Copilot’s capabilities, from generating code snippets to building complete prototypes. Whether you’re new to coding or experienced, this space is for you to develop skills, solve real-world problems, and bring your ideas to life.

## 🌟 Repository Purpose

This repository is designed to:
1. **Help students learn** how to use GitHub Copilot through practical tasks and challenges.
2. **Provide project ideas** focused on innovation in fields like healthcare, sustainable technology, and smart cities.
3. **Offer practice issues** where you can experiment with different Copilot capabilities, such as generating code, optimizing functions, debugging, and much more.

Use this repository as a safe space to learn, experiment, and get inspired to create something impactful!

---

## 📝 How to Use This Repository

1. **Explore the Project Ideas**: Browse through the folders in this repo to see various categories, like `Healthcare-Innovation`, `Education-Tools`, and more. Each folder contains starter files and example code you can use as a foundation.

2. **Practice with GitHub Issues**: Head over to the [Issues](https://github.com/AnthonyByansi/Innovate-with-Copilot-workspace/issues) tab to find practice tasks tailored for Copilot. These tasks range from simple prompts to more complex challenges. Each issue includes:
   - A brief description of the task.
   - Step-by-step instructions on how to use Copilot to complete it.
   - Tips on prompts and suggestions to explore Copilot’s features further.

3. **Experiment Freely**: Feel free to try different prompts with Copilot, explore new ways of solving tasks, and make the projects your own. This is a space to learn by doing.

4. **Submit Your Solutions**: If you’d like to share your work, feel free to submit a Pull Request or start a Discussion. Collaborate with others and get feedback on your work!

---

## 🛠️ Getting Started with GitHub Copilot

If this is your first time using Copilot, here’s how to set it up:
1. **Install** GitHub Copilot in your IDE (VS Code or similar).
2. **Open this repository** in your IDE and try out some of the issues listed.
3. **Use the README and Issues** as your guide to experiment with Copilot in different coding scenarios.

For more details on setting up Copilot, check out the official [GitHub Copilot documentation](https://docs.github.com/en/copilot).

---

## 🚀 Ready to Innovate?

We’re excited to see what you’ll create!

## 📝 How to Run the Flask Application

To run the Flask application, follow these steps:

1. **Install the required dependencies**: Make sure you have Python and pip installed. Then, install the required packages by running:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up the database**: Initialize the SQLite database by running the following commands in the Python shell:
   ```python
   from app import db
   db.create_all()
   ```

3. **Run the Flask application**: Start the Flask development server by running:
   ```bash
   flask run
   ```

4. **Access the application**: Open your web browser and go to `http://localhost:5000` to access the application.

5. **API Endpoints**: The following API endpoints are available:
   - `POST /register`: Register a new user.
   - `POST /login`: Log in a user and receive a JWT token.
   - `POST /login/google`: Log in a user using Google OAuth 2.0.
   - `POST /login/facebook`: Log in a user using Facebook OAuth 2.0.
   - `POST /ideas`: Create a new student innovation idea (requires JWT token).
   - `GET /ideas`: Get all student innovation ideas (requires JWT token).
   - `PUT /ideas/<id>`: Update a student innovation idea by ID (requires JWT token).
   - `DELETE /ideas/<id>`: Delete a student innovation idea by ID (requires JWT token).
