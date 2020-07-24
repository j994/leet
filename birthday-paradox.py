import random


class Birthday:
    # Generate birthdays
    def give_birth(self, n):
        return [random.randint(1, 365) for x in range(n)]

    def compare_birth(self):
        results = []
        for x in range(5, 101, 5):
            birthdays = self.give_birth(x)
            answer = len(birthdays) != len(set(birthdays))
            results.append(answer)
        return results


a = Birthday()
b = a.compare_birth()
print(b)
