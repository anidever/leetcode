class Solution:
    def reformatDate(self, date: str) -> str:
        clean = date.split()
        month = [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]
        day, month, year = str(clean[0])[:-2], month.index(clean[1]) + 1, clean[2]
        if len(day) == 1:
            day = f"0{day}"
        if len(str(month)) == 1:
            month = f"0{month}"

        return f"{year}-{month}-{day}"
