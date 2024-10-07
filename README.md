
# AI-Driven Integrated Development Environment (IDE)

## Overview
This is an advanced AI-powered IDE designed to assist developers throughout the entire software development lifecycle. It combines intelligent automation, deep AI integration, and user-centric customization to maximize productivity and streamline development processes. Key features include the open-interpreter AI chat popup, a customizable dashboard homepage, and the GPT-Pilot module for real-life project generation.

### Core Features
1. **AI-Powered Code Review Assistant**: Analyzes code snippets and suggests improvements.
2. **AI Code Search and Navigation**: Allows developers to search project files using natural language.
3. **Integrated Voice Control**: Interact with the IDE using voice commands.
4. **Customizable Productivity Dashboard**: Personalized dashboard widgets that help track progress and tasks.
5. **Interactive Debugging AI**: AI-assisted debugging to identify issues in code.
6. **Real-Time Collaboration Workspace**: Collaborate with other developers in real-time with AI assistance.
7. **AI-Driven Test Case Generation and Automation**: Automatically generates test cases for written code.
8. **Serverless Function Deployment**: Supports deploying functions to serverless platforms like AWS Lambda.

## Setup Instructions

### Prerequisites
- Python >= 3.8
- Git
- Pip
- A GitHub personal access token for repository management (used for GitPython integration)

### Installation Steps

1. **Clone the Repository**
   ```
   git clone https://github.com/ZanaNowshad/ai-driven-ide-complete.git
   cd ai-driven-ide-complete
   ```

2. **Install Dependencies**
   Run the following command to install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
   *Note*: Some packages may need to be upgraded manually to address vulnerabilities. You may encounter warnings during the security audit.

3. **Configure Environment Variables**
   Set up the required environment variables:
   ```
   export GITHUB_TOKEN=your_github_token
   ```
   This is required for pushing changes to GitHub using GitPython.

4. **Install GitPython and Safety Tools**
   To manage Git operations programmatically and perform security audits:
   ```
   pip install gitpython safety
   ```

5. **Run the IDE**
   To start the AI-driven IDE:
   ```
   python start_ide.py
   ```

### Running Security Audit
To ensure that the environment is secure and ready for production, run the following command:
```
python AI/deployment_readiness/security_audit.py
```

### Running Integration Tests
Integration tests can be run to verify that the different components of the IDE work seamlessly together:
```
python AI/integration_testing/integration_tests.py
```

## Project Structure

```
ai-driven-ide-complete/
│
├── AI/
│   ├── code_review/                # Contains the Code Review Assistant script
│   ├── collaboration/              # Real-Time Collaboration script
│   ├── debugging/                  # Interactive Debugging script
│   ├── serverless_deployment/      # Serverless Function Deployment script
│   ├── integration_testing/        # Integration Testing framework
│   ├── deployment_readiness/       # Security Audits and Deployment Readiness checks
│
├── README.md                       # Project documentation
├── requirements.txt                # Required Python packages
└── start_ide.py                    # Entry point to start the IDE
```

## Usage Guide

- **Open-Interpreter AI Chat Popup**: Use the chat window docked to the right of the IDE to ask questions about coding, generate code snippets, or refactor code.
- **GPT-Pilot Module**: This module allows users to create full-fledged projects using natural language descriptions. Just describe your project, and the module will generate a production-ready codebase.
- **Customizable Dashboard Homepage**: The homepage allows you to view project metrics, manage tasks, and even drag-and-drop widgets for personalization.

### Common Commands
- **Run Integration Tests**: Tests are located in `AI/integration_testing/integration_tests.py`.
- **Perform Security Audit**: To run a security audit for outdated or vulnerable packages, use the script in `AI/deployment_readiness/security_audit.py`.

## Deployment Readiness & Security
- Regularly perform a security audit using the `safety` tool to ensure there are no known vulnerabilities in the dependencies.
- Ensure all dependencies are updated to the latest secure versions to mitigate potential risks.

## Contribution Guidelines
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

## Future Work
- **Integrate Containerization**: Dockerize the IDE for easier deployment.
- **Additional AI Models**: Add support for different AI models for increased flexibility.
- **Cloud IDE**: Expand the IDE to support cloud development environments for greater scalability.

## License
This project is licensed under the MIT License.

---

**NOTE**: Always keep the environment secure by updating the dependencies and addressing any vulnerabilities reported during the security audits.

