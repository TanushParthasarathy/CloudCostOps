from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class CloudResource:
    provider: str
    account_id: str
    resource_id: str
    name: str
    resource_type: str
    region: str
    monthly_cost: float = 0.0
    status: Optional[str] = None
    cpu_utilization: Optional[float] = None
    attached: Optional[bool] = None
    tags: Dict[str, str] = field(default_factory=dict)