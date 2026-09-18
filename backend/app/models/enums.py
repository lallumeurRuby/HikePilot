import enum


class AnswerType(str, enum.Enum):
    SINGLE_CHOICE = "single_choice"
    MULTI_CHOICE = "multi_choice"
    OPEN_TEXT = "open_text"
    MATRIX_SINGLE_CHOICE = "matrix_single_choice"


class DifficultyLevel(str, enum.Enum):
    EASY = "easy"
    MODERATE = "moderate"
    HARD = "hard"
    EXPERT = "expert"


class OpenStatus(str, enum.Enum):
    OPEN = "open"
    CLOSED = "closed"
    PARTIAL_CLOSED = "partial_closed"


class SectionName(str, enum.Enum):
    ROUTE_SUMMARY = "route_summary"
    ITINERARY = "itinerary"
    WEATHER_CONDITIONS = "weather_conditions"
    RISK_RESPONSE = "risk_response"
    GEAR_SUPPLY = "gear_supply"
    TRANSPORTATION = "transportation"
    EMERGENCY_RESPONSE = "emergency_response"
    PRE_TRIP_CHECKLIST = "pre_trip_checklist"
