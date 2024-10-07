
import subprocess
import json

def run_security_audit():
    vulnerabilities = []
    # Example command to check for outdated dependencies
    result = subprocess.run(['pip', 'list', '--outdated', '--format=json'], capture_output=True, text=True)
    outdated_packages = json.loads(result.stdout)

    if outdated_packages:
        for package in outdated_packages:
            vulnerabilities.append(f"Package {package['name']} is outdated. Current version: {package['version']}, Latest version: {package['latest_version']}.")

    # Security check for known vulnerabilities
    result = subprocess.run(['safety', 'check'], capture_output=True, text=True)
    if "No known security vulnerabilities found." not in result.stdout:
        vulnerabilities.append(result.stdout)

    return vulnerabilities

if __name__ == "__main__":
    vulnerabilities = run_security_audit()
    if vulnerabilities:
        print("Security Audit Report:")
        for issue in vulnerabilities:
            print(issue)
    else:
        print("No vulnerabilities found. Deployment is ready for production.")
