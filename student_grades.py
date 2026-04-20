class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.get_by_index(index)
        if score >= 90:
            return "A"
        elif 80 <= score < 90:
            return "B"
        elif 70<=score<80:
            return "C"
        elif 60<=score<70:
            return "D"
        elif 50<=score<60:
            return "E"
        else:
            return "F"

    def find(self, target_score):
        idxs = []
        for i, score in enumerate(self.scores):
            if score == target_score:
                idxs.append(i)
        return idxs

    def get_sorted(self):
        scores = list(self.scores)

        for serazeno_od_konce in range(len(scores)):
            has_changed = False
            for pozice_porovnani in range(len(scores) - 1 - serazeno_od_konce):
                if scores[pozice_porovnani] > scores[pozice_porovnani + 1]:
                    scores[pozice_porovnani], scores[pozice_porovnani + 1] = (
                        scores[pozice_porovnani + 1],
                        scores[pozice_porovnani],
                    )
                    has_changed = True

            if not has_changed:
                break

        return scores




results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
print(results.count())
print(results.get_by_index(2))

print(results.get_grade(2))  # A (91 bodů)
print(results.get_grade(6))  # A (100 bodů)
print(results.get_grade(7))  # F (38 bodů)

print(results.find(100))  # [6]
print(results.find(50))   # [4]
print(results.find(77))   # []

print(results.get_sorted())   # [38, 42, 50, 58, 67, 73, 85, 91, 100]
print(results.scores)         # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny


results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
print(f"Test psalo: {results.count()}")
# for i, score in enumerate(results):jk
#     print(f"Student {i}: {results[score]} points - {results.get_grade(score)}")

# for i, score in enumerate(self.scores):
#     print(f"Student {i}: {score} points - {self.get_grade(score)}")
# for i, score in enumerate(results):
#     print(f"Student {i}: {score} points - {results.get_grade(score)}")
print(f"Indexy studentu s 100 body: {results.find(100)}")
print(f"Serazeno: {results.get_sorted()}")



