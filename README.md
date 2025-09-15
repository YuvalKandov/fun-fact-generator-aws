# ☁️ Fun Fact Generator – Serverless AWS + AI

A serverless cloud application that delivers witty, AI-enhanced fun facts.  
Built with **AWS Lambda, API Gateway, DynamoDB, Amplify Hosting, and Amazon Bedrock (Claude AI).**

---

## 🚀 Overview

This project demonstrates how to build a **real-world serverless web application** by combining:
- **Serverless compute** with AWS Lambda  
- **API-driven communication** using API Gateway  
- **Database-backed persistence** with DynamoDB  
- **Generative AI** via Amazon Bedrock (Claude)  
- **Static web hosting** with AWS Amplify  

---

## 🏗️ Architecture

<img width="570" height="426" alt="Fun Fact Generator (Serverless AWS + AI) drawio" src="https://github.com/user-attachments/assets/b69460c2-3982-48dd-98ae-ac06e5e72385" />

### Flow
1. **User** opens the frontend hosted on **AWS Amplify**  
2. Clicking **“Generate Fun Fact”** triggers an **API request** through **API Gateway**  
3. **API Gateway** invokes the **Lambda function**  
4. **Lambda** fetches a random fact from **DynamoDB**  
5. The fact is sent to **Amazon Bedrock (Claude AI)** for rephrasing  
6. **Bedrock** returns a witty, AI-powered version of the fact  
7. The **Amplify frontend** displays the result to the user  

---

## 🔧 Technologies Used

- **AWS Lambda** – serverless compute  
- **API Gateway (HTTP API)** – API exposure  
- **DynamoDB** – fact storage  
- **IAM** – secure permissions  
- **Amazon Bedrock (Claude AI)** – Generative AI enhancement  
- **AWS Amplify** – frontend hosting  
- **HTML + Tailwind** – frontend design  

---
## 🐍 Lambda Function (Python)

The core logic runs on AWS Lambda using Python.

- Retrieves a random fact from DynamoDB  
- Optionally rephrases it via Amazon Bedrock (Claude AI)  
- Returns the result as JSON through API Gateway  

Code is in [`lambda/LambdaCode.py`](lambda/LambdaCode.py).

---
## 📸 Screenshots

<img width="870" height="684" alt="image" src="https://github.com/user-attachments/assets/267e2ca8-1cdb-467a-8695-c54ad279128c" />

---

## 📚 Lessons Learned

- Configuring **CORS** correctly for API Gateway + Amplify  
- Securing **DynamoDB access** with IAM roles  
- Integrating **Amazon Bedrock** into a serverless workflow  
- Deploying a **frontend + backend** end-to-end on AWS  

---

## 💡 Future Enhancements

- Add **authentication** (Cognito) so users can log in and save favorites  
- Replace facts database with a more complex schema (categories, tags)  
- Add **CI/CD pipeline** for frontend + Lambda deployment  
- Containerize Lambda with **Docker** for portability  

---
