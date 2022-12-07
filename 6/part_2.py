class Analyzer:
    counter = 0
    active_stash = []

    def push_new_letter(self, letter):
        self.counter += 1
        if len(self.active_stash) >= 14:
            self.active_stash.pop(0)
        self.active_stash.append(letter)
        result = self._check_for_success_state()
        return result

    def _check_for_success_state(self):
        if len(set(self.active_stash)) == len(self.active_stash) and len(self.active_stash) >= 14:
            return True
        return False

with open("input.txt") as file:
    data = file.read()

analyzer = Analyzer()

for char in data:
    result = analyzer.push_new_letter(char)
    if result is True:
        break
print(analyzer.counter)
