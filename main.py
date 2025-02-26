import subprocess
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>")
        sys.exit(1)
    
    command = sys.argv[1:]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=False)

        message = ""
        message += f"stdout: {result.stdout}\n"
        message += f"stderr: {result.stderr}\n"
        print(message)
    except Exception as e:
        print(f"Error executing command: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

