# AWS Lambda Resume API Challenge

## Introduction

This project is designed to showcase the development of a serverless API using AWS Lambda and DynamoDB, integrated with GitHub Actions. The primary objective is to construct an API capable of serving resume data in JSON format. This document provides guidance on setting up, deploying, and using the API.

## Getting Started

### Prerequisites

Before you begin, ensure you have installed the following software:

- AWS CLI
- Git
- An Integrated Development Environment (IDE) such as Visual Studio Code

### Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Configure your AWS credentials by setting up your Access Key ID and Secret Access Key. It's recommended to use environment variables or AWS Secrets Manager for security reasons.

## Project Structure

The project consists of the following main components:

- **DynamoDB Table (`resumes`)**: Stores resume data in JSON format.
- **AWS Lambda Function**: Fetches and returns resume data based on an ID.
- **API Gateway**: Exposes the Lambda function through HTTP endpoints.
- **GitHub Actions Workflow**: Automates the deployment of the Lambda function on every push to the repository.

## Usage

To use the API, send a GET request to the endpoint URL with a query parameter specifying the resume ID. For example:

Replace `/resume` with your actual API Gateway endpoint path and `12345` with the desired resume ID.

## Deployment

Deployment is automated through GitHub Actions. Any changes pushed to the repository will trigger the deployment workflow, updating the Lambda function and API Gateway configuration accordingly.

## Contributing

Contributions are welcome! Please follow the standard fork-and-pull request workflow.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- AWS for providing the cloud infrastructure and services.
- GitHub Actions for CI/CD automation.
- The community for support and inspiration.


