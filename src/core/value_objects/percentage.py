from __future__ import annotations
from dataclasses import dataclass
from typing import Union, Annotated

Number = Union[int, float]


@dataclass(frozen=True)
class Percentage:
    """
    A class representing a percentage value (e.g. 50%, 0.5, etc.)
    with support for arithmetic operations, comparisons, and string formatting.

    Example:
        >>> p1 = Percentage(50)
        >>> p2 = Percentage.from_ratio(0.25)
        >>> (p1 + p2).value
        75.0
        >>> str(p2)
        '25.00%'
        >>> p2.to_ratio()
        0.25
    """

    value: float
    """The percentage value, represented as a number between 0 and 100 inclusive."""

    # ────────────────────────────────────────────────────────────────
    # Construction
    # ────────────────────────────────────────────────────────────────
    def __post_init__(self):
        if not isinstance(self.value, (int, float)):
            raise TypeError("Percentage value must be a numeric type (int or float).")
        if not (0 <= self.value <= 100):
            raise ValueError("Percentage value must be between 0 and 100 inclusive.")

    @classmethod
    def from_ratio(cls, ratio: Number) -> "Percentage":
        """
        Create a Percentage instance from a ratio between 0 and 1.

        Args:
            ratio (Number): A number such as 0.25 representing 25%.

        Returns:
            Percentage: A new instance corresponding to ratio * 100.

        Raises:
            ValueError: If ratio is outside [0, 1].
        """
        if not (0 <= ratio <= 1):
            raise ValueError("Ratio must be between 0 and 1 inclusive.")
        return cls(ratio * 100)

    # ────────────────────────────────────────────────────────────────
    # Conversion utilities
    # ────────────────────────────────────────────────────────────────
    def to_ratio(self) -> float:
        """
        Convert this percentage to its fractional ratio representation.

        Example:
            >>> Percentage(75).to_ratio()
            0.75
        """
        return self.value / 100.0

    def as_decimal(self, places: int = 2) -> str:
        """
        Format the percentage as a string with a specified number of decimal places.

        Args:
            places (int): Number of decimal places to show. Default is 2.

        Returns:
            str: Formatted string such as '45.67%'.
        """
        return f"{self.value:.{places}f}%"

    # ────────────────────────────────────────────────────────────────
    # Arithmetic operations
    # ────────────────────────────────────────────────────────────────
    def __add__(self, other: Union["Percentage", Number]) -> "Percentage":
        """Add two percentages or add a raw numeric delta."""
        other_val = other.value if isinstance(other, Percentage) else other
        return Percentage(min(max(self.value + other_val, 0), 100))

    def __sub__(self, other: Union["Percentage", Number]) -> "Percentage":
        """Subtract another percentage or numeric value."""
        other_val = other.value if isinstance(other, Percentage) else other
        return Percentage(min(max(self.value - other_val, 0), 100))

    def __mul__(self, other: Number) -> "Percentage":
        """Scale a percentage by a numeric multiplier (e.g., p * 0.5)."""
        if not isinstance(other, (int, float)):
            raise TypeError("Can only multiply by a numeric value.")
        return Percentage(min(max(self.value * other, 0), 100))

    def __truediv__(self, other: Number) -> "Percentage":
        """Divide a percentage by a numeric divisor."""
        if not isinstance(other, (int, float)):
            raise TypeError("Can only divide by a numeric value.")
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return Percentage(min(max(self.value / other, 0), 100))

    # ────────────────────────────────────────────────────────────────
    # Comparisons
    # ────────────────────────────────────────────────────────────────
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Percentage):
            return NotImplemented
        return self.value == other.value

    def __lt__(self, other: "Percentage") -> bool:
        return self.value < other.value

    def __le__(self, other: "Percentage") -> bool:
        return self.value <= other.value

    def __gt__(self, other: "Percentage") -> bool:
        return self.value > other.value

    def __ge__(self, other: "Percentage") -> bool:
        return self.value >= other.value

    # ────────────────────────────────────────────────────────────────
    # String representations
    # ────────────────────────────────────────────────────────────────
    def __repr__(self) -> str:
        return f"Percentage(value={self.value:.2f})"

    def __str__(self) -> str:
        return self.as_decimal(2)

    # ────────────────────────────────────────────────────────────────
    # Serialization helpers
    # ────────────────────────────────────────────────────────────────
    def to_json(self) -> dict:
        """
        Serialize this percentage to a dictionary suitable for JSON encoding.
        """
        return {"percentage": self.value}

    @classmethod
    def from_json(cls, data: dict) -> "Percentage":
        """
        Deserialize a Percentage instance from JSON-like data.

        Args:
            data (dict): Dictionary with key 'percentage' containing a numeric value.

        Returns:
            Percentage: Deserialized object.
        """
        if "percentage" not in data:
            raise KeyError("Missing key 'percentage' in data.")
        return cls(float(data["percentage"]))
