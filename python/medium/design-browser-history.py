class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.pointer = 0
        self.size = len(self.history)

    def visit(self, url: str) -> None:
        # if its new entry add to the history
        if self.pointer + 1 >= len(self.history):
            self.history.append(url)
        else:
            # if its not new entry, update the history
            self.history[self.pointer + 1] = url

        self.pointer += 1
        self.size = self.pointer + 1

    def back(self, steps: int) -> str:
        self.pointer = max(0, self.pointer - steps)
        return self.history[self.pointer]

    def forward(self, steps: int) -> str:
        self.pointer = min(self.size, self.pointer + steps)
        return self.history[self.pointer]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)