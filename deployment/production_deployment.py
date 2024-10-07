
import os
import subprocess

def deploy_to_production():
    # Example: Deploy the frontend and backend services
    try:
        # Build and deploy frontend
        print("Building and deploying frontend...")
        subprocess.run(["npm", "run", "build"], cwd="../frontend", check=True)

        # Deploy backend services
        print("Deploying backend services...")
        subprocess.run(["pm2", "start", "server.js"], cwd="../backend", check=True)

        print("Production deployment completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Deployment failed: {e}")

if __name__ == "__main__":
    deploy_to_production()
