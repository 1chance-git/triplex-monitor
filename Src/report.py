import os

# File paths
BREAK_LOG = "logs/break_log.txt"
RECOVERY_LOG = "logs/recovery_log.txt"
GROWTH_LOG = "logs/growth_log.txt"

def read_log(file_path):
    """Read a log file and return its content."""
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.readlines()
    return []

def generate_report():
    """Generate a summary report of the logs."""
    report = []
    
    # Read each log file
    break_events = read_log(BREAK_LOG)
    recovery_events = read_log(RECOVERY_LOG)
    growth_events = read_log(GROWTH_LOG)
    
    # Add each log file's content to the report
    report.append("=== Break Events ===")
    report.extend(break_events)
    
    report.append("\n=== Recovery Events ===")
    report.extend(recovery_events)
    
    report.append("\n=== Growth Events ===")
    report.extend(growth_events)
    
    # Return the full report as a string
    return "\n".join(report)

def save_report(report):
    """Save the generated report to a file."""
    with open("logs/summary_report.txt", "w") as file:
        file.write(report)

def main():
    """Main function to generate and save the report."""
    report = generate_report()
    save_report(report)
    print("Report generated and saved as summary_report.txt")

if __name__ == "__main__":
    main()
