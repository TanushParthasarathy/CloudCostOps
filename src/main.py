from models.resource import CloudResource


def main():
    # Resource 1: Azure example
    resource1 = CloudResource(
        provider="Azure",
        account_id="example-subscription",
        resource_id="example-resource-id",
        name="web01",
        resource_type="compute",
        region="eastus",
        monthly_cost=180.00,
        status="running",
        cpu_utilization=4.2,
        tags={
            "Environment": "Dev",
            "Owner": "CloudOps"
        }
    )

    # Resource 2: AWS example
    resource2 = CloudResource(
        provider="AWS",
        account_id="example-account",
        resource_id="example-instance",
        name="app01",
        resource_type="compute",
        region="us-east-1",
        monthly_cost=240.00,
        status="running",
        cpu_utilization=65.0,
        tags={"Environment": "Test"}
    )

    # Put both objects into one list
    resources = [resource1, resource2]

    # Create an empty list for optimization findings
    recommendations = []

    print("Cloud Resource Inventory")
    print("---------------------------")

    # Examine every resource
    for resource in resources:
        print(f"Provider: {resource.provider}")
        print(f"Name: {resource.name}")
        print(f"Type: {resource.resource_type}")
        print(f"Region: {resource.region}")
        print(f"Monthly Cost: ${resource.monthly_cost}")
        print(f"CPU Utilization: {resource.cpu_utilization}%")
        print(f"Status: {resource.status}")
        print(f"Tags: {resource.tags}")

        # Check whether CPU is available and below 5%
        if (
            resource.cpu_utilization is not None
            and resource.cpu_utilization < 5
        ):
            recommendations.append(resource)

        print()

    # Print the summary after processing every resource
    print("Optimization Summary")
    print("---------------------------")

    if recommendations:
        for candidate in recommendations:
            print(
                f"{candidate.name}: "
                "Review for possible rightsizing."
            )
    else:
        print("No resources met the current review rule.")


if __name__ == "__main__":
    main()
