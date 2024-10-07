
import subprocess
import json

def run_security_audit():
    vulnerabilities = []
    # Example command to check for outdated dependencies with a timeout
    try:
        result = subprocess.run(['pip', 'list', '--outdated', '--format=json'], capture_output=True, text=True, timeout=30)
        outdated_packages = json.loads(result.stdout)

        if outdated_packages:
            for package in outdated_packages:
                vulnerabilities.append(f"Package {package['name']} is outdated. Current version: {package['version']}, Latest version: {package['latest_version']}.")
    except subprocess.TimeoutExpired:
        vulnerabilities.append("Timeout occurred while checking for outdated dependencies.")

    # Security check for known vulnerabilities with a timeout
    try:
        result = subprocess.run(['safety', 'check'], capture_output=True, text=True, timeout=30)
        if "No known security vulnerabilities found." not in result.stdout:
            vulnerabilities.append(result.stdout)
    except subprocess.TimeoutExpired:
        vulnerabilities.append("Timeout occurred while checking for known vulnerabilities.")

    return vulnerabilities

if __name__ == "__main__":
    vulnerabilities = run_security_audit()
    if vulnerabilities:
        print("Security Audit Report:")
        for issue in vulnerabilities:
            print(issue)
    else:
        print("No vulnerabilities found. Deployment is ready for production.")
