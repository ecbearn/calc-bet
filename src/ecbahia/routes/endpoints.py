from pydantic.dataclasses import dataclass


PREFIX = "/api/lucrative"


@dataclass
class Endpoints:
    post_earning = f"{PREFIX}/earning"
    post_amounts = f"{PREFIX}/amounts"

    post_multi_earnings = f"{PREFIX}/multi-earnings"

    post_earnings = f"{PREFIX}/earnings"
