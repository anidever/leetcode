from tpying import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tables = set(order[1] for order in orders)
        menu = set(order[2] for order in orders)
        lookup = {table: {item: 0 for item in menu} for table in tables}
        for order in orders:
            lookup[order[1]][order[2]] += 1

        menu = sorted(menu)
        res = [["Table"] + menu]
        for x in sorted(int(table) for table in tables):
            x = str(x)
            holder = [str(lookup[x][item]) for item in menu]
            holder.insert(0, x)
            res.append(holder)

        return res
