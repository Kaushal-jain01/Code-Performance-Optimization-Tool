from typing import TypedDict, Optional

class state(TypedDict):
    performance: Optional[str] = None
    history: Optional[str] = None
    code: Optional[str] = None
    optimizations: Optional[str] = None
    iterations: Optional[int] = None
    performance_compare: Optional[str] = None
    actual_code: Optional[str] = None


