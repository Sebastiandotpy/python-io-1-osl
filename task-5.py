import os
import csv
import shutil


DATA_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "initial")
REPORTS_DIR = os.path.join(DATA_ROOT, "work", "reports")
PENDING_JOBS_FILE = os.path.join(REPORTS_DIR, "pending_jobs.csv")
CUSTOMERS_FILE = os.path.join(DATA_ROOT, "work", "customers.csv")
JOBS_FILE = os.path.join(DATA_ROOT, "work", "jobs.csv")

def generate_pending_jobs_report():
    # Create the reports directory if it doesn't exist
    os.makedirs(REPORTS_DIR, exist_ok=True)
    
    # Load customer data into a dictionary for easy lookup
    customer_data = {}
    with open(CUSTOMERS_FILE, "r") as customers_csv:
        reader = csv.DictReader(customers_csv)
        for row in reader:
            customer_data[row["id"]] = row["name"]
    
    # Generate the pending jobs report
    pending_jobs = []
    with open(JOBS_FILE, "r") as jobs_csv:
        reader = csv.DictReader(jobs_csv)
        for row in reader:
            if "customer" in row and row["status"].lower() != "done":
                job_data = {
                    "id": row["id"],
                    "description": row["description"],
                    "client": customer_data.get(row["customer"], "Unknown")
                }
                pending_jobs.append(job_data)
    
    # Write the pending jobs report to CSV
    with open(PENDING_JOBS_FILE, "w", newline="") as pending_jobs_csv:
        fieldnames = ["id", "description", "client"]
        writer = csv.DictWriter(pending_jobs_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(pending_jobs)
    
    print("Pending jobs report generated successfully.")

if __name__ == "__main__":
    generate_pending_jobs_report()
