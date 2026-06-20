"""Control point model."""

from enum import StrEnum


class ControlPointType(StrEnum):
    DESIGN = "design"
    MANUFACTURING = "manufacturing"
    DETECTION_RELEASE = "detection_release"
    SUPPLY_CHAIN = "supply_chain"
    CONFIGURATION_CHANGE = "configuration_change"
    ORGANIZATION = "organization"


class ControlPointFunction(StrEnum):
    PREVENT = "prevent"
    DETECT = "detect"
    ISOLATE = "isolate"
    RELEASE = "release"


class ControlPointStatus(StrEnum):
    EXISTS = "exists"
    MISSING = "missing"
    WEAK = "weak"
    BYPASSED = "bypassed"
    MISCONFIGURED = "misconfigured"
    NOT_VERIFIED = "not_verified"
    NOT_APPLICABLE = "not_applicable"


CONTROL_POINT_LABELS: dict[str, str] = {
    ControlPointType.DESIGN: "设计控制点",
    ControlPointType.MANUFACTURING: "制造过程控制点",
    ControlPointType.DETECTION_RELEASE: "检测与放行控制点",
    ControlPointType.SUPPLY_CHAIN: "供应链控制点",
    ControlPointType.CONFIGURATION_CHANGE: "配置与变更控制点",
    ControlPointType.ORGANIZATION: "组织与管理控制点",
}
