import subprocess
import sys

USER = "Rooyca"
REPO_DB = "short-db"
REPO_DEPLOY = "short"

def create_github_issue(url):
    cmd = ["gh", "issue", "create", "--repo", f"{USER}/{REPO_DB}", "--title", url, "--body", ""]
    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stdout.strip()
    return output.replace(f"github.com/{USER}/{REPO_DB}/issues", f"{USER}.github.io/{REPO_DEPLOY}")

def main():
    args = "".join(sys.argv[1:])
    if args and args.startswith("https://"):
        issue_output = create_github_issue(args)
        print(issue_output)
    else:
        print("Please enter a url...")
        exit(1)

if __name__ == "__main__":
    main()
