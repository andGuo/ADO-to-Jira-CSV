import csv
from dataclasses import dataclass


@dataclass
class Mapping:
    azure_str: str | None
    jira_str: str


source_file = "data.csv"

header_mappings = [
    Mapping("Area Level 2", "Project"),
    Mapping("Title", "Summary"),
    Mapping("Description", "Description"),
    Mapping("ID", "Issue Key"),
    Mapping(None, "Component"),
    Mapping(None, "Affects Version"),
    Mapping("Azure DevOps", "Fix Version"),
    Mapping(None, "Comment Body"), # maybe can scrape comments and add them here 
    Mapping("Created Date", "Date Created"),
    Mapping("Changed Date", "Date Modified"),
    Mapping("Due Date", "Due Date"),
    Mapping(
        "Work Item Type", "Issue Type"
    ),  # else uses default (i.e. first) value specififed in Jira
    Mapping("Stack Rank", "Issue rank"),  # Won't be retained???
    Mapping("Tags", "Labels"),
    Mapping(
        "Priority", "Priority"
    ),  # else uses default (i.e. first) value specififed in Jira
    Mapping(
        "Resolved Reason", "Resolution"
    ),  # else uses default (i.e. first) value specififed in Jira
    Mapping(
        "State", "Status"
    ),  # else uses default (i.e. first) value specififed in Jira
    Mapping("Original Estimate", "Original Estimate"),
    Mapping(
        None, "Remaining Estimate"
    ),  # probably can calculate from Original Estimate and Finish Date
    Mapping("Effort", "Time Spent"),
    Mapping("Assigned To", "Assignee"),
    Mapping(
        "Created By", "Reporter"
    ), 
    Mapping(None, "Users"), # maybe can add all commenters here if we end up scraping comments
    Mapping(None, "Watchers"), 
    Mapping(None, "Other fields"),  # Insert custom fields here
]


def map_to_jira(header: str) -> str:
    for mapping in header_mappings:
        if mapping.azure_str == header:
            return mapping.jira_str
    
    print(f"WARNING: No mapping found for {header}")

    return header


def convert_to_jira_date_format(date: str) -> str:
    pass


def convert_to_jira_type(type: str) -> str:
    pass


def convert_to_jira_priority(priority: str) -> str:
    pass


def map_to_jira_user(user: str) -> str:
    pass


def main():
    data: list(str) = []

    with open(source_file, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    header_row = data[0]
    mapped_header = [map_to_jira(header) for header in header_row]

    with open(f"{source_file}-output.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(mapped_header)
        writer.writerows(data[1:])


if __name__ == "__main__":
    main()
