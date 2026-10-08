from models.resource import CloudResource


def main():
    resource = CloudResource(
        provider="Azure",
        account_id="example-subscription",
        resource_id="/subscriptions/example/resourceGroups/demo/providers/Microsoft.Compute/virtualMachines/web01",
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

    print("Cloud Resource")
    print("---------------------------")
    print(f"Provider: {resource.provider}")
    print(f"Name: {resource.name}")
    print(f"Type: {resource.resource_type}")
    print(f"Region: {resource.region}")
    print(f"Monthly Cost: ${resource.monthly_cost}")
    print(f"CPU Utilization: {resource.cpu_utilization}%")
    print(f"Status: {resource.status}")
    print(f"Tags: {resource.tags}")


if __name__ == "__main__":
    main()